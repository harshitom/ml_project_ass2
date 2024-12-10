import pandas as pd
import numpy as np

# Step 1: Load the dataset
# Make sure the dataset path is correct. Replace the path below with the actual path to your CSV file.
data = pd.read_csv('path_to_your_data/nhanes_data.csv')

# Step 2: Check for any missing data
print("Missing data:\n", data.isnull().sum())

# Step 3: Handle missing values (for simplicity, let's drop the rows with missing data)
data.dropna(inplace=True)

# Step 4: Select only relevant columns (You can choose based on the dataset columns you have)
# Assuming the dataset contains columns for SEQN (Survey ID), Age, Gender, and CardiovascularHealth.
# Change the column names below based on your dataset.
data = data[['SEQN', 'Age', 'Gender', 'CardiovascularHealth']]

# Step 5: Age categorization (Dividing Age into specified ranges)
data['AgeGroup'] = pd.cut(data['Age'], bins=[0, 20, 30, 40, 50, 60, 70, 100], 
                           labels=['10-20', '21-30', '31-40', '41-50', '51-60', '61-70', 'Above 70'])

# Step 6: Convert categorical variables to numeric values
# Gender: Male = 0, Female = 1
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# Cardiovascular Health: No = 0, Yes = 1
data['CardiovascularHealth'] = data['CardiovascularHealth'].map({'No': 0, 'Yes': 1})

# Step 7: Check the preprocessed data
print("\nPreprocessed Data:\n", data.head())

# Step 8: Save the preprocessed data to a new CSV file for future use
data.to_csv('path_to_save/processed_nhanes_data.csv', index=False)

