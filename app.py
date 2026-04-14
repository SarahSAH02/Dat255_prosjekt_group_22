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
model_cnn.load_state_dict(torch.load("models/best_model_cnn.pth", map_location=torch.device('cpu')))
model_cnn.eval()

#Load ResNet18
def get_resnet():
    model = models.resnet18()
    model.fc = nn.Linear(model.fc.in_features, 14)  # Change to 14 classes
    return model

model_resnet = get_resnet()
model_resnet.load_state_dict(torch.load("models/best_model_resnet.pth", map_location=torch.device('cpu')))
model_resnet.eval()

st.set_page_config(page_title="Disease detection in X-ray", page_icon="🖼️")
st.title("Disease detection for X-ray")
st.write("Upload an image")