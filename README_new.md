# Multi-Label Classification of Chest X-rays with Uncertainty Exploration

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=flat&logo=PyTorch&logoColor=white)](https://pytorch.org/)

Dette prosjektet utforsker bruk av dyplæring for automatisk klassifisering av thorax-patologier fra røntgenbilder. Målet er å utvikle et system som kan predikere flere sykdommer samtidig (multi-label) og samtidig gi innsikt i modellens beslutninger gjennom forklarbarhet.

---

## 👥 Prosjektgruppe

- Astrid I. Bensnes  
- Mannat Gabria  
- Amna Zafar  
- Sarah S. Ahsan  

---

## 📊 Dataset

Vi benytter en kuratert versjon av **CheXpert-datasettet** fra Kaggle (`ashery/chexpert`).

- ~200k røntgenbilder  
- Multi-label annotasjoner  
- Inneholder usikre labels  

Datasettet er splittet slik at pasienter ikke overlapper:

- **Train (80%)**
- **Validation (10%)**
- **Test (10%)**

---

## 🧠 Modeller

Vi har eksperimentert med flere modeller:

- **SimpleCNN (baseline)**
- **ResNet-18 (hovedmodell)**
- **DenseNet121 (eksperimentell)**

Alle modellene håndterer multi-label klassifisering med `BCEWithLogitsLoss`.

---

## ⚖️ Modellvalg

Flere modeller ga sammenlignbar ytelse, men **ResNet-18** ble valgt som hovedmodell.

Valget er basert på:

- stabil og konsistent ytelse  
- god balanse mellom kompleksitet og resultat  
- enklere og mer robust treningsprosess  
- bedre integrasjon i vår pipeline  

Dette reflekterer et bevisst valg hvor vi prioriterer **robusthet og konsistens**, ikke kun høyeste metrikk.

---

## 📈 Resultater

| Metrikk                              | Verdi      |
|-------------------------------------|-----------|
| Gjennomsnittlig AUC (14 klasser)    | 0.7683    |
| Valideringstap                      | 0.2900    |
| Beste F1-score                      | 0.74      |
| Laveste F1-score                    | 0.13      |

**Observasjoner:**
- Modellen presterer best på tydelige patologier (f.eks. pleural effusion)
- Vanskeligere klasser skyldes ofte **klasseubalanse og diffuse mønstre**

---

## 🔍 Forklarbarhet og Usikkerhet

### Grad-CAM

Vi bruker **Grad-CAM** for å visualisere hvor modellen fokuserer i bildet.

Dette gjør det mulig å:
- verifisere medisinsk relevante områder  
- øke transparens  
- identifisere feilaktig fokus  

---

### Monte Carlo Dropout

Vi utforsker også **MC Dropout** for å estimere modellens usikkerhet ved prediksjon.

---

## 🌐 Webapplikasjon

Vi har utviklet en interaktiv webapplikasjon med **Streamlit**.

Applikasjonen lar brukeren:

- laste opp et røntgenbilde  
- få prediksjoner for alle klasser  
- se sannsynligheter per sykdom  
- visualisere modellens fokus med Grad-CAM  

Modellen lastes fra en `.pth`-fil og brukes til sanntids inferens.

---

## 📁 Prosjektstruktur

```bash
DAT255_prosjekt/
├── data/
├── models/
├── notebooks/
├── outputs/
├── app.py
├── requirements.txt
└── README.md