import torch
import torch.nn as nn
import torchvision.models as models
import streamlit as st

# Your custom CNN architecture
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(3, 16, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.fc = nn.Linear(32*56*56, 14)

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)

#Load CNN
model_cnn = SimpleCNN()
model_cnn.load_state_dict(torch.load("models/best_model_cnn.pth"))
model_cnn.eval()

#Load ResNet18
model_resnet = models.resnet18()
model_resnet.load_state_dict(torch.load("models/best_model_resnet.pth"))
model_resnet.eval()

st.set_page_config(page_title="Keras Image Classifier", page_icon="🖼️")
st.title("Image classifier")
st.write("Upload an image or click an example.")
