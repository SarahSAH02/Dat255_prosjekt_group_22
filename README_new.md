# 🫁 Multi-label sykdomsdeteksjon i brystrøntgenbilder

Dette prosjektet er utviklet som en del av **DAT255 – Deep Learning Engineering** ved HVL.

Målet med prosjektet er å utvikle og evaluere dyp læringsmodeller for **multi-label klassifikasjon av brystrøntgenbilder**, basert på **CheXpert-datasettet**. Systemet predikerer flere patologier fra ett enkelt bilde, og utforsker hvordan modellvalg, terskeloptimalisering og forklarbarhet påvirker ytelsen.

---

## 👥 Prosjektgruppe

- Astrid I. Bensnes  
- Mannat Gabria  
- Amna Zafar  
- Sarah S. Ahsan  

---

## 📌 Problemstilling

Prosjektet undersøker følgende:

Hvordan påvirker modellarkitekturens kompleksitet klassifisering av patologier i brystrøntgenbilder sammenlignet med en enklere egenutviklet modell, og hvordan kan terskel optimalisering bidra til mer robuste prediksjoner i et ubalansert datasett?

Modellen predikerer totalt **14 patologiklasser** fra brystrøntgenbilder.

---

## 📊 Datasett

Vi benytter en kuratert versjon av **CheXpert**-datasettet (`ashery/chexpert` fra Kaggle).

### Egenskaper

- Multi-label datasett (14 klasser)
- Inneholder usikre annotasjoner (-1)
- Betydelig klasseubalanse

### Databehandling

- Usikre verdier (-1) og manglende verdier behandles som **negative (0)**
- Datasplitting (på pasient-ID for å unngå data leakage):
  - Treningssett: ~80%
  - Valideringssett: ~10%
  - Testsett: ~10%

---

## ⚙️ Metode

### Modeller

Vi har implementert og sammenlignet følgende modeller:

- **Baseline CNN** (egenutviklet modell)
- **ResNet18** (transfer learning)
- **DenseNet121** (transfer learning)
- **EfficientNet-B0** (transfer learning)

Alle modellene er tilpasset en **multi-label klassifikasjonsoppgave**.

---

### Treningsoppsett

- Tapsfunksjon: `BCEWithLogitsLoss`
- Optimalisering: **AdamW**
- Læringsrate: `1e-4`
- Weight decay: `1e-4`
- Inputstørrelse: `224x224`

### Datapreprosessering

- Resize til 224×224
- Normalisering (ImageNet)
- Konvertering til tensor

### Dataaugmentering (kun trening)

- Random crop
- Horisontal speiling
- Rotasjon

---

## 📈 Resultater

| Modell           | Mean AUC | Macro F1 |
|------------------|---------|----------|
| Baseline CNN     | 0.6668  | 0.2790   |
| ResNet18         | 0.7752  | 0.3926   |
| DenseNet121      | ~0.78   | **0.4100** |
| EfficientNet-B0  | **0.7889** | ~0.40 |

### Viktige observasjoner

- Transfer learning gir betydelig bedre ytelse enn baseline-modellen
- EfficientNet-B0 og DenseNet121 presterer best totalt
- Enkelte klasser (f.eks. Pneumonia) er vanskelig å klassifisere
- **Terskeloptimalisering** forbedrer balansen mellom presisjon og recall

---

## 🔍 Forklarbarhet

Vi benytter **Grad-CAM** for å visualisere modellens beslutninger.

- Viser hvilke områder i bildet modellen fokuserer på
- Bidrar til økt transparens
- Gir innsikt i om modellen baserer seg på relevante anatomiske strukturer

---

## 🌐 Webapplikasjon (Deployment)

Modellen er deployet som en interaktiv webapplikasjon ved hjelp av **Streamlit**.

### Funksjonalitet

- Last opp brystrøntgenbilde
- Få prediksjoner for 14 patologiklasser
- Se sannsynligheter per klasse
- Visualiser modellens fokus med Grad-CAM

### Teknisk løsning

- Modellen lagres som `.pth`-fil
- Lastes inn ved oppstart av applikasjonen
- Input preprocesseres likt som under trening
- Prediksjoner genereres i sanntid

---

## 📸 Demo


```markdown
![Web App Demo](outputs/demo.png)
