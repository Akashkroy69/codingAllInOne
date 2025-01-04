import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
ageData = [
    11, 11, 11, 12, 12, 12, 14, 14, 14, 9, 9, 9, 16, 16, 16, 16, 30, 30, 30,
    30, 56, 67, 67, 67, 67, 67, 78, 78, 78, 90, 90
]
print(ageData)
ageData.sort()
print(ageData," \nlength : ",len(ageData))

firstQuartile = (len(ageData)+1)/4
print("first quartile element: ",firstQuartile)

secondQuartile = ((len(ageData)+1)/4)*2
print("second quartile element: ",secondQuartile)

thirdQuartile = ((len(ageData)+1)/4)*3
print("third quartile element: ",thirdQuartile)


print("------using numpy.quantile()----------")
firstQuartileNp = np.quantile(ageData,0.25)
print("manual first quartile: ",firstQuartileNp,"th element")
secondQuartileNp = np.quantile(ageData,0.50)   # # or np.median(ageData)
print("manual first quartile: ",secondQuartileNp,"th element")
thirdQuartileNp = np.quantile(ageData,0.75)
print("manual first quartile: ",thirdQuartileNp,"th element")

print("------using pandas quantile()----------")

age_series = pd.Series(ageData)

Q1 = age_series.quantile(0.25)
Q2 = age_series.quantile(0.5)
Q3 = age_series.quantile(0.75)
print("pandas quartiles: ",Q1,Q2,Q3)

plt.boxplot(ageData)
plt.show()