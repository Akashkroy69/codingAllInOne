import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [15, 25, 30, 10, 20]
})

# Bar chart
# plt.figure(figsize=(8, 5))
# sns.barplot(x='Category', y='Values', data=data, palette='viridis')
# plt.title('Bar Chart Example')
# plt.xlabel('Category')
# plt.ylabel('Values')
# plt.show()

# pie chart
# Pie chart
plt.figure(figsize=(6, 6))
plt.pie(data['Values'], labels=data['Category'], autopct='%1.2f%%', startangle=10)
# colors=plt.cm.viridis.colors[:5]
plt.title('Pie Chart Example')
plt.show()


