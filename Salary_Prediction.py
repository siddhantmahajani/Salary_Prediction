# Predict salary based on experience level of the Employee

# import libraries
import pandas as pd

# import dataset
dataset = pd.read_csv('data/salary_data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# apply polynomial regression on the complete dataset for better salary prediction
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
polynomialFeatures = PolynomialFeatures(degree=3)
x_polynomial = polynomialFeatures.fit_transform(x)
polynomialRegression = LinearRegression()
polynomialRegression.fit(x_polynomial, y)

# predict the salary based on the experience which is received as input
# the experience should be between 1 to 20
experience = input('Enter the number of experience in years: ')
print(polynomialRegression.predict(polynomialFeatures.fit_transform([[float(experience)]])))