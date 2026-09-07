# Low-Resource Tribal Language to Hindi Translation

M.Tech research project on low-resource machine translation using parameter-efficient fine-tuning.

## Experiment Status

| Model | Bhili | Mundari | Gondi |
|---|---|---|---|
| Gemma 3-4B | Complete | Complete | Complete |
| Sarvam Translate | Pending | Pending | Training |

## Gemma 3-4B Results

| Language | spBLEU | ChrF++ | COMET |
|---|---:|---:|---:|
| Bhili | 23.2592 | 46.5085 | 0.651306 |
| Mundari | 18.101908 | 32.098273 | 0.564452 |
| Gondi | 14.432006 | 28.800049 | 0.580771 |

## Fine-Tuning

- Base model: google/gemma-3-4b-it
- Method: QLoRA
- 4-bit NF4 quantization
- LoRA rank: 16
- LoRA alpha: 32
- LoRA dropout: 0.05
- Training steps: 500
- Learning rate: 1e-4
- Seed: 42
- Data split: 90 / 5 / 5

## Evaluation

- spBLEU
- ChrF++
- COMET: Unbabel/wmt22-comet-da

## Repository Structure

`	ext
00_Master/
01_Gemma3_4B_Bhili/
02_Gemma3_4B_Mundari/
03_Gemma3_4B_Gondi/
04_Sarvam_Bhili/
05_Sarvam_Mundari/
06_Sarvam_Gondi/
07_REPRODUCIBILITY/
`",
",


See 07_REPRODUCIBILITY for:

- training code
- inference code
- evaluation code
- experiment configuration
- requirements
- SHA256 hashes

## Large Artifacts

Large checkpoints and evidence ZIP files are excluded from GitHub and stored separately.
