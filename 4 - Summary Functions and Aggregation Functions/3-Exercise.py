import pandas as pd

url = 'https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv'
sma_data = pd.read_csv(url)

print(sma_data.head())

print("\n")
print("Question 1", "\n")
"""
Use mean() method on the dataframe sma_data and select the correct statements:
The mean of the column land_area is in the range 2615 to 2616
The mean of the column income is in the range6762 to 6763
Both are correct
None of the above are correct
"""

print(sma_data.columns)
print(sma_data['land_area'].mean())
print(sma_data['income'].mean())


print("\n")
print("Question 2", "\n")
#Use unique() for the column region. How many unique values are there in this column?
print(sma_data.region.unique())


print("\n")
print("Question 3", "\n")
"""
Select the correct statement about the sma_data. [Hint: Summary function - describe()][Note: For us (humans) 769.0 and 769 are same]
The minimum income is 769.0
The maximum crime rate is 85.62
The median land area is 1951.0
There are 99 non-null values in work_force column
All of the above are correct
"""

print(sma_data.income.describe())
print(sma_data['crime_rate'].describe())
print(sma_data['land_area'].median())
print(sma_data['work_force'].isna().count())

print("\n")
print("Question 4", "\n")
"""
Select the observations from the dataframe sma_data where the region is equal to 3. 
Name this selected data as sample_data1. select the correct options about sample_data1.
"""
sample_data1 = sma_data[sma_data['region']==3]
print(sample_data1.shape)
print(sample_data1.mean(numeric_only=True))
print(sma_data['graduates'].isna().count())


print("\n")
print("Question 5", "\n")
"""
Count the occurence of unique values in the column region of the dataframe sma_data. Select the correct statements. [Hint: value_counts()]

The maximum occurring region is 3
The minimum occurring region is 2
The region 4 is occurring 17 times
Both 1 and 3 are correct
Both 1 and 2 are correct
"""

print(sma_data.region.value_counts())

