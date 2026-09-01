# 🥗 NutriCare — Personalized Caloric Intake Prediction

A machine learning project that predicts a user's daily caloric intake while focusing on **data quality, preprocessing, noisy data validation, and data leakage detection**.

This project is not only about achieving high prediction accuracy.  
The main objective is to understand **how data quality and feature selection affect machine learning model performance**.

---

## 📌 About the Project

NutriCare predicts daily caloric intake (`Caloric_Intake`) using personal, health, lifestyle and dietary features.

The major focus of this project is to investigate:

- Missing values
- Duplicate records
- Noisy and inconsistent data
- BMI validation
- Blood pressure validation
- Different missing-value handling strategies
- Data leakage
- Effect of leakage on model performance
- Train/test evaluation
- Realistic model performance after removing leakage

---

## 🎯 Project Objective

The project follows a research-oriented approach rather than simply training a model and reporting accuracy.

The main question investigated is:

> **Does better preprocessing always mean better machine learning performance, or can hidden data leakage make a model appear artificially accurate?**

---

## 🔬 Project Workflow

text
Original Dataset
       ↓
Data Understanding
       ↓
Missing Value Analysis
       ↓
Duplicate Analysis
       ↓
Noisy Data Validation
       ├── BMI Validation
       └── Blood Pressure Validation
       ↓
Preprocessing Experiments
       ├── Drop Rows
       ├── Mode Imputation
       └── Unknown Category
       ↓
Data Leakage Detection
       ├── Recommended_Calories
       └── Calorie Difference
       ↓
Clean Dataset
       ↓
Train / Test Split
       ↓
Preprocessing Pipeline
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Streamlit Prediction UI

'''
## 📊 Dataset

The dataset contains 5000 records.

The target variable selected for this project is:

Caloric_Intake
Target Summary
Statistic	Value
Count	5000
Mean	2347.35
Standard Deviation	659.88
Minimum	1200
Median	2350.50
Maximum	3499

Caloric_Intake is a continuous numerical variable, therefore this is treated as a regression problem.
