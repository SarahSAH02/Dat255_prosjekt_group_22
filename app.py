import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
import streamlit as st
from PIL import Image
import numpy as np
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget

LABELS = [
    "No Finding", "Enlarged Cardiomediastinum", "Cardiomegaly",
    "Lung Opacity", "Lung Lesion", "Edema", "Consolidation",
    "Pneumonia", "Atelectasis", "Pneumothorax", "Pleural Effusion",
    "Pleural Other", "Fracture", "Support Devices"
]

def get_efficientnet():
    model = models.efficientnet_b0(weights=None)
    model.classifier[1] = nn.Linear(model.classifier[1].in_features, 14)
    return model

@st.cache_resource
def load_model():
    efficientnet = get_efficientnet()
    efficientnet.load_state_dict(torch.load("models/efficientnet.pth", map_location=torch.device('cpu')))
    efficientnet.eval()

    return efficientnet

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

def get_gradcam(model, tensor, raw_image, target_class=0):
    target_layers = [model.features[-1]]

    cam = GradCAM(model=model, target_layers=target_layers)
    targets = [ClassifierOutputTarget(target_class)]
    grayscale_cam = cam(input_tensor=tensor, targets=targets)[0]

    raw = np.array(raw_image.resize((224, 224))).astype(np.float32) / 255.0
    visualization = show_cam_on_image(raw, grayscale_cam, use_rgb=True)
    return Image.fromarray(visualization)

#Streamlit
st.set_page_config(page_title="Disease Detection for Chest X-ray", layout="wide")
st.title("Disease Detection for Chest X-ray")
st.write("Upload a chest x-ray and get a diagnosis")

model_efficientnet = load_model()

diagnose = st.button("Click to diagnose")
uploaded_file = st.file_uploader("Upload x-ray image", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file and diagnose:
    image = Image.open(uploaded_file).convert("RGB")
    tensor = preprocess(image)

    preds_efficientnet = predict(model_efficientnet, tensor)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Uploaded X-ray")
        st.image(image, caption="Uploaded x-ray", width='stretch')

    with col2:
        top_class = int(np.argmax(preds_efficientnet))
        gradcam_image = get_gradcam(model_efficientnet, tensor, image, target_class=top_class)
        st.subheader("Grad-CAM Heatmap")
        st.image(gradcam_image, caption=f"Focus area for: {LABELS[top_class]}", width='stretch')
        
    with col3:  
        st.subheader("Results")
        sorted_results = sorted(zip(LABELS, preds_efficientnet), key=lambda x: x[1], reverse=True)
        for i, (label, score) in enumerate(sorted_results):
            if i == 0:
                st.markdown(f"<p style='font-size:18px; background-color:#acd8a7; padding:8px; border-radius:5px;'><b> {label.upper()}: {score:.1%}</b></p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p style='font-size:18px'>- {label}: {score:.1%}</p>", unsafe_allow_html=True)