import pandas as pd
data = [[1000, "Steve", 86.29], [1001, "Ron", 75.69], [1002, "Rebekah", 98.67], [1003, "Matthew", 83.2]]
df = pd.DataFrame(data, columns=["Reg.No", "Names", "Marks"])

df.Names = "Elijah"
print(df)

df[df.Marks == 83.20] = 84.20
print(df)

