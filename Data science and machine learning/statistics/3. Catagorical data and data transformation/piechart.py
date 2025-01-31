import matplotlib.pyplot as plt
fruits = ['Apple', 'Banana', 'Orange', 'Mango']
frequencies = [30, 20, 25, 15]

# Pie Chart
plt.pie(frequencies, labels=fruits, autopct='%1.2f%%')
plt.title('Favorite Fruits')
plt.show()