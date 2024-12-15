# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:28:33 2024

@author: PAVAN
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

heart_disease_model = pickle.load(open('heart_disease.sav', 'rb'))


st.title('Heart Disease Prediction')


age = st.text_input('Age')
sex = st.text_input('Sex')
cp = st.text_input('Chest Pain types')
trestbps = st.text_input('Resting Blood Pressure')
chol = st.text_input('Serum Cholestoral in mg/dl')
fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
restecg = st.text_input('Resting Electrocardiographic results')
thalach = st.text_input('Maximum Heart Rate achieved')
exang = st.text_input('Exercise Induced Angina')
oldpeak = st.text_input('ST depression induced by exercise')
slope = st.text_input('Slope of the peak exercise ST segment')
ca = st.text_input('Major vessels colored by flourosopy')
thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

# code for Prediction
heart_diagnosis = ''

    # creating a button for Prediction

if st.button('Heart Disease Test Result'):

    user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    user_input = [float(x) for x in user_input]

    heart_prediction = heart_disease_model.predict([user_input])

    if heart_prediction[0] == 1:
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person does not have any heart disease'

st.success(heart_diagnosis)
