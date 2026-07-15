# ELLEVO-PATHWAYS-LOAN-PREDICTION-SYSTEM
# 🎓 Student Performance Factors Analysis

## 📌 Project Overview
This project performs a comprehensive data analysis and visualization of student performance factors using a dataset containing over **6,600 student records**. The analysis explores various academic, personal, and environmental factors that influence student exam scores, providing actionable insights for educators and policymakers.

---

## 📊 Dataset Description
The dataset `StudentPerformanceFactors.csv` contains **6,607 student records** with **20 features** covering:

### **Academic Factors**
- `Hours_Studied`: Weekly study hours (1–44 hours)
- `Attendance`: Attendance percentage (60–100%)
- `Previous_Scores`: Previous exam scores (50–100)
- `Tutoring_Sessions`: Number of tutoring sessions attended (0–8)
- `Exam_Score`: Target variable – final exam score (55–101)

### **Personal & Environmental Factors**
- `Parental_Involvement`: Level of parental engagement (Low/Medium/High)
- `Access_to_Resources`: Access to educational resources (Low/Medium/High)
- `Extracurricular_Activities`: Participation in extracurriculars (Yes/No)
- `Sleep_Hours`: Daily sleep hours (4–10 hours)
- `Motivation_Level`: Student motivation level (Low/Medium/High)
- `Internet_Access`: Internet availability (Yes/No)
- `Family_Income`: Family income level (Low/Medium/High)
- `Teacher_Quality`: Teacher quality rating (Low/Medium/High)
- `School_Type`: Type of school (Public/Private)
- `Peer_Influence`: Peer influence (Positive/Neutral/Negative)
- `Physical_Activity`: Weekly physical activity hours (0–6)
- `Learning_Disabilities`: Learning disability status (Yes/No)
- `Parental_Education_Level`: Parent education level (categorical)
- `Distance_from_Home`: Distance from school (Near/Moderate/Far)
- `Gender`: Student gender (Male/Female)

---

## 🧹 Methodology

### **Data Cleaning**
- **Missing Values Treatment**: Removed rows with missing values in key columns:
  - `Teacher_Quality` (78 missing)
  - `Parental_Education_Level` (90 missing)
  - `Distance_from_Home` (67 missing)
- **Final Dataset**: 6,378 clean records
- **Duplicate Removal**: Identified and removed **1 duplicate row**

---

## 📈 Summary Statistics

| Metric               | Value  |
|----------------------|--------|
| Mean Exam Score      | 67.24  |
| Mean Study Hours     | 19.98  |
| Mean Attendance      | 79.98% |
| Mean Previous Score  | 75.07  |
| Average Sleep        | 7.03   |
| Mean Tutoring Sessions | 1.49 |

---

## 🎨 Key Visualizations

### 1. Exam Score Distribution
- Histogram with KDE showing the distribution of exam scores:
  - Most scores cluster between **65–70**
  - Slight **right-skewed** distribution
  - KDE overlays smooth density estimation

### 2. Top 10 Study Hours
- Bar chart showing the most common study hours:
  - **20 hours/week** is the most frequent (448 students)
  - **19 hours/week** (425 students)
  - **21 hours/week** (420 students)
  - Students typically study **15–24 hours per week**

### 3. Motivation Level Distribution
- Pie chart breaking down student motivation:
  - Clear distribution across **Low / Medium / High** levels
  - Helps identify motivation patterns in the student population

### 4. Access to Resources
- Line chart showing the distribution of students by resource access level:
  - Visualizes educational resource inequality
  - Shows count of students at each resource level

---

## 🛠️ Technologies Used

| Library | Purpose |
|---------|---------|
| **Pandas** | Data manipulation and analysis |
| **Matplotlib** | Basic plotting and visualization |
| **Seaborn** | Statistical data visualization |
| **Jupyter Notebook** | Interactive development environment |

---

## 📁 Project Structure
