# Multi-Label Classification of Chest X-rays with Uncertainty Exploration

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=flat&logo=PyTorch&logoColor=white)](https://pytorch.org/)

Dette prosjektet utforsker bruken av dyplæring for automatisert diagnostisering av thorax-patologier fra røntgenbilder. Ved å kombinere moderne nevrale nettverk (ResNet-18) med metoder for usikkerhetsestimering og visuell forklarbarhet, har vi utviklet et system som gir dypere innsikt i AI-basert diagnostikk.

## 👥 Prosjektgruppe

- Astrid I. Bensnes
- Mannat Gabria
- Amna Zafar
- Sarah S. Ahsan

---

## 📊 Datasett og Metodikk

### Datakilde (Kaggle)

Vi har benyttet en kuratert versjon av **CheXpert**-datasettet fra **Kaggle** (`ashery/chexpert`). Dette ble valgt for å sikre sømløs integrasjon med Google Colab og for å utnytte en optimalisert filstruktur for bildebehandling.

### Oppsplitting av data

For å sikre en valid evaluering ble datasettet splittet slik at ingen pasient-ID-er overlapper mellom settene:

- **Treningssett (80%):** Brukt til modelltrening og vektoppdatering.
- **Valideringssett (10%):** Brukt til hyperparameter-tuning og terskel-optimalisering.
- **Testsett (10%):** Brukt for den endelige, objektive evalueringen.

---

## 🧠 Modellarkitektur

Vi har implementert og sammenlignet to ulike tilnærminger:

1.  **SimpleCNN (Baseline):** En egenutviklet arkitektur med to konvolusjonelle lag. Denne fungerer som et sammenligningsgrunnlag og ble brukt til å utforske **Monte Carlo Dropout** for usikkerhetsestimering.
2.  **ResNet-18 (Hovedmodell):** Et dypt rest-nettverk som utnytter **Transfer Learning** fra ImageNet. Denne modellen håndterer multi-label klassifiseringen ved bruk av `BCEWithLogitsLoss`.

---

## 📈 Resultater

Følgende resultater ble oppnådd med vår optimaliserte ResNet-18 modell etter 5 epoker:

| Metrikk                                          | Verdi      |
| :----------------------------------------------- | :--------- |
| **Gjennomsnittlig AUC (14 klasser)**             | **0.7683** |
| **Siste Valideringstap (Loss)**                  | **0.2900** |
| **Beste medisinske F1-score (Pleural Effusion)** | **0.74**   |
| **Laveste F1-score (Pneumonia)**                 | **0.13**   |

### Analyse av ytelse

- **Pleural Effusion (0.74):** Modellen presterer sterkt på klasser med tydelige radiologiske tegn (væskeansamling).
- **Pneumonia (0.13):** Lungebetennelse viste seg å være mest utfordrende grunnet diffuse visuelle grenser og klasseubalanse. .

---

## 🔍 Forklarbarhet og Pålitelighet

### Grad-CAM Visualisering

Vi benytter **Grad-CAM (Gradient-weighted Class Activation Mapping)** for å generere varmekart. Dette gjør det mulig å verifisere at modellen fokuserer på de anatomisk korrekte områdene i lungene, noe som er essensielt for medisinsk tillit.

Varmekartene bekrefter at modellen har lært å lokalisere patologier i lungefeltene, i stedet for å basere seg på bakgrunnsstøy eller artefakter.

|                             Pleural Effusion (Væske i lungene)                             |                          Pneumonia (Lungebetennelse)                          |
| :----------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------: |
|                        ![Pleural Effusion](Pleural%20effusion.png)                         |                            ![Pneumonia](phen.png)                             |
| _Modellen fokuserer korrekt på væskeansamling nederst i lungeposen (kostofrenisk vinkel)._ | _Varmekartet lokaliserer et fortettet område (infiltrat) i midtre lungefelt._ |

---

### Usikkerhetsestimering (MC Dropout)

For å unngå "overconfident" feilprediksjoner, utforsket vi **Monte Carlo Dropout** på baseline-modellen. Ved å beholde dropout aktiv under prediksjon, kan vi beregne et standardavvik som indikerer hvor usikker modellen er på diagnosen den stiller.

---

## 🛠 Installasjon og Bruk

1. **Klon repositoriet:**

   ```bash
   git clone [https://github.com/brukernavn/DAT255-Chest-Xray.git](https://github.com/brukernavn/DAT255-Chest-Xray.git)

   ```

2. **Kjør kommandoen i terminalen:**

   ```bash
   python3.11 -m pip install -r requirements.txt

   ```

3. **Kjøre kommandoen i terminalen for å få opp websiden:**

   ```bash
   streamlit run app.py

   ```
