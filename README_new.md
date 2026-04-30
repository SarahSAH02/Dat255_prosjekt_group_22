# 🩺 Multi-label sykdomsdeteksjon i brystrøntgen (Chest X-rays)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=flat&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/status-completed-brightgreen)]()

---

## 🎥 Demo

![Demo](assets/demo.gif)

---

## 🚀 Kort om prosjektet

Dette prosjektet (DAT255 – Deep Learning Engineering) utvikler og sammenligner deep learning-modeller for å identifisere **14 patologier i brystrøntgenbilder**.

Fokus:
- Multi-label klassifikasjon  
- Klasseubalanse  
- Terskeloptimalisering  
- Modellforklarbarhet (Grad-CAM)  

---

## 🎯 Problemstilling

> Hvordan påvirker modellarkitektur klassifisering av patologier i brystrøntgenbilder, og hvordan kan terskeloptimalisering forbedre ytelsen i ubalanserte datasett?

---

## 🧠 Modeller

Vi sammenligner:

- **Baseline CNN (egenutviklet)**
- ResNet18  
- DenseNet121  
- EfficientNet-B0  

Alle modeller er tilpasset multi-label klassifikasjon (14 outputs med sigmoid).

---

## 📊 Datasett

**CheXpert (small)**

- 14 patologier  
- Multi-label  
- Sterkt ubalansert  
- Inneholder usikre labels  

### Label-håndtering:
```python
1 = positiv
0 / -1 / NaN = negativ

### 🔀 Datasplitting
Trening: 80.2%
Validering: 10.0%
Test: 9.9%

✔ Splittet på pasientnivå (unngår datalekkasje)

### ⚙️ Treningsoppsett
Loss: BCEWithLogitsLoss
Optimizer: AdamW
Learning rate: 1e-4
Weight decay: 1e-4

### 🔄 Pipeline
CSV → Preprosessering → Augmentering → Modell → Prediksjon → Threshold tuning → Evaluering

### 📈 Evalueringsmetrikker
F1-score (macro)
ROC-AUC
Confusion matrix

### 🎯 Terskeloptimalisering
I stedet for fast terskel (0.5):

Optimaliseres per klasse
Basert på valideringssett
Maksimerer F1-score

💡 Kritisk for ytelse i ubalanserte datasett

### 📊 Resultater
Modell	Mean AUC	Macro F1
Baseline CNN	0.6668	0.2790
ResNet18	0.7752	0.3926
EfficientNet-B0	0.7889	~0.40
DenseNet121	~0.78	0.4100
🔑 Viktige innsikter
Pretrained modeller >> baseline
EfficientNet & DenseNet best
Threshold tuning gir stor forbedring
Pneumonia er vanskeligst klasse

### 🔍 Forklarbarhet (Grad-CAM)
Pleural Effusion	Pneumonia

	

✔ Viser hvor modellen "ser"
✔ Øker tillit og tolkbarhet

### 🌐 Deployment (Web App)

Bygget med Streamlit

✨ Funksjoner
Last opp røntgenbilde
Prediker 14 patologier
Vis sannsynligheter
Grad-CAM visualisering

### ▶️ Kjør lokalt
git clone https://github.com/brukernavn/DAT255-Chest-Xray.git
cd DAT255-Chest-Xray
pip install -r requirements.txt
streamlit run app.py

### 📁 Prosjektstruktur
project/
│── data/
│── models/
│── notebooks/
│── src/
│── app/
│── results/
│── README.md

### ⚠️ Begrensninger
Klasseubalanse ikke håndtert i loss
Usikre labels behandles som negative
Nedskalert datasett
Begrenset generalisering

### 🛠️ Teknologi
Python
PyTorch
Streamlit
NumPy / Pandas

