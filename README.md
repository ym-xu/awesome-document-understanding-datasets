# 📚 Awesome Document Understanding Datasets

This repository collects major datasets used in **Document Understanding (DU)** research, covering tasks like OCR, form understanding, table extraction, document VQA, key information extraction, and multimodal document reasoning.

We aim to provide:
- ✅ An organized list of DU datasets
- ✅ Paper references and official links
- ✅ A one-click script to download datasets locally

---

## 🗂️ Dataset Categories

### 🖼️ 1. OCR & Layout Analysis

| Dataset     | Description                       | Size   | Language | Paper / Link | 🛠️ In Script? |
|-------------|-----------------------------------|--------|----------|----------------|--------|
| RVL-CDIP    | Document classification (16 types)| 400k+  | English  | [📄](https://arxiv.org/abs/1505.03850), [🔗](https://www.cs.cmu.edu/~aharley/rvl-cdip/) |
| PubLayNet   | Layout segmentation in papers     | 360k   | English  | [📄](https://arxiv.org/abs/1908.07836), [🔗](https://github.com/ibm-aur-nlp/PubLayNet) |
| DocBank     | Document layout annotations       | 500k+  | English  | [📄](https://arxiv.org/abs/2006.01038), [🔗](https://github.com/doc-analysis/DocBank) |
| IIT-CDIP    | Scanned documents for OCR         | 11M+   | English  | [🔗](https://www.cs.cmu.edu/~aharley/rvl-cdip/) |

---

### 🧾 2. Form Understanding & Key Information Extraction (KIE)

| Dataset     | Description                       | Size   | Language | Paper / Link | 🛠️ In Script? |
|-------------|-----------------------------------|--------|----------|----------------|--------|
| FUNSD       | Form + OCR + entity linking       | 199    | English  | [📄](https://arxiv.org/abs/1905.13538), [🔗](https://guillaumejaume.github.io/FUNSD/) |
| CORD        | Receipt KIE                       | 1,000+ | KR/EN    | [📄](https://arxiv.org/abs/1912.03299), [🔗](https://github.com/clovaai/cord) |
| XFUND       | Multilingual form understanding   | 1,000+ | 7 langs  | [📄](https://arxiv.org/abs/2102.08903), [🔗](https://github.com/doc-analysis/XFUND) |
| SROIE       | Invoice info extraction           | ~1,000 | English  | [🔗](https://rrc.cvc.uab.es/?ch=13) |
| Kleister-NDA   | Legal      | NDA entity extraction               | English  | [📄](https://arxiv.org/abs/2003.04988), [🔗](https://github.com/applicaai/kleister-nda) |
---

### 📊 3. Table Detection & Structure Recognition

| Dataset     | Description                       | Size   | Language | Paper / Link | 🛠️ In Script? |
|-------------|-----------------------------------|--------|----------|----------------|--------|
| TableBank   | Table detection (Word/PDF)        | 417k   | EN/CH    | [📄](https://arxiv.org/abs/1903.10676), [🔗](https://doc-analysis.github.io/tablebank-page/) |
| SciTSR      | Table structure recognition       | 12k    | English  | [📄](https://arxiv.org/abs/1911.04994), [🔗](https://github.com/abc-nlp/SciTSR) |
| SciCap      | Table caption generation          | 12k    | English  | [📄](https://arxiv.org/abs/2010.03150), [🔗](https://github.com/lichengunc/SciCap) |

---

### ❓ 4. Document Visual Question Answering (DocVQA)

| Dataset     | Description                       | Size   | Language | Paper / Link | 🛠️ In Script? |
|-------------|-----------------------------------|--------|----------|----------------|--------|
| DocVQA      | VQA on real documents             | 50k+   | English  | [📄](https://arxiv.org/abs/2007.00398), [🔗](https://docvqa.org/) |
| InfographicVQA| VQA on infographic-style images | 5k+    | English  | [📄](https://arxiv.org/abs/2206.01091), [🔗](https://github.com/google-research-datasets/infographicVQA) |
| VisualMRC   | Multimodal long-doc QA            | 12k    | English  | [📄](https://arxiv.org/abs/2311.04180), [🔗](https://github.com/hpanwar08/VisualMRC) |

---

### 🌍 5. Multilingual Document Understanding

| Dataset     | Description                       | Language | Paper / Link | 🛠️ In Script? |
|-------------|-----------------------------------|----------|----------------|----------|
| XFUND       | Form understanding (7 languages)  | 7 langs  | [📄](https://arxiv.org/abs/2102.08903), [🔗](https://github.com/doc-analysis/XFUND) |
| MLDoc       | Multilingual classification       | 8 langs  | [📄](https://arxiv.org/abs/1811.00218), [🔗](https://github.com/facebookresearch/MLDoc) |

---

### 📌 6. Domain-Specific Document Datasets

| Dataset        | Domain     | Description                         | Language | Paper / Link | 🛠️ In Script? |
|----------------|------------|-------------------------------------|----------|----------------|----------|
| Kleister-NDA   | Legal      | NDA entity extraction               | English  | [📄](https://arxiv.org/abs/2003.04988), [🔗](https://github.com/applicaai/kleister-nda) |
| SciDocs        | Academic   | Citation prediction and doc linkage| English  | [📄](https://arxiv.org/abs/2004.07180), [🔗](https://github.com/allenai/scidocs) |
| EU-LEGIS       | Legal      | Multilingual EU legal documents     | Multi    | [📄](https://arxiv.org/abs/2305.15386), [🔗](https://huggingface.co/datasets/ferretj/eulegis) |

---

## 📥 Download All Datasets with One Command

This project provides a script to automatically download datasets listed above.

### 🔧 Usage Examples

```bash
# Download all datasets
python scripts/download_all.py

# Download a single dataset (e.g., FUNSD)
python scripts/download_all.py --only funsd

# List all available dataset keys
python scripts/download_all.py --list
```

### 📄 Config file

The script reads from scripts/datasets_config.json, which contains download URLs, formats (zip / tar.gz), and target folders.

#### 🧩 Example entry in config:

```
"funsd": {
  "name": "FUNSD",
  "url": "https://guillaumejaume.github.io/FUNSD/dataset.zip",
  "filetype": "zip",
  "target_dir": "funsd"
}
```

---

## 🙌 Contributing

Have a dataset we missed? Feel free to open a pull request or issue!

Please follow the format in `datasets_config.json` and include:
- Dataset name
- Task type
- URL
- Paper link (if available)
- License info

---

## 📜 License

This project is under the MIT License, but datasets themselves may have different licenses. Please refer to individual dataset links for license terms.
