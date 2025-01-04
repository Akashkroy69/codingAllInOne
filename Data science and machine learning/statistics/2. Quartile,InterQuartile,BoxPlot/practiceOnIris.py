import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataFrame = sns.load_dataset('iris')
sepal_length = dataFrame["sepal_length"]
print(sepal_length.head())
sorted_sepal = sepal_length.sort_values()


print(dataFrame)
print(sorted_sepal.head())

print("quartiles: ")
first_Q = (len(sepal_length)+1)/4
second_Q = ((len(sepal_length)+1)/4) * 2
third_Q = ((len(sepal_length)+1)/4) * 3
print("first quartile : ",first_Q,"th element")
print("second quartile : ",second_Q,"th element")
print("third quartile : ",third_Q,"th element")


print("------using numpy---------")
first_QElement = np.quantile(sorted_sepal,0.25)
second_QElement = np.quantile(sorted_sepal,0.5)
third_QElement = np.quantile(sorted_sepal,0.75)

print("first quartile element: ",first_QElement)
print("second quartile element: ",second_QElement)
print("third quartile element: ",third_QElement)
print("------using pandas---------")
speal_in_series = pd.Series(sorted_sepal)
first_QElement = sepal_length.quantile(0.25)
second_QElement = sepal_length.quantile(0.5)
third_QElement = sepal_length.quantile(0.75)
print("first quartile element: ",first_QElement)
print("second quartile element: ",second_QElement)
print("third quartile element: ",third_QElement)

plt.boxplot(sorted_sepal)

plt.show()






