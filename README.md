# ❤️ Heart Stroke Prediction System

The **Heart Stroke Prediction System** is an end-to-end **Machine Learning–based web application** designed to predict the risk of heart stroke using key patient health indicators.  
This project demonstrates the complete ML workflow — from data preprocessing and model training to deployment through an interactive web interface using **Streamlit**.

The goal of this project is to make machine learning models **accessible, interpretable, and usable** for non-technical users while maintaining a clean and professional medical-style interface.

---

## 🎯 Project Objective
- To analyze patient health data and predict the likelihood of heart stroke.
- To build a real-time prediction system that accepts user inputs and returns instant results.
- To demonstrate practical deployment of a machine learning model as a web application.

---

## 🚀 Key Features
- Clean, responsive, and user-friendly medical UI built with Streamlit
- Heart stroke risk prediction using a trained **K-Nearest Neighbors (KNN)** model
- Real-time prediction with instant feedback
- Feature preprocessing using standard scaling
- Robust handling of categorical variables
- Clear visual distinction between high-risk and low-risk predictions

---

## 🧠 Machine Learning Approach
- **Algorithm Used:** K-Nearest Neighbors (KNN)
- **Problem Type:** Binary Classification
- **Preprocessing Techniques:**
  - Feature scaling using `StandardScaler`
  - One-hot encoding for categorical variables
- **Model Persistence:** Trained model, scaler, and feature columns saved using `joblib`

The model learns patterns from historical medical data and predicts whether a patient is at **high risk or low risk** of heart stroke.

---

## 📊 Input Parameters
The application uses the following patient health attributes:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure (mm Hg)
- Cholesterol Level (mg/dL)
- Fasting Blood Sugar
- Resting Electrocardiogram (ECG)
- Maximum Heart Rate
- Exercise-Induced Angina
- ST Depression (Oldpeak)
- ST Slope

These inputs are processed in real time and passed to the trained ML model for prediction.

---

## 🧰 Tech Stack
- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn  
- **Web Framework:** Streamlit  
- **Data Handling:** Pandas, NumPy  
- **Model Serialization:** Joblib  
## 🌐 Live Demo
👉https://heart-stroke-prediction-aowvknw6oynpccwgzezfeq.streamlit.app/

