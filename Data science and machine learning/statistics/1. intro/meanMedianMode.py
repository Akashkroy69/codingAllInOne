# mean median mode
# mean: average
# median: middle value
# mode: most frequent value
# mean = sum of all values / number of values
# median = middle value of sorted list
import seaborn as sns
import statistics as stats
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = sns.load_dataset("iris")
print(data.dtypes)

# mean
print(data["sepal_length"].mean())
print(data["sepal_width"].mean())
# MEDIAN    
print(data["sepal_length"].median())
# mode
list = [1, 1, 1, 2, 2, 3, 4, 4];
print(stats.mode(list))
print(data.mode())
print(stats.mode(data["sepal_length"]))
print("-----------------")
print(data)
print("-----------------")
print(data.describe())
print("-----------------")
print(data.info())
print("---------mode of catagorical--------")
print(data["species"].mode())
