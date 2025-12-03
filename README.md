# Plant-disease-detection


Here is a professional README.md file tailored to your project. You can copy the code block below and save it as README.md in your project folder.

Markdown
# 🌿 GreenGuard Classifier

**GreenGuard Classifier** is a deep learning-based web application designed to detect plant diseases from leaf images. Built with **Streamlit** and **TensorFlow**, this tool helps farmers and gardeners identify diseases in Apple, Corn, Potato, and Tomato plants and provides detailed treatment recommendations.

## 🚀 Features

* **Image Classification**: Upload leaf images (JPG, PNG) to detect diseases with high accuracy using a pre-trained CNN model.
* **Confidence Scoring**: Displays the model's confidence percentage for every prediction.
* [cite_start]**Detailed Insights**: Provides a description of the disease and recommended treatment steps for positive detections.
* [cite_start]**Multilingual Support**: Includes a translation feature to convert disease details and treatment plans from **English to Hindi** using the Google Translate API.
* **User-Friendly Interface**: Simple, interactive UI powered by Streamlit.

## 📋 Supported Plants & Diseases

[cite_start]The model is trained to identify the following classes:

* 🍎 **Apple**: Apple Scab, Black Rot, Cedar Apple Rust, Healthy.
* 🌽 **Corn (Maize)**: Cercospora (Gray) Leaf Spot, Common Rust, Northern Leaf Blight, Healthy.
* 🥔 **Potato**: Early Blight, Late Blight, Healthy.
* 🍅 **Tomato**: Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy.

## 🛠️ Tech Stack

* **Python 3.x**
* [cite_start]**Streamlit**: Web application framework[cite: 1, 2].
* [cite_start]**TensorFlow**: Deep learning backend for loading the Keras model[cite: 1, 2].
* [cite_start]**NumPy**: Array manipulation[cite: 1, 2].
* [cite_start]**Pillow (PIL)**: Image processing[cite: 1, 2].
* [cite_start]**GoogleTrans**: Translation services (specifically version `4.0.0-rc1`)[cite: 1, 2].

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-directory>
2. Create a Virtual Environment (Recommended)
Bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
3. Install Dependencies
Install the required packages using the provided requirements.txt:

Bash
pip install -r requirements.txt
4. Setup the Model
Ensure your trained model file is placed in the root directory.


Required Filename: god_plant_disease_model_final.keras 

Note: The application explicitly looks for god_plant_disease_model_final.keras. If your model is named differently, rename it or update the load_model function in app.py.

▶️ Running the Application
Run the Streamlit app with the following command:

Bash
streamlit run app.py
The app should open automatically in your browser at http://localhost:8501.

📂 Project Structure
├── app.py                      # Main Streamlit application entry point 
├── class_info.py               # Dictionary containing disease descriptions & treatments
├── requirements.txt            # Python dependencies 
├── god_plant_disease_model_final.keras  # Trained Model (Must be added manually)
└── README.md                   # Project documentation
⚠️ Disclaimer
The disease descriptions and treatment recommendations provided by this application are for illustrative purposes only. While based on agricultural data, results should be verified with agricultural experts or local agronomists before taking action.
