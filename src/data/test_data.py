import os
import pandas as pd
from PIL import Image

ROOT = "data/chexpert/CheXpert-v1.0 batch 1 (validate & csv)"
CSV_PATH = os.path.join(ROOT, "valid.csv")

df = pd.read_csv(CSV_PATH)
print("Rows:", len(df))
print("Columns:", df.columns.tolist())

row = df.iloc[0]
img_rel = row["Path"]
img_path = os.path.join(ROOT, img_rel.split("CheXpert-v1.0/")[1])

print("First image path:", img_path)
print("Exists?", os.path.exists(img_path))

img = Image.open(img_path).convert("RGB")
print("Image size:", img.size)