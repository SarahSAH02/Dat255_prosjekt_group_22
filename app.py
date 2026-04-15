import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
import streamlit as st
from PIL import Image

LABELS = [
    "No Finding", "Enlarged Cardiomediastinum", "Cardiomegaly",
    "Lung Opacity", "Lung Lesion", "Edema", "Consolidation",
    "Pneumonia", "Atelectasis", "Pneumothorax", "Pleural Effusion",
    "Pleural Other", "Fracture", "Support Devices"
]

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

def get_resnet():
    model = models.resnet18()
    model.fc = nn.Linear(model.fc.in_features, 14)
    return model

@st.cache_resource
def load_models():
  cnn = SimpleCNN()
  cnn.load_state_dict(torch.load("models/best_model_cnn.pth", map_location=torch.device('cpu')))
  cnn.eval()

  resnet = get_resnet()
  resnet.load_state_dict(torch.load("models/best_model_resnet.pth", map_location=torch.device('cpu')))
  resnet.eval()

  return cnn, resnet

def preprocess(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)

def predict(model, tensor):
    with torch.no_grad():
      outputs = torch.sigmoid(model(tensor))
    return outputs.squeeze().numpy()
    
#Streamlit    
st.set_page_config(page_title="Disease detection for chest X-ray", layout="wide")
st.title("Disease detection for chest X-ray")
st.write("Upload a chest x-ray and get a diagnosis")

model_cnn, model_resnet = load_models()

model_choice = st.radio("Choose model:", ["CNN", "ResNet18", "Both"])
diagnose = st.button("Click to diagnose")
uploaded_file = st.file_uploader("Upload x-ray image", type=["jpg", "jpeg", "png"])

if uploaded_file and diagnose:
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open(uploaded_file).convert("RGB")
      st.image(image, caption="Uploaded x-ray", use_container_width=True)

    with col2:
      tensor = preprocess(image)
      st.subheader("Results")

      if model_choice in ["CNN", "Both"]:
        preds = predict(model_cnn, tensor)
        st.markdown("<p style='font-size:20px'><b>CNN Model:</b></p>", unsafe_allow_html=True)
        sorted_results = sorted(zip(LABELS, preds), key=lambda x: x[1], reverse=True)
        for label, score in sorted_results:
            st.markdown(f"<p style='font-size:17px'>- {label}: {score:.1%}</p>", unsafe_allow_html=True)

      if model_choice in ["ResNet18", "Both"]:
        preds = predict(model_resnet, tensor)
        st.markdown("<p style='font-size:20px'><b>ResNet18 Model:</b></p>", unsafe_allow_html=True)
        sorted_results = sorted(zip(LABELS, preds), key=lambda x: x[1], reverse=True)
        for label, score in sorted_results:
            st.markdown(f"<p style='font-size:17px'>- {label}: {score:.1%}</p>", unsafe_allow_html=True)