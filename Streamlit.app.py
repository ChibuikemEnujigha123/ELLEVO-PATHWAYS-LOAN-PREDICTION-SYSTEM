

# ============================================
# LOAN APPROVAL PREDICTOR - STREAMLIT APP
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="💰",
    layout="wide"
)

# ============================================
# LOAD ARTIFACTS
# ============================================

@st.cache_resource
def load_artifacts():
    models = {
        'Random Forest': joblib.load("models/random_forest_model.pkl"),
        'Logistic Regression': joblib.load("models/logistic_model.pkl"),
        'SVM': joblib.load("models/svm_model.pkl")
    }
    scaler = joblib.load("models/scaler.pkl")
    label_encoder = joblib.load("models/label_encoder.pkl")
    feature_names = joblib.load("models/feature_names.pkl")
    edu_categories = joblib.load("models/education_categories.pkl")
    return models, scaler, label_encoder, feature_names, edu_categories

models, scaler, label_encoder, feature_names, edu_categories = load_artifacts()

# ============================================
# TITLE
# ============================================

st.title("💰 Loan Approval Predictor")
st.markdown("Predict whether a loan application will be **Approved** or **Rejected** based on applicant details.")

# ============================================
# SIDEBAR – MODEL SELECTION
# ============================================

st.sidebar.header("Choose Prediction Model")
selected_model_name = st.sidebar.selectbox(
    "Select Model",
    list(models.keys())
)
model = models[selected_model_name]

# ============================================
# INPUT SECTION
# ============================================

st.header("Enter Applicant Information")

# ---- Numeric inputs ----
col1, col2 = st.columns(2)

with col1:
    dependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        max_value=10,
        value=2,
        step=1,
        help="Number of dependents (0–10)"
    )
    income = st.number_input(
        "Annual Income (₦)",
        min_value=0,
        max_value=50_000_000,
        value=5_000_000,
        step=100_000,
        help="Annual income in Naira"
    )
    loan_amount = st.number_input(
        "Loan Amount (₦)",
        min_value=0,
        max_value=100_000_000,
        value=15_000_000,
        step=100_000,
        help="Requested loan amount"
    )
    loan_term = st.number_input(
        "Loan Term (months)",
        min_value=1,
        max_value=30,
        value=12,
        step=1,
        help="Loan repayment period in months"
    )

with col2:
    cibil = st.number_input(
        "CIBIL Score",
        min_value=300,
        max_value=900,
        value=600,
        step=1,
        help="Credit score (300–900)"
    )
    residential_assets = st.number_input(
        "Residential Assets Value (₦)",
        min_value=0,
        max_value=50_000_000,
        value=5_000_000,
        step=100_000
    )
    commercial_assets = st.number_input(
        "Commercial Assets Value (₦)",
        min_value=0,
        max_value=50_000_000,
        value=3_000_000,
        step=100_000
    )
    luxury_assets = st.number_input(
        "Luxury Assets Value (₦)",
        min_value=0,
        max_value=50_000_000,
        value=10_000_000,
        step=100_000
    )
    bank_assets = st.number_input(
        "Bank Assets Value (₦)",
        min_value=0,
        max_value=50_000_000,
        value=4_000_000,
        step=100_000
    )

# ---- Categorical input ----
education = st.selectbox(
    "Education Level",
    edu_categories,
    help="Select the applicant's education level"
)

# ============================================
# PREPROCESS INPUT
# ============================================

# Create a DataFrame with zeros for all 10 features
input_df = pd.DataFrame(0, index=[0], columns=feature_names)

# Fill numeric features (note: column names include leading spaces)
numeric_mapping = {
    ' no_of_dependents': dependents,
    ' income_annum': income,
    ' loan_amount': loan_amount,
    ' loan_term': loan_term,
    ' cibil_score': cibil,
    ' residential_assets_value': residential_assets,
    ' commercial_assets_value': commercial_assets,
    ' luxury_assets_value': luxury_assets,
    ' bank_asset_value': bank_assets
}
for col, val in numeric_mapping.items():
    if col in input_df.columns:
        input_df[col] = val

# One‑hot encode education (drop_first=True, baseline = 'Graduate')
# The dummy column is ' education_Not Graduate'
if education == 'Not Graduate':
    input_df[' education_Not Graduate'] = 1
# else 'Graduate' → remains 0

# ============================================
# PREDICTION
# ============================================

st.header("Prediction Result")

if st.button("Predict Loan Status", type="primary"):
    # Scale input
    scaled_input = scaler.transform(input_df)
    # Predict
    pred_encoded = model.predict(scaled_input)[0]
    pred_label = label_encoder.inverse_transform([pred_encoded])[0]
    
    # ----- Show result with green/red styling -----
    if pred_label == "Approved":
        st.success("✅ Loan Status: Approved")
    else:
        st.error("❌ Loan Status: Rejected")
    
    # ----- Show confidence (if available) -----
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(scaled_input)[0]
        st.write(f"**Confidence:** Approved {proba[1]*100:.1f}% / Rejected {proba[0]*100:.1f}%")
    
    # ----- Show encoded input data for verification -----
    with st.expander("Show input data (after encoding)"):
        st.dataframe(input_df)

# ============================================
# FOOTER
# ============================================

st.caption("Model and preprocessing artifacts loaded from the 'models/' folder.")