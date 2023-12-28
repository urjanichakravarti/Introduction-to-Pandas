import pandas as pd

df = pd.DataFrame({"A": [1,2,3], "B": [3,4,5]})
df2 = pd.DataFrame({"A": [3,4,5], "C": [3,7,8]})

print("Data Frame 1")
print(df)
print("Data Frame 2")
print(df2)

print("Data Frame Concatenation")
concatDf = pd.concat([df, df2])
print(concatDf)

print("Inner Concat: common columns")
innerConcat = pd.concat([df, df2], axis=0, join="inner")
print(innerConcat)

print("Inner Merge/Join: common values")
#Returns records that have matching values in both tables
innerMerge = pd.merge(df, df2, on="A", how="inner")
print(innerMerge)

print("Left Merge/Join:")
#Returns all records from the left table, and the matched records from the right table
leftMerge = pd.merge(df, df2, how="left")
print(leftMerge)

print("Right Merge/Join:")
#Returns all records from the right table, and the matched records from the left table
rightMerge = pd.merge(df, df2, how="right")
print(rightMerge)

print("Full/Outer Merge/Join:")
#Returns all records when there is a match in either left or right table
outerMerge = pd.merge(df, df2, how="outer")
print(outerMerge)
