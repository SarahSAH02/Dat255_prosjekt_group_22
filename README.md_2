# 🩺 Multi-Label Classification of Chest X-rays with Uncertainty Exploration

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=flat&logo=PyTorch&logoColor=white)](https://pytorch.org/)

Dette prosjektet utforsker bruk av dyplæring for automatisk diagnostisering av thorax-patologier fra røntgenbilder. Ved å kombinere moderne nevrale nettverk med metoder for forklarbarhet og usikkerhetsestimering, har vi utviklet et system som gir innsikt i AI-basert diagnostikk.

---

## 👥 Prosjektgruppe

- Astrid I. Bensnes  
- Mannat Gabria  
- Amna Zafar  
- Sarah S. Ahsan  

---

## 🌐 Webapplikasjon

For å demonstrere modellens praktiske anvendelse er det utviklet en interaktiv webapplikasjon ved hjelp av :contentReference[oaicite:0]{index=0}.

Applikasjonen lar brukeren:
- laste opp et bryst-røntgenbilde  
- motta prediksjoner for 14 sykdomsklasser  
- visualisere modellens fokusområder med Grad-CAM  

Den ferdig trente modellen (`.pth`) lastes inn ved oppstart og brukes til inferens i sanntid.

---

## 📊 Datasett og Metodikk

### Datakilde (Kaggle)

Vi har benyttet en kuratert versjon av **CheXpert**-datasettet fra Kaggle (`ashery/chexpert`). Dette ble valgt for å sikre enkel integrasjon og effektiv bildebehandling.

### Oppsplitting av data

For å sikre en valid evaluering ble datasettet splittet slik at ingen pasient-ID-er overlapper mellom settene:

- **Treningssett (80%)** – brukt til modelltrening  
- **Valideringssett (10%)** – brukt til tuning og terskeloptimalisering  
- **Testsett (10%)** – brukt for endelig evaluering  

---

## 🧠 Modellarkitektur

Vi har implementert og sammenlignet to tilnærminger:

1. **SimpleCNN (Baseline)**  
   - Egenutviklet modell  
   - Brukt til å utforske *Monte Carlo Dropout*  

2. **ResNet-18 (Hovedmodell)**  
   - Transfer learning fra ImageNet  
   - Multi-label klassifisering med `BCEWithLogitsLoss`  

---

## 📈 Resultater

Følgende resultater ble oppnådd med ResNet-18 etter 5 epoker:

| Metrikk | Verdi |
|--------|------|
| **Gjennomsnittlig AUC (14 klasser)** | **0.7683** |
| **Valideringstap (Loss)** | **0.2900** |
| **Beste F1-score** | **0.74 (Pleural Effusion)** |
| **Laveste F1-score** | **0.13 (Pneumonia)** |

### Analyse av ytelse

- **Pleural Effusion (0.74):** Sterk ytelse på tydelige radiologiske funn  
- **Pneumonia (0.13):** Vanskelig klasse grunnet diffuse mønstre og klasseubalanse  

---

## 🔍 Forklarbarhet og Pålitelighet

### Grad-CAM

Vi benytter Grad-CAM for å visualisere hvilke områder modellen fokuserer på. Dette gir innsikt i modellens beslutningsprosess og øker tilliten til resultatene.

| Pleural Effusion | Pneumonia |
|-----------------|----------|
| ![Pleural Effusion](Pleural%20effusion.png) | ![Pneumonia](phen.png) |

---

### Usikkerhetsestimering (MC Dropout)

Vi utforsket Monte Carlo Dropout for å estimere modellens usikkerhet. Dette reduserer risikoen for overkonfidente feilprediksjoner.

---

## 🛠 Installasjon og bruk

### 1. Klon repositoriet

```bash
git clone https://github.com/SarahSAH02/Dat255_prosjekt.git
cd Dat255_prosjekt
