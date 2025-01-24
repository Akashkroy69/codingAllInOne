import pandas as pd
import numpy as np
# categories = ['Dog', 'Cat', 'Bird']
# data = pd.Categorical(['Dog', 'Cat', 'Dog','Cat','Cat'], categories=categories, ordered=True)
# print(data)


data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David',"akash","Aman"],
    'Gender': ['Female', 'Male', 'Male', 'Female',"Male","Male"],
    'Rating': ['Good', 'Average', 'Good', 'Poor',"Poor","Good"]
})

# Analyze
print("----------------")
print(data['Gender'].value_counts())
unique_categories = data['Rating'].unique()
print("Unique categories in Rating:", unique_categories)
data['Rating_encoded'] = pd.Categorical(data['Rating'],categories=unique_categories,ordered=True).codes
medianRating = np.median(data['Rating_encoded'])
meanRating = np.mean(data['Rating_encoded'])

print(data)
print("median of rating",medianRating)
print("mean of rating",meanRating)

# print("----------------")

# # Convert to categorical
# data['Gender'] = data['Gender'].astype('category')
# print(data['Gender'])
# print("-------encoding---------")
# # Encode using Label Encoding
# data['Gender_Code'] = data['Gender'].cat.codes
# print(data['Gender_Code'])
# print("----------------")

# # Encode using One-Hot Encoding
# encoded = pd.get_dummies(data['Rating'], prefix='Rating')
# print("----------------")

# # Add the encoded columns to the dataset
# data = pd.concat([data, encoded], axis=1)
# print("----------------")

# print(data)
# print("----------------")



