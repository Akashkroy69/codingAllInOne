import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Create a bar chart
plt.figure(figsize=(8, 5))
print(data['species'].value_counts().index)
sns.countplot(data=data, x='species', palette='pastel', order=data['species'].value_counts().index)
plt.title('Bar Chart of Iris Species', fontsize=14)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.show()


# Calculate the count of each species
# species_counts = data['species'].value_counts()
# print(species_counts)

# # Create a pie chart
# plt.figure(figsize=(6, 6))
# plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=90)
# plt.title('Pie Chart of Iris Species', fontsize=14)
# plt.show()

