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


Recommended_Calories


🧪 Leakage Experiment

To understand the effect of leakage, two experiments were performed.

Model 1 — With Leakage

Recommended_Calories was included as a feature.

Performance
MAE  : 90.03
RMSE : 107.68
R²   : 0.9734

The performance looked extremely good.

However, this result was not considered reliable because the model had access to a potentially target-derived feature.

Model 2 — Clean Model

Recommended_Calories was removed before training.

Performance
MAE  : 580.67
RMSE : 667.32
R²   : -0.0223

This was a major performance drop.

What does this show?

It demonstrates that:

High model performance does not always mean a good model.

A model can achieve an excellent R² score because of leakage rather than because it has genuinely learned useful relationships from independent input features.

This was one of the main learning outcomes of the project.

📊 Leakage vs Clean Model
Model	Recommended_Calories	MAE	RMSE	R²
Leakage Model	Included	90.03	107.68	0.9734
Clean Model	Removed	580.67	667.32	-0.0223
Interpretation

The leakage model appears significantly better.

However:

R² = 0.9734

should not automatically be considered a success because the model may be benefiting from leaked information.

After removing the suspected leakage feature:

R² = -0.0223

This indicates that the remaining features in the current dataset do not provide enough predictive information for the selected model to reliably predict Caloric_Intake.

This result is valuable because it exposes a limitation in the dataset instead of hiding it behind artificially high accuracy.
