import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dphi-official/Datasets/master/titanic_data.csv')

print("Question 1")
#Check if the dataset has any missing values or not.
# If there are any missing values, then which of the following columns are they?

print(df.isna().sum(), "\n")


print("Question 2")
"""
Find the mean value of Age column and assign it to a variable age_mean_before. 
Fill the missing value of the column Age with the mean value i.e. age_mean_before. 
[To calculate mean you can directly use mean() method on the Age column]. 
After filling the missing value of the column Age, find the mean of column Age again and assign it to a variable age_mean_after. 
Select the correct answer.
"""

print(df.columns)
age_mean_before = df.Age.mean()
df.Age.fillna(age_mean_before, inplace=True)
age_mean_after = df.Age.mean()
print("Age Before Mean", age_mean_before)
print("Age After Mean", age_mean_after)


print("\n")
print("Question 2")
"""
Find the maximum occurring value/category in the column Embarked [Hint: value_counts()]. 
Fill the missing value in this column Embarked with the maximum occurring value. 
Select the correct statement.
"""
print("Before - ", df.Embarked.value_counts())

df.Embarked.fillna('S', inplace=True)
print("After - ", df.Embarked.value_counts())
