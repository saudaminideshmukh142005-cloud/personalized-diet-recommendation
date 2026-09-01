# 🥗 Personalized Diet Recommendation System

A Machine Learning based system for predicting a person's daily caloric intake using personal, body, health, lifestyle and dietary information.

This project focuses not only on building a Machine Learning model, but also on understanding how **data quality, preprocessing decisions and data leakage affect the complete dataset and model performance**.

---

## 📌 About Project

The objective of this project is to predict:

> **Target Variable: `Caloric_Intake`**

The model uses information such as:

- Age
- Gender
- Height
- Weight
- BMI
- Blood Pressure
- Cholesterol
- Blood Sugar
- Lifestyle habits
- Exercise frequency
- Sleep hours
- Dietary habits
- Protein, carbohydrate and fat intake
- Dietary preferences
- Health-related information

The project was developed as a research-oriented Machine Learning study where the main goal was to understand **why a model performs well or poorly**, rather than focusing only on achieving high accuracy.

---

# 🎯 Main Objective

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

# 🔬 Research Focus — Data Leakage

## 🚨 Why Data Leakage Matters

One of the most important findings of this project was **data leakage**.

Data leakage occurs when information that should not be available to the model during prediction is used as an input feature.

This can make the model appear highly accurate during testing, while the performance may not represent how the model would behave on genuinely unseen real-world data.

### Example

The dataset contained a feature:

```text
Recommended_Calories
