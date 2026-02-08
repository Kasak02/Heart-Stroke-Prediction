import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Heart Stroke Prediction",
    page_icon="❤️",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("KNN_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style='text-align:center; color:#C0392B;'> Heart Stroke Prediction System</h1>
    <p style='text-align:center; font-size:18px;'>
    Enter patient details to assess the risk of heart stroke 
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------------- LAYOUT ----------------
col1, col2 = st.columns(2)

# ---------------- PERSONAL DETAILS ----------------
with col1:
    st.subheader("🧍 Personal Information")
    age = st.slider("Age", 18, 100, 40)
    sex = st.selectbox("Sex", ["M", "F"])
    chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])

# ---------------- MEDICAL DETAILS ----------------
with col2:
    st.subheader("🩺 Medical Measurements")
    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
    max_hr = st.slider("Max Heart Rate", 60, 220, 150)
    oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)

# ---------------- ADVANCED DETAILS ----------------
with st.expander("📊 ECG & Exercise Details"):
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# ---------------- PREDICT BUTTON ----------------
st.markdown("<br>", unsafe_allow_html=True)
predict_btn = st.button("🔍 Predict Heart Stroke Risk")

# ---------------- PREDICTION ----------------
if predict_btn:

    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    # Fill missing columns
    for col in columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[columns]

    # Scale
    scaled_input = scaler.transform(input_df)

    # Predict
    prediction = model.predict(scaled_input)[0]

    st.markdown("<hr>", unsafe_allow_html=True)

    # ---------------- RESULT ----------------
    if prediction == 1:
        st.error("⚠️ **High Risk of Heart Stroke Detected**")
    else:
        st.success("✅ **Low Risk of Heart Stroke Detected**")

    # ---------------- DISCLAIMER ----------------
    st.markdown(
    """
    <div style='background-color:#FFF3CD;
                color:#856404;
                padding:15px;
                border-radius:10px;
                border:1px solid #FFEEBA;'>
    <b>⚠️ Disclaimer:</b> This prediction is generated using a machine learning model
    and should not be considered a substitute for professional medical advice.
    </div>
    """,
    unsafe_allow_html=True
)

