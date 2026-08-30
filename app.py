# import streamlit as st
# import pandas as pd
# import joblib


# # ============================================================
# # PAGE CONFIG
# # ============================================================

# st.set_page_config(
#     page_title="Caloric Intake Prediction",
#     page_icon="🥗",
#     layout="wide"
# )


# # ============================================================
# # CUSTOM HTML + CSS
# # ============================================================

# st.markdown("""
# <style>

# .stApp {
#     background-color: #f5f8f5;
# }

# .title {
#     text-align: center;
#     color: #2e7d32;
#     font-size: 40px;
#     font-weight: 700;
# }

# .subtitle {
#     text-align: center;
#     color: #666;
#     font-size: 17px;
#     margin-bottom: 30px;
# }

# .section {
#     background-color: white;
#     padding: 15px 20px;
#     border-radius: 12px;
#     margin-top: 20px;
#     border-left: 5px solid #2e7d32;
# }

# .result {
#     background-color: #e8f5e9;
#     padding: 25px;
#     border-radius: 15px;
#     text-align: center;
#     margin-top: 25px;
# }

# .result-title {
#     font-size: 20px;
#     color: #2e7d32;
# }

# .result-value {
#     font-size: 38px;
#     font-weight: bold;
#     color: #1b5e20;
# }

# </style>
# """, unsafe_allow_html=True)


# # ============================================================
# # LOAD MODEL
# # ============================================================

# @st.cache_resource
# def load_model():

#     try:
#         return joblib.load("caloric_intake_model (3).pkl")

#     except FileNotFoundError:

#         st.error(
#             "❌ caloric_intake_model.pkl not found."
#         )

#         st.info(
#             "Place caloric_intake_model.pkl "
#             "in the same folder as app.py."
#         )

#         st.stop()


# model = load_model()


# # ============================================================
# # HEADER
# # ============================================================

# st.markdown(
#     '<div class="title">🥗 Caloric Intake Prediction</div>',
#     unsafe_allow_html=True
# )

# st.markdown(
#     """
#     <div class="subtitle">
#     Enter the user's information to estimate daily caloric intake.
#     </div>
#     """,
#     unsafe_allow_html=True
# )


# # ============================================================
# # USER INFORMATION
# # ============================================================

# st.markdown(
#     '<div class="section"><h3>👤 Personal Information</h3></div>',
#     unsafe_allow_html=True
# )

# col1, col2, col3 = st.columns(3)

# with col1:
#     patient_id = st.text_input("Patient ID")

# with col2:
#     age = st.number_input(
#         "Age",
#         min_value=18,
#         max_value=100,
#         value=25
#     )

# with col3:
#     gender = st.selectbox(
#         "Gender",
#         ["Female", "Male", "Other"]
#     )


# col1, col2, col3 = st.columns(3)

# with col1:
#     height = st.number_input(
#         "Height (cm)",
#         min_value=100.0,
#         max_value=250.0,
#         value=170.0
#     )

# with col2:
#     weight = st.number_input(
#         "Weight (kg)",
#         min_value=20.0,
#         max_value=250.0,
#         value=70.0
#     )

# with col3:
#     bmi = st.number_input(
#         "BMI",
#         min_value=5.0,
#         max_value=60.0,
#         value=23.0
#     )


# # ============================================================
# # HEALTH INFORMATION
# # ============================================================

# st.markdown(
#     '<div class="section"><h3>❤️ Health Information</h3></div>',
#     unsafe_allow_html=True
# )

# col1, col2, col3 = st.columns(3)

# with col1:
#     chronic_disease = st.selectbox(
#         "Chronic Disease",
#         [
#             "Diabetes",
#             "Heart Disease",
#             "Hypertension",
#             "Obesity",
#             "None"
#         ]
#     )

# with col2:
#     systolic = st.number_input(
#         "Blood Pressure - Systolic",
#         min_value=70,
#         max_value=250,
#         value=120
#     )

# with col3:
#     diastolic = st.number_input(
#         "Blood Pressure - Diastolic",
#         min_value=40,
#         max_value=150,
#         value=80
#     )


