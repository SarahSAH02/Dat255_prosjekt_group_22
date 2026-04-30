# CheXpert Dataset

Dette prosjektet benytter **CheXpert-v1.0-small**, en nedskalert versjon hentet fra kaggle. Det originale datasettet er utviklet av Stanford Machine Learning Group. Datasettet består av brystrøntgenbilder med tilhørende annotasjoner for ulike patologiske tilstander.

## 📊 Innhold
- Totalt antall bilder: ~224 000 (originalt datasett)  
- Antall pasienter: ~65 000  
- Antall klasser: 14 patologiske observasjoner  

### Dataformat
- Bilder lagret som JPG-filer  
- Annotasjoner lagret i CSV-filer  

## 🏷️ Labels
Hver observasjon er kodet som:
- `1` → Tilstedeværelse av sykdom  
- `0` → Fravær av sykdom  
- `-1` → Usikker annotasjon  
- `NaN` → Manglende verdi  

I dette prosjektet er både `-1` og `NaN` behandlet som `0` for å forenkle klassifikasjonsoppgaven.

## 📂 Datastruktur
Datasettet er organisert via CSV-filer, hvor hver rad inneholder:
- Filsti til bilde  
- Pasientinformasjon (ID, kjønn, alder)  
- 14 label-kolonner  
