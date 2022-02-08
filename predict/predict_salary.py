"""
Author: Siddhant Mahajani
predict_salary.py - Salary prediction program to predict salary
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

import warnings
warnings.filterwarnings('ignore')


def predict(experience):
    dataset = pd.read_csv('data/data.csv')
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    polynomialFeatures = PolynomialFeatures(degree=3)
    x_polynomial = polynomialFeatures.fit_transform(x)
    polynomialRegression = LinearRegression()
    polynomialRegression.fit(x_polynomial, y)

    result = polynomialRegression.predict(polynomialFeatures.fit_transform([[float(experience)]]))
    return result
