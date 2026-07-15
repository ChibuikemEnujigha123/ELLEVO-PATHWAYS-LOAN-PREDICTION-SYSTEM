# ELLEVO-PATHWAYS-LOAN-PREDICTION-SYSTEM


## 📌 Project Overview
This project builds a **machine learning-based Loan Approval Prediction System** that determines whether a loan application should be **Approved** or **Rejected** based on applicant financial and personal information. The system uses three different classification models and provides a user-friendly Streamlit interface for real-time predictions.

---

## 📊 Dataset Description
The dataset `loan_approval_dataset.csv` contains **4,269 loan records** with **13 features**:

### **Applicant Demographics**
- `loan_id`: Unique identifier for each loan application
- `no_of_dependents`: Number of dependents (0–5)
- `education`: Education level (`Graduate` / `Not Graduate`)
- `self_employed`: Self-employment status (`Yes` / `No`)

### **Financial Information**
- `income_annum`: Annual income in Naira (₦)
- `loan_amount`: Requested loan amount in Naira (₦)
- `loan_term`: Loan repayment period (2–20 months)
- `cibil_score`: Credit score (300–900)

### **Asset Values**
- `residential_assets_value`: Residential assets value (₦)
- `commercial_assets_value`: Commercial assets value (₦)
- `luxury_assets_value`: Luxury assets value (₦)
- `bank_asset_value`: Bank assets value (₦)

### **Target Variable**
- `loan_status`: Loan approval status (`Approved` / `Rejected`)

---

## 🧹 Methodology

### **Data Cleaning**
- **Missing Values**: No missing values found in the dataset
- **Duplicate Removal**: Identified and removed **1 duplicate** row
- **Outlier Detection**: Used IQR method to identify outliers in asset columns:
  - `residential_assets_value`: 52 outliers removed
  - `commercial_assets_value`: 37 outliers removed
  - `bank_asset_value`: 5 outliers removed
- **Feature Engineering**: Dropped unnecessary columns (`loan_id`, `self_employed`)
- **Final Dataset Shape**: 4,264 rows × 11 columns

### **Data Preprocessing**
1. **Encoding**: One-hot encoded `education` feature
2. **Label Encoding**: Converted target variable `loan_status` to numerical values
3. **Feature Scaling**: Standardized features using `StandardScaler`
4. **Train-Test Split**: 70% training, 30% testing (stratified split)

---

## 📈 Summary Statistics

| Metric | Value |
|--------|-------|
| **Mean Dependents** | 2.50 |
| **Mean Annual Income** | ₦5.05M |
| **Mean Loan Amount** | ₦15.12M |
| **Mean Loan Term** | 10.9 months |
| **Mean CIBIL Score** | 600.09 |
| **Mean Residential Assets** | ₦7.46M |
| **Mean Commercial Assets** | ₦4.97M |
| **Mean Luxury Assets** | ₦15.11M |
| **Mean Bank Assets** | ₦4.97M |

---

## 🤖 Models Implemented

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| **Logistic Regression** | 93% | 0.91–0.94 | 0.90–0.94 | 0.90–0.94 |
| **SVM (Linear)** | 94% | 0.91–0.95 | 0.93–0.94 | 0.92–0.95 |
| **Random Forest** | **98%** | 0.99–1.00 | 0.96–0.99 | 0.98–0.99 |

### **Best Model: Random Forest**
- **Confusion Matrix**: [[792, 5], [18, 465]]
- **Key Parameters**: `n_estimators=500`, `random_state=42`
- **Performance**: Excellent classification with minimal misclassifications

---

## 🎨 Key Visualizations

### 1. Loan Amount Distribution
- Histogram with KDE showing loan amount distribution
- Most loan amounts cluster between ₦5M–₦25M
- Right-skewed distribution

### 2. Loan Status Distribution
- Count of Approved vs Rejected applications
- Shows class balance in the dataset

### 3. Loan Amount by Status
- Bar chart comparing average loan amounts for Approved vs Rejected applications
- Insights into approval patterns based on loan size

---

## 🛠️ Technologies Used

| Library | Purpose |
|---------|---------|
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computing |
| **Matplotlib** | Basic plotting and visualization |
| **Seaborn** | Statistical data visualization |
| **Scikit-learn** | Machine learning models and preprocessing |
| **Joblib** | Model serialization and export |
| **Streamlit** | Web application interface |
| **Jupyter Notebook** | Interactive development environment |

---
