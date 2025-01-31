import seaborn as sns
import matplotlib.pyplot as plt
import random
import pandas as pd
# Define possible breakfast options

breakfast_options = ["Pancakes", "Omelette", "Cereal", "Toast", "Fruit", "Paratha", "None"]



# Generate random breakfast data for 100 students

breakfast_data = [random.choice(breakfast_options) for _ in range(90)]
students = [
    "Alice", "Bob", "Charlie", "David", "Ella", "Fiona", "George", "Hannah", "Ian", "Jack",
    "Kara", "Liam", "Mia", "Nathan", "Olivia", "Peter", "Quincy", "Rachel", "Sophia", "Tom",
    "Uma", "Victor", "Wendy", "Xander", "Yara", "Zane", "Ava", "Ben", "Chloe", "Daniel",
    "Eva", "Frank", "Grace", "Harry", "Isla", "Jake", "Katie", "Luke", "Maya", "Noah",
    "Oscar", "Penny", "Quinn", "Ruby", "Sam", "Tina", "Umar", "Violet", "Will", "Xenia",
    "Yvonne", "Zack", "Amy", "Blake", "Claire", "Dean", "Elena", "Felix", "Gina", "Henry",
    "Isabelle", "James", "Kylie", "Leo", "Megan", "Nick", "Opal", "Paula", "Quinton", "Rose",
    "Sara", "Tim", "Una", "Vince", "Willa", "Xavi", "Yasmin", "Zion", "Aria", "Bryan",
    "Charlotte", "Derek", "Emily", "Finn", "Gabby", "Hugo", "Isabel", "Jade", "Kyle", "Lara"
]

print(len(breakfast_data))
print(len(students))

dataFrame = pd.DataFrame({
    "students" : students,
    "breakfast": breakfast_data
})

print(dataFrame)

# sns.countplot(dataFrame,x="breakfast",palette="pastel",order=dataFrame["breakfast"].value_counts().index)
# freq = dataFrame['breakfast'].value_counts()
# plt.pie(freq,labels=)
plt.show()