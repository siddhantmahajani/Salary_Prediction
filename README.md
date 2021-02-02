Basic salary prediction

The program will predict the basic salary of the employee based on the number of years of experience he has. 
The program takes experience in years as input and then predicts the expected salary of the employee. The experience ranges from 1 to 20 year(s).

Polynomial Regression:
To predict the salaries of the employee, I have used Polynomial Regression with the degree/order 3 to get accurate and reliable salaries as the output. 

Libraries used for prediction:
1. pandas: to read csv passed as input data
2. sklearn: to prepare a model and predict the salaries
3. matplotlib.pyplot: to plot a visualization of the experience vs salaries data

Dataset:
Dataset is present in the data folder. The dataset has 2 columns:
1. Experience
2. Salary
Note: If you want to add your own dataset, create a dataset similar to the one present currently and add the dataset to the data folder. If you have renamed the dataset, make sure to change the dataset name in the code while reading the dataset.

Code:
The code contains 2 files:
1. Salary_Prediction.py: This is a python file which takes experience as input and predicts the expected salary of the employee.
2. Salary_Prediction.ipynb: This is a jupyter notebook file and you'll need either Jupyter notebook or Google Colab to run this file. It will predict the salary for the candidate with 4.3 years of experience and along with that it will also plot the graph of experience vs salaries.