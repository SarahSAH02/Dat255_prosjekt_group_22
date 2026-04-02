# DAT255 – Reliable Multi-Label Chest X-ray Classification

Deep learning for medical image analysis with uncertainty estimation and explainability.

## 👥 Team
- Astrid I. Bensnes  
- Mannat Gabria  
- Amna Zafar  
- Sarah S. Ahsan  

---

## 📌 Project Overview

This project investigates multi-label classification of chest X-ray images using deep learning.  
Unlike traditional single-class classification, a chest X-ray may contain multiple co-existing pathologies.  

Our goal is not only to achieve high predictive performance, but to develop a **reliable and transparent medical AI system** by integrating:

- ✅ High-performance CNN architectures  
- ✅ Predictive uncertainty estimation  
- ✅ Visual explainability methods  


---

## 📊 Dataset

We use the **CheXpert dataset** from Stanford ML Group:

https://stanfordmlgroup.github.io/competitions/chexpert

CheXpert is a large-scale dataset of labeled chest X-rays containing multiple thoracic pathologies.

⚠️ The dataset is **not included** in this repository due to licensing restrictions.

---

## 🧠 Models

### 1️⃣ ResNet (Baseline)
A standard convolutional neural network architecture used as our baseline model.

### 2️⃣ EfficientNet
A more advanced architecture designed for improved performance and parameter efficiency.

We compare models using:
- ROC-AUC (per label)
- Macro and Micro F1-score
- Precision / Recall

---

## 📈 Uncertainty Estimation – MC Dropout

To improve model reliability in a medical context, we apply **Monte Carlo Dropout** during inference.

This allows us to:
- Estimate predictive uncertainty
- Analyze the relationship between uncertainty and misclassification
- Investigate model calibration

Uncertainty is critical in medical AI to avoid overconfident incorrect predictions.

---

## 🔥 Explainability – Grad-CAM

We use **Grad-CAM** to generate heatmaps that highlight image regions contributing to model predictions.

This enables:
- Visual interpretation of decisions
- Failure case analysis
- Detection of shortcut learning or spurious correlations

---

