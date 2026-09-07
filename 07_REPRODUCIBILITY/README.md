# MTP Reproducibility Package

## Project

Low-resource tribal language → Hindi translation.

Gemma 3-4B was fine-tuned separately for:

- Bhili → Hindi
- Mundari → Hindi
- Gondi → Hindi

using QLoRA.

---

## Base model

google/gemma-3-4b-it

The base Gemma model is NOT stored in this folder.

To reproduce inference:

Base Gemma 3-4B
+
the appropriate LoRA adapter
=
fine-tuned translation model

The LoRA adapter is stored inside each language's FINAL_Evidence ZIP.

---

## Training method

QLoRA

Base model:
4-bit NF4 quantization

LoRA:

r = 16
alpha = 32
dropout = 0.05

Target modules:

q_proj
k_proj
v_proj
o_proj
gate_proj
up_proj
down_proj

Only language_model modules were adapted.

---

## Training configuration

500 optimizer steps

learning rate = 1e-4

warmup ratio = 0.03

batch size / device = 1

gradient accumulation = 4

maximum sequence length = 192

optimizer = paged_adamw_8bit

seed = 42

---

## Dataset split

For every language:

90% training
5% validation
5% test

random_state = 42

Exact splits are stored inside the corresponding FINAL_Evidence ZIP.

SHA256 hashes for the splits are stored in:

split_hashes.json

---

## Prompt template

Training and inference used the pattern:

Translate the following <LANGUAGE> sentence into Hindi.
Return only the Hindi translation.

<LANGUAGE>: <source sentence>

The assistant target during supervised fine-tuning was the Hindi reference translation.

---

## Inference configuration

padding_side = left

use_cache = True

do_sample = False

max_new_tokens = 128

batch_per_gpu = 8

2 × NVIDIA Tesla T4

4-bit NF4 model

bitsandbytes inference compute dtype = float32

attention implementation = eager

The left-padding configuration was important for stable batched Gemma generation.

---

## Metrics

### spBLEU

SacreBLEU

tokenize = flores200

### ChrF++

SacreBLEU CHRF

word_order = 2

### COMET

Unbabel/wmt22-comet-da

Input:

src = tribal-language sentence

mt = generated Hindi translation

ref = Hindi reference

---

## Reproducing a language experiment

Example for Gondi.

1. Extract:

03_Gemma3_4B_Gondi/
Gemma3_4B_Gondi_Hindi_FINAL_Evidence.zip

2. Locate:

train_split.csv
val_split.csv
test_split.csv
lora_adapter/
training_metadata.json
split_hashes.json

3. Install:

pip install -r requirements.txt

4. Train again:

python train_gemma.py --language Gondi --evidence_dir <path>

5. Run inference:

python inference_gemma.py --language Gondi --evidence_dir <path>

6. Evaluate:

python evaluate.py --predictions <test_predictions_FINAL.csv>

---

## Important artifacts

For every experiment preserve:

FINAL_Evidence.zip
checkpoint500_FINAL.zip
FINAL_RESULTS.zip
test_predictions_FINAL.csv
test_predictions_with_COMET.csv

The project-level results are stored in:

00_Master/MTP_FINAL_RESULTS.csv

---

## Verification

FILE_HASHES_SHA256.csv contains SHA256 hashes of the stored final project artifacts.

These hashes can be used to verify that files have not changed.

---

## Environment

Run:

python capture_kaggle_environment.py

inside the Kaggle runtime to record:

Python version
PyTorch version
CUDA version
GPU model
pip freeze

For maximum publication-quality reproducibility, retain the generated environment report.
