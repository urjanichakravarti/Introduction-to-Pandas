import pandas as pd

cars = pd.read_csv("mtcars.csv")
print(cars)

#Converting mpg column to strings
# cars.mpg = cars.mpg.astype(str)

#visualising top/bottom rows
print(cars.head())
print(cars.tail())

#shape of a dataset
print(cars.shape)

#arithmetic
# print(cars.mean())
# print(cars.median())
# print(cars.std())
# print(cars.max())
# print(cars.min())
# print(cars.count())
print(cars.describe())

#exporting to csv:
"""
--- Using the "to_csv" function
df.to_csv("filename.csv")

--- if you want to export without index: add attribute index = False
df.to_csv("filename.csv", index=False)
"""