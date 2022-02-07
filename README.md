Basic salary prediction

The program will predict the basic salary of the employee based on the number of years of experience he has. <br/>
The program takes experience in years as input and then predicts the expected salary of the employee. The experience ranges from 1 to 20 year(s).<br/>

Polynomial Regression:<br/>
To predict the salaries of the employee, I have used Polynomial Regression with the degree/order 3 to get accurate and reliable salaries as the output.<br/> 

Libraries used for prediction:<br/>
1. pandas: to read csv passed as input data.<br/>
2. sklearn: to prepare a model and predict the salaries.<br/>
3. streamlit: to convert the application into a simple web application.<br/>

Dataset:<br/>
Dataset is present in the data folder. The dataset has 2 columns:<br/>
1. Experience<br/>
2. Salary<br/>
Note: If you want to add your own dataset, create a dataset similar to the one present currently and add the dataset to the data folder. If you have renamed the dataset, make sure to change the dataset name in the code while reading the dataset.<br/>

Code:
The code contains 2 files:<br/>
1. predict_salary.py: This is a python file which takes experience as input and predicts the expected salary of the employee.<br/>
2. application.py: This is the main application file for execution. This will start the application using stream lit on the browser take no of years of experience as input from the user and pass it to predict_salary. Once the salary is returned, it will display the response on browser.<br/>

To execute the application type: streamlit run application.py from cmd. This will execute the code on a web browser.

NOTE: I won't say that the predictions are 100% accurate, it depends on user to user but I found the predictions 90% accurate.<br/>
