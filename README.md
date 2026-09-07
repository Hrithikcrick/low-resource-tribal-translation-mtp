<div align="center">
<img src="assets/tribal_ai_banner.svg" width="100%" alt="Tribal Language AI Translation Banner">
<h1>🌍 Low-Resource Tribal Language → Hindi Translation</h1>
<h3>🌿 Language × Culture × Artificial Intelligence 🧠</h3>
<p>
Bhili • Mundari • Gondi → Hindi
</p>
<p>
<img src="https://img.shields.io/badge/Gemma_3--4B-3%2F3_COMPLETE-00c853?style=for-the-badge&logo=google">
<img src="https://img.shields.io/badge/Sarvam_Translate-Gondi_Training-ff9800?style=for-the-badge">
<img src="https://img.shields.io/badge/Fine--Tuning-QLoRA-8338ec?style=for-the-badge">
</p>
<p>
<img src="https://img.shields.io/badge/spBLEU-Translation_Metric-219ebc?style=flat-square">
<img src="https://img.shields.io/badge/ChrF%2B%2B-Translation_Metric-fb8500?style=flat-square">
<img src="https://img.shields.io/badge/COMET-Neural_Metric-ff006e?style=flat-square">
</p>
</div>
<hr>
<h2>✨ Project Vision</h2>
<p>
India has extraordinary linguistic diversity, but many low-resource tribal languages remain underrepresented in modern NLP systems.
</p>
<p>
This research investigates whether multilingual Large Language Models can be efficiently adapted for 
<b>tribal-language → Hindi translation</b> using parameter-efficient fine-tuning.
</p>
<table>
<tr>
<th>Language</th>
<th>Translation Direction</th>
<th>Current Model</th>
</tr>
<tr>
<td>🟣 Bhili</td>
<td>Bhili → Hindi</td>
<td>Gemma 3-4B</td>
</tr>
<tr>
<td>🟠 Mundari</td>
<td>Mundari → Hindi</td>
<td>Gemma 3-4B</td>
</tr>
<tr>
<td>🔵 Gondi</td>
<td>Gondi → Hindi</td>
<td>Gemma 3-4B + Sarvam</td>
</tr>
</table>
<hr>
<div align="center">
<h2>🧠 Low-Resource Languages + AI</h2>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=23&duration=2500&pause=700&color=00D9FF&center=true&vCenter=true&width=850&lines=Bhili+to+Hindi;Mundari+to+Hindi;Gondi+to+Hindi;Low-Resource+Languages+%2B+AI;Language+Preservation+through+Technology" alt="Animated Language AI Text">
</div>
<hr>
<h2>🏆 Gemma 3-4B Results</h2>
<div align="center">
<img src="assets/gemma_results.svg" width="100%" alt="Gemma Translation Results">
</div>
<br>
<table>
<thead>
<tr>
<th>🌐 Language</th>
<th>🔵 spBLEU</th>
<th>🟠 ChrF++</th>
<th>🟣 COMET</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>Bhili → Hindi</b></td>
<td><b>23.2592</b></td>
<td><b>46.5085</b></td>
<td><b>0.651306</b></td>
<td>✅ Complete</td>
</tr>
<tr>
<td><b>Mundari → Hindi</b></td>
<td><b>18.101908</b></td>
<td><b>32.098273</b></td>
<td><b>0.564452</b></td>
<td>✅ Complete</td>
</tr>
<tr>
<td><b>Gondi → Hindi</b></td>
<td><b>14.432006</b></td>
<td><b>28.800049</b></td>
<td><b>0.580771</b></td>
<td>✅ Complete</td>
</tr>
</tbody>
</table>
<blockquote>
🥇 Bhili currently gives the strongest Gemma 3-4B translation performance across the three evaluated languages.
</blockquote>
<hr>
<h2>🚦 Experiment Progress</h2>
<table>
<tr>
<th>Model</th>
<th>Bhili</th>
<th>Mundari</th>
<th>Gondi</th>
</tr>
<tr>
<td>🧠 Gemma 3-4B</td>
<td>✅ Complete</td>
<td>✅ Complete</td>
<td>✅ Complete</td>
</tr>
<tr>
<td>🇮🇳 Sarvam Translate</td>
<td>⏳ Pending</td>
<td>⏳ Pending</td>
<td>🔄 Training</td>
</tr>
</table>
<div align="center">
<h3>Overall Progress</h3>
<img src="https://img.shields.io/badge/Completed-3%20of%206-00c853?style=for-the-badge">
<img src="https://img.shields.io/badge/Gemma-100%25_COMPLETE-3a86ff?style=for-the-badge">
</div>
<hr>
<h2>⚙️ Fine-Tuning Configuration</h2>
<table>
<tr>
<td><b>Base Model</b></td>
<td>google/gemma-3-4b-it</td>
</tr>
<tr>
<td><b>Fine-Tuning</b></td>
<td>QLoRA</td>
</tr>
<tr>
<td><b>Quantization</b></td>
<td>4-bit NF4</td>
</tr>
<tr>
<td><b>Training Steps</b></td>
<td>500</td>
</tr>
<tr>
<td><b>Learning Rate</b></td>
<td>1e-4</td>
</tr>
<tr>
<td><b>LoRA Rank</b></td>
<td>16</td>
</tr>
<tr>
<td><b>LoRA Alpha</b></td>
<td>32</td>
</tr>
<tr>
<td><b>LoRA Dropout</b></td>
<td>0.05</td>
</tr>
<tr>
<td><b>Seed</b></td>
<td>42</td>
</tr>
<tr>
<td><b>Dataset Split</b></td>
<td>90% Train / 5% Validation / 5% Test</td>
</tr>
</table>
<h3>🎯 LoRA Target Modules</h3>
<p>
<code>q_proj</code> &nbsp;
<code>k_proj</code> &nbsp;
<code>v_proj</code> &nbsp;
<code>o_proj</code> &nbsp;
<code>gate_proj</code> &nbsp;
<code>up_proj</code> &nbsp;
<code>down_proj</code>
</p>
<hr>
<h2>🔄 Translation Workflow</h2>
<div align="center">
<table>
<tr>
<td align="center">🌿<br><b>Tribal Sentence</b></td>
<td align="center">➡️</td>
<td align="center">🧹<br><b>Cleaning</b></td>
<td align="center">➡️</td>
<td align="center">✂️<br><b>90/5/5 Split</b></td>
<td align="center">➡️</td>
<td align="center">🧠<br><b>LLM</b></td>
<td align="center">➡️</td>
<td align="center">⚡<br><b>QLoRA</b></td>
<td align="center">➡️</td>
<td align="center">🇮🇳<br><b>Hindi</b></td>
</tr>
</table>
<br>
<table>
<tr>
<td>📊 spBLEU</td>
<td>📊 ChrF++</td>
<td>🧠 COMET</td>
</tr>
</table>
</div>
<hr>
<h2>📊 Evaluation Metrics</h2>
<details>
<summary><b>🔵 spBLEU</b></summary>
<br>
<p>SentencePiece-aware BLEU evaluation used for multilingual translation quality.</p>
</details>
<details>
<summary><b>🟠 ChrF++</b></summary>
<br>
<p>Character and word n-gram F-score useful for evaluating morphologically rich languages.</p>
</details>
<details>
<summary><b>🟣 COMET</b></summary>
<br>
<p>Neural machine-translation evaluation using <code>Unbabel/wmt22-comet-da</code>.</p>
</details>
<hr>
<h2>📁 Repository Structure</h2>
<table>
<tr>
<th>Directory</th>
<th>Purpose</th>
</tr>
<tr>
<td><code>00_Master</code></td>
<td>Master results and experiment tracker</td>
</tr>
<tr>
<td><code>01_Gemma3_4B_Bhili</code></td>
<td>Bhili → Hindi experiment</td>
</tr>
<tr>
<td><code>02_Gemma3_4B_Mundari</code></td>
<td>Mundari → Hindi experiment</td>
</tr>
<tr>
<td><code>03_Gemma3_4B_Gondi</code></td>
<td>Gondi → Hindi experiment</td>
</tr>
<tr>
<td><code>04_Sarvam_Bhili</code></td>
<td>Sarvam Bhili experiment</td>
</tr>
<tr>
<td><code>05_Sarvam_Mundari</code></td>
<td>Sarvam Mundari experiment</td>
</tr>
<tr>
<td><code>06_Sarvam_Gondi</code></td>
<td>Sarvam Gondi experiment</td>
</tr>
<tr>
<td><code>07_REPRODUCIBILITY</code></td>
<td>Training, inference and evaluation code</td>
</tr>
</table>
<hr>
<h2>♻️ Reproducibility</h2>
<p>The reproducibility package contains:</p>
<table>
<tr>
<td>✅</td>
<td>Experiment configuration</td>
</tr>
<tr>
<td>✅</td>
<td>Training scripts</td>
</tr>
<tr>
<td>✅</td>
<td>Inference scripts</td>
</tr>
<tr>
<td>✅</td>
<td>Evaluation scripts</td>
</tr>
<tr>
<td>✅</td>
<td>Dependency versions</td>
</tr>
<tr>
<td>✅</td>
<td>SHA256 artifact hashes</td>
</tr>
<tr>
<td>✅</td>
<td>Master results</td>
</tr>
</table>
<p>
Large checkpoints and evidence archives are stored separately because of GitHub file-size limitations.
</p>
<hr>
<h2>🧭 Research Roadmap</h2>
<table>
<tr>
<th>Stage</th>
<th>Experiment</th>
<th>Status</th>
</tr>
<tr>
<td>1</td>
<td>Gemma 3-4B • Bhili → Hindi</td>
<td>✅ Complete</td>
</tr>
<tr>
<td>2</td>
<td>Gemma 3-4B • Mundari → Hindi</td>
<td>✅ Complete</td>
</tr>
<tr>
<td>3</td>
<td>Gemma 3-4B • Gondi → Hindi</td>
<td>✅ Complete</td>
</tr>
<tr>
<td>4</td>
<td>Sarvam Translate • Gondi → Hindi</td>
<td>🔄 Training</td>
</tr>
<tr>
<td>5</td>
<td>Sarvam Translate • Mundari → Hindi</td>
<td>⏳ Pending</td>
</tr>
<tr>
<td>6</td>
<td>Sarvam Translate • Bhili → Hindi</td>
<td>⏳ Pending</td>
</tr>
</table>
<hr>
<div align="center">
<h2>🌱 Why This Matters</h2>
<blockquote>
Every language carries knowledge, identity, culture and history.
</blockquote>
<p>
This project explores how modern AI can extend machine translation technology to languages that historically received far less computational representation.
</p>
<h3>🌿 Language &nbsp; × &nbsp; 🧠 Artificial Intelligence &nbsp; × &nbsp; 🇮🇳 India</h3>
</div>
