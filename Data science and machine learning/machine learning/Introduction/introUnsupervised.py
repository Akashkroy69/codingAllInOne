from sklearn.cluster import KMeans
import numpy as np

# Data: heights and weights of students
students = np.array([[150, 45], [160, 50], [170, 70], [180, 80], [155, 48], [175, 75]])

# Cluster into 2 groups
kmeans = KMeans(n_clusters=2)
kmeans.fit(students)

# Predict group for a new student
new_student = np.array([[165, 60]])
group = kmeans.predict(new_student)
print("New student belongs to group:", group[0])
