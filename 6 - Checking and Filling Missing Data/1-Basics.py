import pandas as pd

data = [[1000, "Steve", 86.29], [1001, "Ron", 75.69], [1002, "Rebekah", 98.67], [1003, "Matthew", 83.2], [1004, "Elijah"], [1005]]
df = pd.DataFrame(data, columns=["Reg.No", "Name", "Marks"])
print(df, "\n")


"""
Pandas provides isnull(), isna() functions to detect missing values. Both of them do the same thing.
df.isna() or df.isnull() returns the DataFrame with Boolean values indicating whether a value is missing (True) or not (False)
"""

print(df.isnull(), "\n")
print(df.isna().sum(), "\n")
print(df.Name.fillna("Klaus"), "\n") #changes are NOT made in original dataset
print(df.Name.fillna("Klaus", inplace=True), "\n") #changes are  made in original dataset
print(df, "\n")

#example
mean = df["Marks"].mean()

df['Marks'].fillna(mean, inplace=True)
print(df, "\n")