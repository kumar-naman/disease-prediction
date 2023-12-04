# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:53:51 2022

@author: Naman Kumar
"""
# login page
import pickle
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd


def creds_entered():
    if st.session_state["user"].strip() == "admin" and st.session_state["passwd"].strip() == "admin": 
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        st.error("Invalid Username/Password !!!!")

def authenticate_user():
    
    if "authenticated" not in st.session_state:
        st.sidebar.image('logo.png')
        st.markdown("<h1 style='text-align: center;'> LOGIN PAGE </h1><br>", unsafe_allow_html=True)
        st.header("Enter Username & Password: ")
        st.text_input(label="Username:", value="", key="user", on_change=creds_entered) 
        st.text_input(label="Password", value="", key="passwd", type="password", on_change=creds_entered)
        return False
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.sidebar.image('logo.png')
            st.markdown("<h1 style='text-align: center;'> LOGIN PAGE </h1><br>", unsafe_allow_html=True)
            st.header("Enter Username & Password: ")
            st.text_input(label="Username:", value="", key="user", on_change=creds_entered)
            st.text_input(label="Password :", value="", key="passwd", type="password", on_change=creds_entered)
            return False

if authenticate_user():


    # loading the saved models

    diabetes_model = pickle.load(open('saved models/diabetes_model.sav', 'rb'))

    heart_model = pickle.load(open('saved models/nb_model.pkl','rb'))

    kidney_model = pickle.load(open('saved models/kd_model.pkl', 'rb'))
    
    
    # sidebar for navigation
    with st.sidebar:
        
        st.sidebar.image('logo.png')
        selected = option_menu( 'Multiple Disease Prediction System',                           
                            ['Home',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Kidney Disease Prediction'],
                            icons=['house','activity','heart','kanban'],
                            default_index=0,
                            styles={
                                "container": {"padding": "0!important", "background-color": ""},
                                "icon": {"color": "orange", "font-size": "25px"}, 
                                "nav-link": { "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                "nav-link-selected": {"background-color": "red"},
                                }
                            )
        
        
    if selected == 'Home':
        st.title('Multiple Disease Prediction System')
        st.image('https://www.medicaldevice-network.com/wp-content/uploads/sites/23/2021/02/shutterstock_1364662745.jpg')
        st.info('In this digital world, data is an asset, and enormous data was generated in all the fields. Data in the healthcare industry consists of all the information related to patients. Here a general architecture has been proposed for predicting the disease in the healthcare industry. Many of the existing models are concentrating on one disease per analysis. Like one analysis for diabetes analysis, one for cancer analysis, one for skin diseases like that. There is no common system present that can analyze more than one disease at a time.')
        st.error('In this system, we are going to analyze Diabetes, Heart, and malaria disease analysis. Later many more diseases can be included In multiple disease prediction, it is possible to predict more than one disease at a time. So, the user doesn’t need to traverse different sites in order to predict the diseases. We are taking three diseases that are Liver, Diabetes, and Heart. As all the three diseases are correlated to each other. To implement multiple disease analyses we are going to use machine learning algorithms and StreamLit. When the user is accessing this API, the user has to send the parameters of the disease along with the disease name. ')
        st.info('The main feature will be the machine learning, in which we will be using algorithms such as Naïve Bayes Algorithm, KNearest Algorithm, Decision Tree Algorithm, Random Forest Algorithm and Support Vector Machine, which will predict accurate disease and also, will find which algorithm gives a faster and efficient result by comparatively comparing. The importance of this system analysis is that while analyzing the diseases all the parameters which cause the disease are included so it is possible to detect the disease efficiently and more accurately. The final model behavior will be saved as a python pickle file.')
               

    if selected == 'Heart Disease Prediction':

        st.title("Heart Disease Prediction")
        age = st.number_input("Age")
        gender = st.selectbox("Gender (0-Male, 1-Female)", ["0", "1"])
        cp = st.number_input("Chest Pain Type")
        trestbps = st.number_input("Resting Blood Pressure")
        chol = st.number_input("Cholesterol")
        fbs = st.number_input("Fasting Blood Sugar")
        restecg = st.number_input("Resting ECG")
        thalach = st.number_input("Maximum Heart Rate Achieved")
        exang = st.number_input("Exercise-Induced Angina")
        oldpeak = st.number_input("ST Depression Induced by Exercise")
        slope = st.number_input("Slope of the Peak Exercise ST Segment")
        ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy")
        thal = st.number_input("Thalassemia")

        if st.button("Predict Heart Disease"):
            user_data = {
                "age": int(age),
                "gender": int(gender),
                "cp": float(cp),
                "trestbps": float(trestbps),
                "chol": float(chol),
                "fbs": float(fbs),
                "restecg": float(restecg),
                "thalach": float(thalach),
                "exang": float(exang),
                "oldpeak": float(oldpeak),
                "slope": float(slope),
                "ca": float(ca),
                "thal": float(thal)
            }

            input_data = pd.DataFrame([user_data])
            heart_prediction = heart_model.predict(input_data)

            if heart_prediction[0] == 1:
                st.write("Yes, you are at risk of Heart Disease.")
            else:
                st.write("No, you are not at risk of Heart Disease.")

    if selected == 'Kidney Disease Prediction':

        st.title("Kidney Disease Prediction")
        age = st.number_input("Age")
        blood_pressure = st.number_input("Blood Pressure")
        specific_gravity = st.number_input("Specific Gravity")
        albumin = st.number_input("Albumin")
        sugar = st.number_input("Sugar")
        red_blood_cells = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
        pus_cell = st.selectbox("Pus Cell", ["normal", "abnormal"])
        pus_cell_clumps = st.selectbox("Pus Cell Clumps", ["notpresent", "present"])
        bacteria = st.selectbox("Bacteria", ["notpresent", "present"])
        blood_glucose_random = st.number_input("Blood Glucose Random")
        blood_urea = st.number_input("Blood Urea")
        serum_creatinine = st.number_input("Serum Creatinine")
        sodium = st.number_input("Sodium")
        potassium = st.number_input("Potassium")
        hemoglobin = st.number_input("Hemoglobin")
        hypertension = st.selectbox("Hypertension", ["yes", "no"])
        diabetes_mellitus = st.selectbox("Diabetes Mellitus", ["yes", "no"])
        coronary_artery_disease = st.selectbox("Coronary Artery Disease", ["yes", "no"])
        appetite = st.selectbox("Appetite", ["good", "poor"])
        pedal_edema = st.selectbox("Pedal Edema", ["yes", "no"])
        anemia = st.selectbox("Anemia", ["yes", "no"])

        if st.button("Predict Kidney Disease"):
            user_data = {
                "age": age,
                "blood_pressure": blood_pressure,
                "specific_gravity": specific_gravity,
                "albumin": albumin,
                "sugar": sugar,
                "red_blood_cells": red_blood_cells,
                "pus_cell": pus_cell,
                "pus_cell_clumps": pus_cell_clumps,
                "bacteria": bacteria,
                "blood_glucose_random": blood_glucose_random,
                "blood_urea": blood_urea,
                "serum_creatinine": serum_creatinine,
                "sodium": sodium,
                "potassium": potassium,
                "hemoglobin": hemoglobin,
                "hypertension": hypertension,
                "diabetes_mellitus": diabetes_mellitus,
                "coronary_artery_disease": coronary_artery_disease,
                "appetite": appetite,
                "pedal_edema": pedal_edema,
                "anemia": anemia
            }
            input_data = pd.DataFrame([user_data])
            input_data_encoded = pd.get_dummies(input_data)
            kidney_prediction = kidney_model.predict(input_data_encoded)
            if kidney_prediction[0] == 1:
                st.write("Yes, you are at risk of Kidney Disease.")
            else:
                st.write("No, you are not at risk of Kidney Disease.")

    if selected == 'Diabetes Prediction':

        st.title("Diabetes Prediction")
        pregnancies = st.number_input("Pregnancies")
        glucose = st.number_input("Glucose")
        blood_pressure = st.number_input("Blood Pressure")
        skin_thickness = st.number_input("Skin Thickness")
        insulin = st.number_input("Insulin")
        bmi = st.number_input("BMI")
        diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function")
        age = st.number_input("Age")

        if st.button("Predict Diabetes"):
            user_data = {
                "Pregnancies": int(pregnancies),
                "Glucose": glucose,
                "BloodPressure": blood_pressure,
                "SkinThickness": skin_thickness,
                "Insulin": insulin,
                "BMI": bmi,
                "DiabetesPedigreeFunction": diabetes_pedigree_function,
                "Age": int(age)
            }
            input_data = pd.DataFrame([user_data])
            diabetes_prediction = diabetes_model.predict(input_data)
            if diabetes_prediction[0] == 1:
                st.write("Yes, you Have Diabetes.")
            else:
                st.write("No, you Don't Have Diabetes.")


