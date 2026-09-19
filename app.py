import streamlit as st
import cv2
import numpy as np
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget
from pytorch_grad_cam.utils.image import show_cam_on_image
import google.generativeai as genai
import os
import urllib.request

# 1. Page Config
st.set_page_config(page_title="DR Screening System", layout="wide")

# --- HIDE STREAMLIT BRANDING ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            [data-testid="stToolbar"] {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# -------------------------------

st.title("Diabetic Retinopathy Multimodal Screening Suite")

# 2. Configure Google AI Studio Securely via Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
llm_model = genai.GenerativeModel("gemini-3.6-flash")

# 3. Model Downloader & Loader
@st.cache_resource
def load_model():
    weights_path = 'dr_resnet50_enhanced_weights.pth'
    
    # Auto-download weights from your GitHub release if not present
    if not os.path.exists(weights_path):
        with st.spinner("Downloading model weights from release..."):
            url = "https://github.com/yuvansh2025/netra.dr/releases/download/code/dr_resnet50_enhanced_weights.pth"
            urllib.request.urlretrieve(url, weights_path)
            
    device = torch.device('cpu') 
    model = models.resnet50(weights=None) 
    model.fc = nn.Sequential(
        nn.Linear(model.fc.in_features, 256),
        nn.ReLU(),
        nn.Dropout(0.4),
        nn.Linear(256, 5) 
    )
    model.load_state_dict(torch.load(weights_path, map_location=device))
    model = model.to(device)
    for param in model.layer4.parameters():
        param.requires_grad = True
    model.eval()
    return model, device

model, device = load_model()
class_names = ['0 - Normal', '1 - Mild', '2 - Moderate', '3 - Severe', '4 - Proliferative']

# 4. Preprocessing Function
def preprocess_image(img_array):
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 15, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        img_array = img_array[y:y+h, x:x+w]
        
    r, g, b = cv2.split(img_array)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    g_enhanced = clahe.apply(g)
    return Image.fromarray(cv2.merge((r, g_enhanced, b)))

# 5. UI Layout and Inference
uploaded_file = st.file_uploader("Upload Retinal Fundus Scan", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    img_array = np.array(image)
    
    with st.spinner("Analyzing scan and generating clinical report..."):
        pil_img = preprocess_image(img_array)
        
        data_transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        input_tensor = data_transform(pil_img).unsqueeze(0).to(device)
        
        with torch.no_grad():
            output = model(input_tensor)
            probabilities = torch.nn.functional.softmax(output[0], dim=0)
            predicted_class_idx = output.argmax(dim=1).item()
            predicted_class_name = class_names[predicted_class_idx]
            confidence_score = float(probabilities[predicted_class_idx]) * 100
            
        cam = GradCAM(model=model, target_layers=[model.layer4[-1]])
        targets = [ClassifierOutputTarget(predicted_class_idx)]
        input_tensor.requires_grad_(True)
        grayscale_cam = cam(input_tensor=input_tensor, targets=targets)[0, :]
        
        rgb_img = np.array(pil_img, dtype=np.float32) / 255.0
        rgb_img = cv2.resize(rgb_img, (224, 224)) 
        visualization = show_cam_on_image(rgb_img, grayscale_cam, use_rgb=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(visualization, caption="Grad-CAM Lesion Heatmap", use_container_width=True)
        with col2:
            st.markdown(f"### Predicted Severity: **{predicted_class_name}**")
            st.progress(int(confidence_score))
            st.write(f"**Confidence:** {confidence_score:.2f}%")
            
        # Call Gemini AI
        prompt = f"""
        You are an ophthalmology clinical assistant. A deep learning diagnostic model analyzed a retinal fundus scan:
        - Predicted Severity: {predicted_class_name}
        - Confidence: {confidence_score:.2f}%
        
        Provide a concise clinical report:
        1. Clinical Assessment: What this stage means pathologically.
        2. Visual Heatmap Interpretation: Explain that the highlighted areas indicate regions of vascular abnormality.
        3. Action Plan: Recommended clinical next steps.
        Keep it strictly factual, professional, and under 150 words.
        """
        try:
            response = llm_model.generate_content(prompt)
            st.success("Google AI Studio: Diagnostic Report Generated")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error communicating with Google AI Studio: {str(e)}")



import streamlit.components.v1 as components
import json

# Send result payload to parent NetraDR window
payload = json.dumps({
    "type": "NETRADR_SCAN_RESULT",
    "stage": predicted_class_idx,
    "confidence": round(confidence_score, 1),
    "stageName": predicted_class_name,
    "report": response.text if 'response' in locals() else ""
})

components.html(f"""
<script>
    window.parent.postMessage({payload}, "*");
</script>
""", height=0)