# col1, col2, col3 = st.columns(3)

# with col1:
#     cholesterol = st.number_input(
#         "Cholesterol Level",
#         min_value=50.0,
#         max_value=500.0,
#         value=200.0
#     )

# with col2:
#     blood_sugar = st.number_input(
#         "Blood Sugar Level",
#         min_value=50.0,
#         max_value=400.0,
#         value=100.0
#     )

# with col3:
#     genetic_risk = st.selectbox(
#         "Genetic Risk Factor",
#         ["Yes", "No"]
#     )


# col1, col2, col3 = st.columns(3)

# with col1:
#     allergies = st.selectbox(
#         "Allergies",
#         [
#             "Lactose Intolerance",
#             "Nut Allergy",
#             "Gluten Intolerance",
#             "None"
#         ]
#     )

# with col2:
#     genetic_risk = genetic_risk

# with col3:
#     pass


# # ============================================================
# # LIFESTYLE
# # ============================================================

# st.markdown(
#     '<div class="section"><h3>🏃 Lifestyle Information</h3></div>',
#     unsafe_allow_html=True
# )

# col1, col2, col3 = st.columns(3)

# with col1:
#     daily_steps = st.number_input(
#         "Daily Steps",
#         min_value=0,
#         max_value=50000,
#         value=5000
#     )

# with col2:
#     exercise_frequency = st.number_input(
#         "Exercise Frequency (days/week)",
#         min_value=0,
#         max_value=7,
#         value=3
#     )

# with col3:
#     sleep_hours = st.number_input(
#         "Sleep Hours",
#         min_value=0.0,
#         max_value=24.0,
#         value=7.0
#     )


# col1, col2, col3 = st.columns(3)

# with col1:
#     alcohol = st.selectbox(
#         "Alcohol Consumption",
#         ["Yes", "No"]
#     )

# with col2:
#     smoking = st.selectbox(
#         "Smoking Habit",
#         ["Yes", "No"]
#     )

# with col3:
#     dietary_habits = st.selectbox(
#         "Dietary Habits",
#         ["Healthy", "Moderate", "Unhealthy"]
#     )


# # ============================================================
# # DIET INFORMATION
# # ============================================================

# st.markdown(
#     '<div class="section"><h3>🍎 Dietary Information</h3></div>',
#     unsafe_allow_html=True
# )

# col1, col2, col3 = st.columns(3)

# with col1:
#     protein = st.number_input(
#         "Protein Intake",
#         min_value=0.0,
#         value=60.0
#     )

# with col2:
#     carbs = st.number_input(
#         "Carbohydrate Intake",
#         min_value=0.0,
#         value=250.0
#     )

# with col3:
#     fat = st.number_input(
#         "Fat Intake",
#         min_value=0.0,
#         value=70.0
#     )


# col1, col2, col3 = st.columns(3)

# with col1:
#     cuisine = st.selectbox(
#         "Preferred Cuisine",
#         [
#             "Indian",
#             "Chinese",
#             "Italian",
#             "Mexican",
#             "Mediterranean",
#             "Other"
#         ]
#     )

# with col2:
#     food_aversions = st.selectbox(
#         "Food Aversions",
#         ["Spicy", "Sweet", "Salty", "None"]
#     )

# with col3:
#     recommended_calories = st.number_input(
#         "Recommended Calories",
#         min_value=0.0,
#         value=2200.0
#     )


# # ============================================================
# # RECOMMENDED NUTRIENTS
# # ============================================================

# st.markdown(
#     '<div class="section"><h3>📊 Recommended Nutrition</h3></div>',
#     unsafe_allow_html=True
# )

# col1, col2, col3 = st.columns(3)

# with col1:
#     recommended_protein = st.number_input(
#         "Recommended Protein",
#         min_value=0.0,
#         value=60.0
#     )

# with col2:
#     recommended_carbs = st.number_input(
#         "Recommended Carbs",
#         min_value=0.0,
#         value=250.0
#     )

# with col3:
#     recommended_fats = st.number_input(
#         "Recommended Fats",
#         min_value=0.0,
#         value=70.0
#     )


