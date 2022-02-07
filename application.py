"""
Author: Siddhant Mahajani
application.py - Main program to perform salary prediction using streamlit for web UI
"""

import streamlit as st
from predict import predict_salary

import warnings
warnings.filterwarnings("ignore")


@st.cache
def getPredictedSalary(exp):
    response = float(predict_salary.predict(experience=exp))
    return response


st.title("Salary Prediction")
st.write("A simple program to perform salary prediction based on the data present")

form = st.form(key="salary-prediction-form")
experience = form.text_input("Enter number of years of experience between 1-20 to predict expected salary: ")
predict = form.form_submit_button(label="Predict")

if predict:
    result = getPredictedSalary(experience)
    st.write("The expected salary is: ", "{:.2f}".format(result))