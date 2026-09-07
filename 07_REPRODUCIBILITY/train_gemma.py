import os
import argparse
import gc
import json

import pandas as pd
import torch

from datasets import Dataset
from kaggle_secrets import UserSecretsClient
from huggingface_hub import login

from transformers import (
    AutoProcessor,
    Gemma3ForConditionalGeneration,
    BitsAndBytesConfig
)

from peft import (
    LoraConfig,
    get_peft_model,
    prepare_model_for_kbit_training
)

from trl import SFTTrainer, SFTConfig


parser = argparse.ArgumentParser()

parser.add_argument("--language", required=True)

parser.add_argument(
    "--evidence_dir",
    required=True
)

parser.add_argument(
    "--output_dir",
    default="./training_output"
)

args = parser.parse_args()


MODEL_ID = "google/gemma-3-4b-it"


train_df = pd.read_csv(
    os.path.join(
        args.evidence_dir,
        "train_split.csv"
    )
)


hf_token = (
    UserSecretsClient()
    .get_secret("HF_TOKEN")
)


login(
    token=hf_token,
    add_to_git_credential=False
)


processor = AutoProcessor.from_pretrained(
    MODEL_ID,
    token=hf_token
)


tokenizer = processor.tokenizer


if tokenizer.pad_token_id is None:
    tokenizer.pad_token = tokenizer.eos_token


def make_text(source, target):

    messages = [
        {
            "role": "user",
            "content": (
                f"Translate the following {args.language} sentence into Hindi. "
                "Return only the Hindi translation.\n\n"
                f"{args.language}: {source}"
            )
        },
        {
            "role": "assistant",
            "content": str(target)
        }
    ]

    return processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=False
    )


texts = [
    make_text(
        row.source,
        row.target
    )
    for row in train_df.itertuples(index=False)
]


dataset = Dataset.from_dict(
    {"text": texts}
)


del texts
gc.collect()


bnb = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.float16
)


model = Gemma3ForConditionalGeneration.from_pretrained(
    MODEL_ID,
    token=hf_token,
    quantization_config=bnb,
    device_map="auto",
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True
)


model.config.use_cache = False


model = prepare_model_for_kbit_training(
    model,
    use_gradient_checkpointing=True
)


suffixes = (
    "q_proj",
    "k_proj",
    "v_proj",
    "o_proj",
    "gate_proj",
    "up_proj",
    "down_proj"
)


targets = sorted(
    {
        name
        for name, module in model.named_modules()
        if "language_model" in name
        and name.endswith(suffixes)
    }
)


lora = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=targets
)


model = get_peft_model(
    model,
    lora
)


config = SFTConfig(
    output_dir=args.output_dir,
    max_steps=500,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    learning_rate=1e-4,
    warmup_ratio=0.03,
    logging_steps=1,
    save_strategy="steps",
    save_steps=100,
    save_total_limit=5,
    eval_strategy="no",
    fp16=True,
    bf16=False,
    gradient_checkpointing=True,
    optim="paged_adamw_8bit",
    max_length=192,
    dataset_text_field="text",
    packing=False,
    report_to="none",
    remove_unused_columns=True,
    seed=42
)


trainer = SFTTrainer(
    model=model,
    args=config,
    train_dataset=dataset,
    processing_class=tokenizer
)


trainer.train()


adapter_dir = os.path.join(
    args.evidence_dir,
    "lora_adapter_reproduced"
)


trainer.model.save_pretrained(
    adapter_dir
)


tokenizer.save_pretrained(
    adapter_dir
)


print(
    "Training complete:",
    trainer.state.global_step
)