# recommended_meal_plan = st.selectbox(
#     "Recommended Meal Plan",
#     [
#         "Balanced",
#         "High Protein",
#         "Low Carb",
#         "Low Fat",
#         "Vegetarian"
#     ]
# )


# # ============================================================
# # CALCULATED FEATURES
# # ============================================================

# st.markdown(
#     '<div class="section"><h3>🧮 Calculated Features</h3></div>',
#     unsafe_allow_html=True
# )

# calculated_bmi = weight / ((height / 100) ** 2)

# bmi_difference = abs(bmi - calculated_bmi)

# calculated_calories = (
#     10 * weight +
#     6.25 * height -
#     5 * age
# )

# calorie_difference = (
#     recommended_calories - calculated_calories
# )

# st.write(
#     f"Calculated BMI: **{calculated_bmi:.2f}**"
# )

# st.write(
#     f"BMI Difference: **{bmi_difference:.2f}**"
# )


# # ============================================================
# # PREDICTION
# # ============================================================

# st.divider()

# if st.button(
#     "🔮 Predict Caloric Intake",
#     use_container_width=True
# ):

#     input_data = {

#         "Patient_ID": patient_id,
#         "Age": age,
#         "Gender": gender,
#         "Height_cm": height,
#         "Weight_kg": weight,
#         "BMI": bmi,

#         "Chronic_Disease": chronic_disease,

#         "Blood_Pressure_Systolic": systolic,
#         "Blood_Pressure_Diastolic": diastolic,

#         "Cholesterol_Level": cholesterol,
#         "Blood_Sugar_Level": blood_sugar,

#         "Genetic_Risk_Factor": genetic_risk,
#         "Allergies": allergies,

#         "Daily_Steps": daily_steps,
#         "Exercise_Frequency": exercise_frequency,
#         "Sleep_Hours": sleep_hours,

#         "Alcohol_Consumption": alcohol,
#         "Smoking_Habit": smoking,

#         "Dietary_Habits": dietary_habits,

#         "Protein_Intake": protein,
#         "Carbohydrate_Intake": carbs,
#         "Fat_Intake": fat,

#         "Preferred_Cuisine": cuisine,
#         "Food_Aversions": food_aversions,

#         "Recommended_Calories": recommended_calories,
#         "Recommended_Protein": recommended_protein,
#         "Recommended_Carbs": recommended_carbs,
#         "Recommended_Fats": recommended_fats,

#         "Recommended_Meal_Plan": recommended_meal_plan,

#         "Calculated_BMI": calculated_bmi,
#         "BMI_Difference": bmi_difference,

#         "Calculated_Calories": calculated_calories,
#         "Calorie_Difference": calorie_difference
#     }


#     input_df = pd.DataFrame([input_data])


#     try:

#         prediction = model.predict(input_df)

#         predicted_calories = float(prediction[0])


#         st.markdown(
#             f"""
#             <div class="result">

#                 <div class="result-title">
#                     Predicted Daily Caloric Intake
#                 </div>

#                 <div class="result-value">
#                     {predicted_calories:.0f} kcal
#                 </div>

#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         st.success(
#             "✅ Prediction generated successfully!"
#         )


#     except Exception as error:

#         st.error("❌ Prediction failed.")

#         st.code(str(error))


# # ============================================================
# # FOOTER
# # ============================================================

# st.divider()

# st.caption(
#     "Machine Learning Based Caloric Intake Prediction"
# )







import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Caloric Intake Prediction",
    page_icon="🥗",
    layout="centered"
)


# ============================================================
# SIMPLE CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #f6f8f7;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
}

h1 {
    color: #245c3a;
}

.stButton > button {
    background-color: #2e7d4f;
    color: white;
    border: none;
    border-radius: 8px;
    height: 45px;
    font-weight: 600;
}

