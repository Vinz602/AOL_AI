import streamlit as st
from PIL import Image
import pandas as pd
from predict import predict_one, class_names

st.title("AI AOL X-ray image dissease classification Fixed")
st.write(f"Upload an image, I’ll classify it as either {class_names}")

uploaded_file = st.file_uploader("Upload here (one image only)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded!", use_column_width=True)

    if st.button("Predict"):
        with st.spinner("Loading, sabar ya"):
            pred_class, confidence, probs = predict_one(img)

        st.subheader("Prediction result")
        st.write(f"Predicted class: {pred_class}")
        st.write(f"Confidence: {confidence * 100:.2f}%")

        st.subheader("Saran :")

        if(pred_class == "Viral Pneumonia"):
            st.write("Istirahat yang cukup dan minum banyak cairan.")
            st.write("Gunakan obat pereda nyeri dan demam seperti parasetamol atau ibuprofen \nuntuk mengurangi gejala.")
            st.write("Hindari merokok dan paparan asap rokok. Jika gejala memburuk atau tidak membaik dalam beberapa hari, segera konsultasikan dengan dokter.\n")
        elif(pred_class == "Corona Virus Disease"):
            st.write("Isolasi mandiri dan segera hubungi fasilitas kesehatan terdekat.")
            st.write("Gunakan masker saat berada di sekitar orang lain dan jaga jarak minimal 1 meter.")
            st.write("Cuci tangan secara rutin dengan sabun dan air mengalir atau gunakan hand sanitizer.")
            st.write("Hindari menyentuh wajah, terutama mata, hidung, dan mulut.\n")
        elif(pred_class == "Bacterial Pneumonia"):
            st.write("WAJIB evaluasi medis segera untuk mendapatkan antibiotik yang sesuai.\n")
            st.write("Istirahat yang cukup dan minum banyak cairan.")
        elif(pred_class == "Tuberculosis"):
            st.write("Segera konsultasikan dengan dokter untuk mendapatkan pengobatan yang tepat.\n")
            st.write("Minum obat sesuai dengan anjuran dokter dan selesaikan seluruh masa pengobatan.")
            st.write("Kontrol rutin ke fasilitas kesehatan untuk memantau perkembangan kondisi.\n")
        elif(pred_class == "Normal"):
            st.write("Sehat-sehat terus ya! Jaga pola hidup sehat dan rutin cek kesehatan.")

# class_names = [
#     "Bacterial Pneumonia",
#     "Corona Virus Disease",
#     "Normal",
#     "Tuberculosis",
#     "Viral Pneumonia"
# ]