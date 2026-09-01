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

## 🎯 Main Objective

The main objectives of this project are:

1. Understand the original dataset before model training.
2. Identify missing values and understand their distribution.
3. Investigate duplicate records.
4. Detect and validate noisy or logically inconsistent data.
5. Validate BMI using height and weight.
6. Validate systolic and diastolic blood pressure values.
7. Compare different missing-value handling approaches.
8. Detect possible data leakage.
9. Understand how leakage can artificially improve model performance.
10. Build a clean Machine Learning model without leakage.
11. Evaluate the model using MAE, RMSE and R².
12. Deploy the model using a simple Streamlit interface.

---

## 🔬 Research Focus — Data Leakage

Why Data Leakage Matters:-

One of the most important findings of this project was **data leakage**.

Data leakage occurs when information that should not be available to the model during prediction is used as an input feature.

This can make the model appear highly accurate during testing, while the performance may not represent how the model would behave on genuinely unseen real-world data.



### Model Performance: Data Leakage Impact

| Model | Recommended_Calories | MAE | RMSE | R² |
|---|---|---:|---:|---:|
| Leakage Model | Included | 90.03 | 107.68 | 0.9734 |
| Clean Model | Removed | 580.67 | 667.32 | -0.0223 |