.result-box {
    background-color: #eaf5ee;
    border: 1px solid #cde5d4;
    border-radius: 10px;
    padding: 25px;
    text-align: center;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("clean_model.pkl")


try:
    model = load_model()

except Exception as e:
    st.error("Model file not found.")
    st.stop()


# ============================================================
# HEADER
# ============================================================

st.title("🥗 Caloric Intake Prediction")

st.write(
    "A simple demonstration of the clean machine learning model."
)

st.divider()


# ============================================================
# USER INPUT
# ============================================================

st.subheader("Personal Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=25
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Female", "Male", "Other"]
    )

with col3:
    height = st.number_input(
        "Height (cm)",
        min_value=100,
        max_value=250,
        value=170
    )


col1, col2, col3 = st.columns(3)

with col1:
    weight = st.number_input(
        "Weight (kg)",
        min_value=20,
        max_value=250,
        value=70
    )

with col2:
    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=24.0
    )

with col3:
    daily_steps = st.number_input(
        "Daily Steps",
        min_value=0,
        max_value=50000,
        value=5000
    )


# ============================================================
# HEALTH INFORMATION
# ============================================================

st.subheader("Health Information")

col1, col2, col3 = st.columns(3)

with col1:
    chronic_disease = st.selectbox(
        "Chronic Disease",
        [
            "Diabetes",
            "Heart Disease",
            "Hypertension",
            "Obesity"
        ]
    )

with col2:
    systolic = st.number_input(
        "Systolic BP",
        min_value=70,
        max_value=250,
        value=120
    )

with col3:
    diastolic = st.number_input(
        "Diastolic BP",
        min_value=40,
        max_value=150,
        value=80
    )


col1, col2 = st.columns(2)

with col1:
    cholesterol = st.number_input(
        "Cholesterol Level",
        min_value=50,
        max_value=500,
        value=200
    )

with col2:
    blood_sugar = st.number_input(
        "Blood Sugar Level",
        min_value=50,
        max_value=400,
        value=100
    )


# ============================================================
# LIFESTYLE
# ============================================================

st.subheader("Lifestyle")

col1, col2, col3 = st.columns(3)

with col1:
    exercise = st.number_input(
        "Exercise Days / Week",
        min_value=0,
        max_value=7,
        value=3
    )

with col2:
    sleep = st.number_input(
        "Sleep Hours",
        min_value=0.0,
        max_value=24.0,
        value=7.0
    )

with col3:
    dietary_habits = st.selectbox(
        "Dietary Habits",
        ["Healthy", "Moderate", "Unhealthy"]
    )


# ============================================================
# PREDICTION
# ============================================================

st.divider()

if st.button(
    "Predict Caloric Intake",
    use_container_width=True
):

    input_data = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Height_cm": height,
        "Weight_kg": weight,
        "BMI": bmi,
        "Chronic_Disease": chronic_disease,
        "Blood_Pressure_Systolic": systolic,
        "Blood_Pressure_Diastolic": diastolic,
        "Cholesterol_Level": cholesterol,
        "Blood_Sugar_Level": blood_sugar,

        # Default values for remaining features
        "Genetic_Risk_Factor": "No",
        "Allergies": "None",
        "Daily_Steps": daily_steps,
        "Exercise_Frequency": exercise,
        "Sleep_Hours": sleep,
        "Alcohol_Consumption": "No",
        "Smoking_Habit": "No",
        "Dietary_Habits": dietary_habits,
        "Protein_Intake": 60,
        "Carbohydrate_Intake": 250,
        "Fat_Intake": 70,
        "Preferred_Cuisine": "Indian",
        "Food_Aversions": "None",
        "Recommended_Protein": 60,
        "Recommended_Carbs": 250,
        "Recommended_Fats": 70,
        "Recommended_Meal_Plan": "Balanced"
    }])

    try:

        prediction = model.predict(input_data)[0]

        st.markdown(
            f"""
            <div class="result-box">
                <h3>Predicted Daily Caloric Intake</h3>
                <h1>{prediction:.0f} kcal</h1>
                <p>Estimated value generated by the clean model.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.warning(
            "Educational project: This model demonstrates the "
            "impact of data quality and data leakage on machine learning performance."
        )

    except Exception as e:

        st.error("Prediction failed.")

        st.code(str(e))


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Personalized Diet Recommendation • Machine Learning Research Project"
)