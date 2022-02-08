"""
Author: Siddhant Mahajani
application.py - Main program to perform salary prediction using streamlit for web UI
"""

import streamlit as st
from predict import predict_salary

import warnings

warnings.filterwarnings('ignore')


@st.cache
def getPredictedSalary(exp):
    response = float(predict_salary.predict(experience=exp))
    return response


st.title('Salary Prediction')
st.write('A simple program to perform salary prediction based on the data_preparation present')

form = st.form(key='salary-prediction-form')
experience = form.slider(label='Years of Experience', min_value=0, max_value=20)
predict = form.form_submit_button(label='Predict')

if predict:
    result = getPredictedSalary(experience)
    expected_salary = "{:.2f}".format(result)
    st.write('The expected salary for {} year(s) of experience must be {}'.format(experience, expected_salary))
