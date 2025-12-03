import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os
from class_info import class_info
from googletrans import Translator

# Load the model once and cache it
@st.cache_resource
def load_model():
    model_path = "god_plant_disease_model_final.keras"
    if not os.path.exists(model_path):
        st.error("Model file not found. Please ensure 'plant_disease_cnn_model.h5' is in the app directory.")
        return None
    model = tf.keras.models.load_model(model_path)
    return model

# Class labels
class_names = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Potato___Early_blight',
    'Potato___Late_blight', 'Potato___healthy', 'Random', 'Tomato___Bacterial_spot',
    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus', 'Tomato___healthy', 'Unknown'
]

# Initialize the translator
translator = Translator()

# App UI
st.title("🌿GreenGuard Classifier")
st.write("Upload a leaf image and click **Analyze** to predict the disease.")

model = load_model()

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "JPG", "JPEG", "PNG"])

# Display image if uploaded
if uploaded_file:
    file_extension = os.path.splitext(uploaded_file.name)[1].lower()
    if file_extension not in [".jpg", ".jpeg", ".png"]:
        st.error("Invalid file extension. Please upload a file with .jpg, .jpeg, or .png extension.")
    else:
        # Proceed with processing the file
        st.write(f"Uploaded file name: {uploaded_file.name}")
        try:
            image = Image.open(uploaded_file).convert('RGB')
            st.image(image, caption='Uploaded Image', use_column_width=True)

            # Analyze button
            if st.button("Analyze"):
                st.write("Classifying...")

                # Preprocess image
                image_resized = image.resize((128, 128))
                img_array = tf.keras.preprocessing.image.img_to_array(image_resized)
                img_array = np.expand_dims(img_array, axis=0)

                # Prediction
                predictions = model.predict(img_array)
                print(predictions.shape)
                predicted_index = np.argmax(predictions[0])
                confidence = float(predictions[0][predicted_index])

                threshold = 0.6
                if confidence < threshold:
                    st.warning("⚠️ This image might not belong to any known class.")
                    st.info(f"**Prediction:** Unknown\n**Confidence:** {confidence:.2%}")
                    st.session_state.description = class_info['Unknown']['description']
                    st.session_state.treatment = class_info['Unknown']['treatment']
                else:
                    predicted_class = class_names[predicted_index]
                    st.success(f"**Prediction:** {predicted_class}")
                    st.info(f"**Confidence:** {confidence:.2%}")
                    st.session_state.description = class_info[predicted_class]['description']
                    st.session_state.treatment = class_info[predicted_class]['treatment']

        except Exception as e:
            st.error(f"Error processing image: {e}")

# Display prediction info if available
if 'description' in st.session_state and 'treatment' in st.session_state:
    st.write("### Description:")
    for line in st.session_state.description:
        st.write(f"- {line}")
    st.write("### Recommended Treatment:")
    for line in st.session_state.treatment:
        st.write(f"- {line}")

    # Translate button
    if st.button("Translate to Hindi"):
        translated_description = [
            translator.translate(line, src='en', dest='hi').text
            for line in st.session_state.description
        ]
        translated_treatment = [
            translator.translate(line, src='en', dest='hi').text
            for line in st.session_state.treatment
        ]

        st.write("### विवरण (Description in Hindi):")
        for line in translated_description:
            st.write(f"- {line}")
        st.write("### अनुशंसित उपचार (Recommended Treatment in Hindi):")
        for line in translated_treatment:
            st.write(f"- {line}")
