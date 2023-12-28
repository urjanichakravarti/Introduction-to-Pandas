import pandas as pd
data = [[1000, "Steve", 86.29], [1001, "Ron", 75.69], [1002, "Rebekah", 98.67], [1003, "Matthew", 83.2]]
df = pd.DataFrame(data, columns=["Reg.No", "Names", "Marks"])

print("Attribute (Dot) Based Selecting")
#Selecting a Column
print(df.Names, "\n")

print("Dictionary (Bracket) Based Selecting")
#Selecting a Column
print(df['Names'], "\n")

print("Selecting Multiple Columns")
print(df[['Names', 'Marks']], "\n")

print("Conditional Selection")
print(df.Names == "Rebekah", "\n")
print(df[df.Names == "Rebekah"])

print("For Loop")
for row in df.index:
    print(df['Names'])
    print(row)
