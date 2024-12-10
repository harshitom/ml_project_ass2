import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

# Load dataset (Assuming you have it downloaded as 'nhanes_data.csv')
data = pd.read_csv('nhanes_data.csv')

# Select relevant columns
data = data[['SEQN', 'Age', 'Gender', 'CardiovascularHealth']]  # Example column names

# Preprocessing (handle missing values, categorize age)
data = data.dropna()  # Drop rows with missing values for simplicity
data['AgeGroup'] = pd.cut(data['Age'], bins=[0, 20, 30, 40, 50, 60, 70, 100], labels=['10-20', '21-30', '31-40', '41-50', '51-60', '61-70', 'Above 70'])

# Convert categorical variables to numeric
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})  # Binary encoding
data['CardiovascularHealth'] = data['CardiovascularHealth'].map({'No': 0, 'Yes': 1})

# Split the data into features and target
X = data[['Age', 'Gender']]  # Features
y = data['CardiovascularHealth']  # Target
