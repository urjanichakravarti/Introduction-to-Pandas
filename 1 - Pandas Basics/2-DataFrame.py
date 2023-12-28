"""
Data Frames are multidimensional data structures with columns of different types
Features:
1. Diff column types
2. Mutable Size
3. Labeled Axis
3. Arithmetic Operations on Rows and Columns

* A single column in a Dataframe is called a series; a dataframe is a collection of series
"""

import pandas as pd

data = [[1,2,3,4,5], [1,2,3]]
df = pd.DataFrame(data)
print(df)

#must be same length when we use dictionaries
data2 = {"a":[1,2,3,4,5], "b": [1,5,7,9,10]}
df2 = pd.DataFrame(data2)
print(df2)

#Concating dataframes
a = [[1,2,3,4,5] , [1,2,3,4], [1,2]]
b = [[2,3,4], [5,6,7,8], [4]]
data1 = pd.DataFrame(a)
print("Data 1")
print(data1)
data2 = pd.DataFrame(b)
print("Data 2")
print(data2)
print("Data Concat")
dataFinal = pd.concat([data1, data2])
print(dataFinal)

data = [[1000, "Steve", 86.29], [1001, "Ron", 75.69], [1002, "Rebekah", 98.67], [1003, "Matthew", 83.2]]
df = pd.DataFrame(data, columns=["Reg.No", "Name", "Marks"])
print(df)

data = {"Reg.No": [1000, 1001, 1002, 1003], "Name": ["Steve", "Ron", "Rebekah", "Matthew"], "Marks": [86.29, 75.69, 98.67, 83.2]}
df = pd.DataFrame(data)
print(df)