<p align="center">
  <img src="assets/tribal_ai_banner.svg" width="100%" alt="Tribal Language AI Translation"/>
</p>
<h1 align="center">🌍 Low-Resource Tribal Language → Hindi Translation</h1>
<p align="center">
  <b>Preserving linguistic diversity through Artificial Intelligence</b>
</p>
<p align="center">
  Bhili • Mundari • Gondi → Hindi
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Gemma_3--4B-3%2F3_COMPLETE-00c853?style=for-the-badge&logo=google"/>
  <img src="https://img.shields.io/badge/Sarvam_Translate-Gondi_Training-ff9800?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Fine--Tuning-QLoRA-8338ec?style=for-the-badge"/>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/spBLEU-Evaluation-219ebc?style=flat-square"/>
  <img src="https://img.shields.io/badge/ChrF%2B%2B-Evaluation-fb8500?style=flat-square"/>
  <img src="https://img.shields.io/badge/COMET-Evaluation-ff006e?style=flat-square"/>
</p>
---
## ✨ Project Vision
India has extraordinary linguistic diversity, including many low-resource tribal languages that are underrepresented in modern NLP systems.
This research investigates whether modern multilingual Large Language Models can be efficiently adapted for **tribal-language → Hindi translation** using parameter-efficient fine-tuning.
The current experiments study:
- 🟣 **Bhili → Hindi**
- 🟠 **Mundari → Hindi**
- 🔵 **Gondi → Hindi**
using:
- 🧠 Gemma 3-4B
- 🇮🇳 Sarvam Translate
- ⚡ QLoRA parameter-efficient fine-tuning
- 📊 spBLEU, ChrF++ and COMET evaluation
---
## 🧠 AI × Language × Cultural Diversity
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=23&duration=2500&pause=700&color=00D9FF&center=true&vCenter=true&width=850&lines=Bhili+%E2%86%92+Hindi;Mundari+%E2%86%92+Hindi;Gondi+%E2%86%92+Hindi;Low-Resource+Languages+%2B+AI;Preserving+Language+Through+Technology" alt="Typing SVG"/>
</p>
---
## 🏆 Gemma 3-4B Results
<p align="center">
  <img src="assets/gemma_results.svg" width="100%" alt="Gemma Translation Results"/>
</p>
| 🌐 Language | 🔵 spBLEU | 🟠 ChrF++ | 🟣 COMET | Status |
|---|---:|---:|---:|---|
| **Bhili → Hindi** | **23.2592** | **46.5085** | **0.651306** | ✅ Complete |
| **Mundari → Hindi** | **18.101908** | **32.098273** | **0.564452** | ✅ Complete |
| **Gondi → Hindi** | **14.432006** | **28.800049** | **0.580771** | ✅ Complete |
> 🥇 Bhili currently achieves the strongest overall Gemma translation performance.
---
## 🚦 Experiment Progress
| Model | Bhili | Mundari | Gondi |
|---|:---:|:---:|:---:|
| 🧠 **Gemma 3-4B** | ✅ | ✅ | ✅ |
| 🇮🇳 **Sarvam Translate** | ⏳ | ⏳ | 🔄 |
**Completed:** `3 / 6` model-language experiments
---
## ⚙️ Fine-Tuning Configuration
```yaml
Base Model: google/gemma-3-4b-it
Method: QLoRA
Quantization: 4-bit NF4
Training Steps: 500
Learning Rate: 1e-4
LoRA Rank: 16
LoRA Alpha: 32
LoRA Dropout: 0.05
Seed: 42
Split: 90% Train / 5% Validation / 5% Test
```
### LoRA Targets
```text
q_proj    k_proj    v_proj    o_proj
gate_proj    up_proj    down_proj
```
---
## 🔄 Translation Pipeline
```mermaid
flowchart LR
    A["🌿 Tribal Language Sentence"] --> B["🧹 Dataset Cleaning"]
    B --> C["✂️ 90 / 5 / 5 Split"]
    C --> D["🧠 Base LLM"]
    D --> E["⚡ QLoRA Fine-Tuning"]
    E --> F["🇮🇳 Hindi Translation"]
    F --> G["📊 spBLEU"]
    F --> H["📊 ChrF++"]
    F --> I["📊 COMET"]
```
---
## 📊 Evaluation Metrics
### 🔵 spBLEU
SentencePiece-aware BLEU evaluation for multilingual translation quality.
### 🟠 ChrF++
Character and word n-gram F-score that is particularly useful for morphologically rich languages.
### 🟣 COMET
Neural machine-translation evaluation using:
`Unbabel/wmt22-comet-da`
---
## 📁 Repository Structure
```text
MTP_FINAL/
│
├── 00_Master/
│   ├── MTP_FINAL_RESULTS.csv
│   └── Experiment Tracker
│
├── 01_Gemma3_4B_Bhili/
├── 02_Gemma3_4B_Mundari/
├── 03_Gemma3_4B_Gondi/
│
├── 04_Sarvam_Bhili/
├── 05_Sarvam_Mundari/
├── 06_Sarvam_Gondi/
│
├── 07_REPRODUCIBILITY/
│   ├── train_gemma.py
│   ├── inference_gemma.py
│   ├── evaluate.py
│   ├── experiment_config.json
│   ├── requirements.txt
│   └── FILE_HASHES_SHA256.csv
│
└── assets/
    ├── tribal_ai_banner.svg
    └── gemma_results.svg
```
---
## ♻️ Reproducibility
The repository contains reproducibility material for the experiments:
- ✅ exact experiment configuration
- ✅ training scripts
- ✅ inference scripts
- ✅ evaluation scripts
- ✅ dependency versions
- ✅ SHA256 artifact hashes
- ✅ master result table
- ✅ final prediction CSVs where applicable
Large checkpoints and evidence archives are stored separately because of GitHub file-size limitations.
---
## 🔬 Current Research Roadmap
```text
Gemma 3-4B
├── Bhili → Hindi       ✅
├── Mundari → Hindi     ✅
└── Gondi → Hindi       ✅

Sarvam Translate
├── Gondi → Hindi       🔄 Training
├── Mundari → Hindi     ⏳ Next
└── Bhili → Hindi       ⏳
```
---
## 🌱 Motivation
> Every language carries knowledge, culture, identity and history.
This project explores how modern AI can help extend machine translation technology to languages that have historically received far less computational representation.
---
<p align="center">
  <b>🌿 Language × Culture × Artificial Intelligence 🧠</b>
</p>
<p align="center">
  <sub>Low-Resource Tribal Language Translation Research</sub>
</p>
