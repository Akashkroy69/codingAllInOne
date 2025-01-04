import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


data = sns.load_dataset("titanic")

print(data.dtypes)
print("-----------------")
print(data)
print("-----------------")
print(data.describe())
print("-----------------")
print(data.info())
print("-----------------")
print(data["deck"].mode())
print("--------is Null---------")
print(data.isnull().sum())