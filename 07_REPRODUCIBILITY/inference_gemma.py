import os
import argparse
import pandas as pd
import torch

from kaggle_secrets import UserSecretsClient
from huggingface_hub import login

from transformers import (
    AutoProcessor,
    Gemma3ForConditionalGeneration,
    BitsAndBytesConfig
)

from peft import PeftModel


parser = argparse.ArgumentParser()

parser.add_argument(
    "--language",
    required=True
)

parser.add_argument(
    "--evidence_dir",
    required=True
)

parser.add_argument(
    "--output",
    default="test_predictions_REPRODUCED.csv"
)

args = parser.parse_args()


MODEL_ID = "google/gemma-3-4b-it"


test = pd.read_csv(
    os.path.join(
        args.evidence_dir,
        "test_split.csv"
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


tokenizer.padding_side = "left"


bnb = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.float32
)


base = Gemma3ForConditionalGeneration.from_pretrained(
    MODEL_ID,
    token=hf_token,
    quantization_config=bnb,
    device_map={"": 0},
    torch_dtype=torch.float32,
    attn_implementation="eager"
)


model = PeftModel.from_pretrained(
    base,
    os.path.join(
        args.evidence_dir,
        "lora_adapter"
    ),
    is_trainable=False
)


model.eval()
model.config.use_cache = True


def prompt(source):

    messages = [
        {
            "role": "user",
            "content": (
                f"Translate the following {args.language} sentence into Hindi. "
                "Return only the Hindi translation.\n\n"
                f"{args.language}: {source}"
            )
        }
    ]

    return processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )


predictions = []


for source in test["source"]:

    text = prompt(source)

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=192
    ).to("cuda:0")

    input_len = inputs["input_ids"].shape[1]

    with torch.inference_mode():

        output = model.generate(
            **inputs,
            max_new_tokens=128,
            do_sample=False,
            use_cache=True,
            pad_token_id=tokenizer.pad_token_id
        )

    pred = tokenizer.decode(
        output[0][input_len:],
        skip_special_tokens=True
    ).strip()

    predictions.append(pred)


result = test.copy()

result["prediction"] = predictions

result.to_csv(
    args.output,
    index=False
)


print(
    "Saved:",
    args.output
)
