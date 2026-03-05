import os
import pandas as pd
import torch
from torch.utils.data import Dataset
from PIL import Image

class CheXpertData(Dataset):

    def __init__(self, root_dir, csv_file, transform=None):
        self.root_dir = root_dir
        self.df = pd.read_csv(csv_file)
        self.transform = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):

        row = self.df.iloc[idx]
        img_rel_path = row["Path"]

        img_path = os.path.join(
            self.root_dir,
            img_rel_path.split("CheXpert-v1.0/")[1]
        )

        image = Image.open(img_path).convert("RGB")

        labels = row.iloc[5:].values.astype("float32")
        labels = torch.tensor(labels)

        if self.transform:
            image = self.transform(image)

        return image, labels