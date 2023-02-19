import streamlit as st
import pickle
import numpy as np

with open ('RegressionModel.pkl', 'rb') as file:
  data = pickle.load(file)
regressor_loaded = data["model"]

def ui():
  st.title("Calorie Burn Estimator")

  genders = {"MALE", "FEMALE"}
  # activityTypes = { 'Walk','Bike', 'Workout', 'Sport', 'Aerobic Workout'}
  activityTypes = { 'Walk','Bike','Aerobic Workout'}

  selected_gender = st.selectbox("Select your gender", genders)

  selected_activityType = st.selectbox("Select your activity", activityTypes)

  user_bmi = float(st.text_input('What is your BMI?', '0'))
  st.write(
    'You can calculate your BMI with https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/english_bmi_calculator/bmi_calculator.html')

  user_activity_hours = 2.0

  user_bpm = float(st.text_input('What was your highest BPM during the activity?', '0'))

  submitted = st.button('Estimate')
  if submitted:
    if selected_gender == 'MALE':
      encoded_gender = [0.0, 0.1]
    else:
      encoded_gender = [1.0, 0.0]
    if (selected_activityType == 'Walk'):
      activity_value = 1
    elif (selected_activityType == 'Bike'):
      activity_value = 2
    elif (selected_activityType == 'Aerobic Workout'):
      activity_value = 5

    user_X = np.array([[encoded_gender[0],encoded_gender[1], user_activity_hours, activity_value, user_bpm, user_bmi]])

    estimate_result = int(regressor_loaded.predict(user_X))
    st.subheader(f"The estimated calorie burn is {estimate_result}k per 30 minutes.")
