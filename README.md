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
## 📊 Dataset

The dataset contains **5,000 records**.

The target variable selected for this project is **`Caloric_Intake`**.

### 🎯 Target Summary

| Statistic          |    Value |
| ------------------ | -------: |
| Count              |    5,000 |
| Mean               | 2,347.35 |
| Standard Deviation |   659.88 |
| Minimum            |    1,200 |
| Median             | 2,350.50 |
| Maximum            |    3,499 |

---
##  🧹 Data Quality & Preprocessing

Data preprocessing focused on making **evidence-based decisions** rather than simply removing duplicates and missing values.

### Missing Value Analysis

The dataset contained missing values in three categorical features:

| Feature         | Missing Values |
| --------------- | -------------: |
| Chronic_Disease |          2,043 |
| Allergies       |          3,497 |
| Food_Aversions  |          1,225 |

Three strategies were considered:

* **Row Removal:** Causes substantial data loss when multiple features contain missing values.
* **Mode Imputation:** Preserves records but may reduce variation and introduce majority-class bias.
* **Unknown Category:** Preserves records while retaining information that the value was missing.

Key takeaway: Missing-value handling was treated as a modeling decision because it can affect the training data, feature distributions, model performance, and generalization.
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

---



## 🧠 What I Learned

This project taught me that **Machine Learning is not just about choosing an algorithm and achieving a high evaluation score.** Reliable ML depends heavily on understanding the data, validating assumptions, and making scientifically justified preprocessing decisions.

The most important lessons from this project were:

### 1. Missing Values Are a Data Problem, Not Just a Cleaning Problem

Missing values should not automatically be removed or replaced.

The appropriate strategy depends on:

* Percentage of missing data
* Feature type
* Meaning of the missingness
* Information loss
* Impact on model behavior

**Key concept:**

> Missing-value treatment should preserve useful information while minimizing bias and unnecessary data loss.

---

### 2. Duplicate Detection Requires Context

A duplicate is not always simply a row that looks similar to another row.

It is important to distinguish between:

* **Exact duplicates** — identical records
* **Similar records** — different observations that may legitimately share similar values

Removing valid similar observations can reduce the diversity of the dataset and introduce unintended bias.

**Key concept:**

> Data cleaning should remove redundancy, not legitimate variation.

---

### 3. Outliers and Noise Must Be Validated

An unusual value is not automatically an incorrect value.

Instead of blindly removing outliers, I applied **domain-based validation**, including:

* BMI consistency checks
* Blood pressure logical validation
* Numerical consistency checks

This helped distinguish between **legitimate extreme observations** and **potentially erroneous records**.

**Key concept:**

> Statistical unusualness does not necessarily mean data invalidity.

---

### 4. Data Leakage Can Create Misleadingly High Performance

One of the most important concepts I learned was **data leakage**.

A model can achieve an apparently excellent result, such as:

**R² ≈ 0.97**

while still being unreliable if a feature contains information that would not legitimately be available at prediction time.

In this project, removing the leakage-related feature caused a substantial change in model performance.

This demonstrated that:

> **High accuracy does not necessarily mean a good Machine Learning model.**

The real objective is to build a model that performs well using **valid, independent, and realistically available information**.

---

### 5. Preprocessing Is Part of the Modeling Process

Preprocessing is not an isolated step performed before Machine Learning.

Every preprocessing decision can influence:

```text
Raw Data
   ↓
Data Quality
   ↓
Missing Values / Noise / Outliers
   ↓
Feature Representation
   ↓
Training Data
   ↓
Testing Data
   ↓
Model Performance
   ↓
Final Conclusions
```

Changing how missing values, duplicates, noise, or leakage are handled can change the data distribution and ultimately affect model performance.

**Key concept:**

> Preprocessing decisions are modeling decisions because they directly influence what information the model learns from.

---

### 6. Model Performance Must Be Interpreted, Not Just Reported

Another important lesson was that evaluation metrics should be interpreted in the context of the problem.

I learned to look beyond a single metric and compare:

* **MAE** — average magnitude of prediction error
* **RMSE** — sensitivity to larger errors
* **R²** — proportion of variance explained by the model

More importantly, these metrics must be considered alongside **data quality, leakage, feature validity, and generalization**.

---

### 🎯 Overall Learning

The biggest lesson from this project was:

> **Reliable Machine Learning is more important than artificially high performance.**

A strong ML workflow should therefore focus on:

**Data Quality → Valid Preprocessing → Leakage Detection → Appropriate Modeling → Meaningful Evaluation → Reliable Conclusions**

This project shifted my perspective from *“How can I get a better score?”* to *“Why is the model performing this way, and can I trust the result?”*

---
## 🏗️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Programming |
| 🐼 Pandas | Data manipulation and preprocessing |
| 🔢 NumPy | Numerical operations |
| 🤖 Scikit-learn | Machine learning and model training |
| 💾 Joblib | Model serialization and loading |
| 📊 Matplotlib | Data visualization and analysis |
| 🌐 Streamlit | Interactive prediction interface |
| 📓 Jupyter / Google Colab | Data analysis, experimentation, and model development |

---
## 🚀 How to Run

Follow the steps below to run the Personalized Diet Recommendation application locally.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd personalized-diet-recommendation
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

### 5. Use the Application

Enter the required user information in the **NutriCare** interface and click the prediction button to generate the predicted caloric intake.

### ⚠️ Important

Make sure the trained model file is present in the project directory before running the application.

```text
app.py
clean_model.pkl
requirements.txt
```
---
## 📂 Project Structure

```text
personalized-diet-recommendation/
│
├── notebooks/
│   └── GitHub_project.ipynb
│
├── app.py
├── clean_model.pkl
├── Personalized_Diet_Recommendations.csv
├── README.md
├── requirements.txt
└── .gitignore
```

### 📄 File Description

| File / Folder                           | Description                                   |
| --------------------------------------- | --------------------------------------------- |
| `app.py`                                | Streamlit prediction application              |
| `clean_model.pkl`                       | Trained machine learning model                |
| `notebooks/GitHub_project.ipynb`        | Complete data analysis and ML experimentation |
| `Personalized_Diet_Recommendations.csv` | Original dataset                              |
| `requirements.txt`                      | Required Python libraries                     |
| `README.md`                             | Project documentation                         |
| `.gitignore`                            | Files and folders excluded from Git tracking  |

---
## 👩‍💻 Author

**Saudamini Deshmukh**


