from sklearn.linear_model import LinearRegression
import numpy as np

# Example data: study hours vs. test scores
study_hours = np.array([[1], [2], [3], [4], [5]])
test_scores = np.array([50, 60, 65, 70, 80])

# Train the model
model = LinearRegression()
model.fit(study_hours, test_scores)

# Predict test score for 6 study hours

num_hours = np.array([[float(input("Enter number of study hours: "))]])
# predicted_score = model.predict([[6]])
predicted_score = model.predict(num_hours)
print("Predicted Test Score for 6 hours:", predicted_score[0])
