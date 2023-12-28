import pandas as pd

#Exercise
sma_data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv")
print(sma_data.head())
print("Question 1")
#Use the index-based selection technique to select the 10th observation from data frame sma_data. What is the crime_rate for this observation?
# [Remember indexing in Python starts with 0, so if you have to select nth observation, you should get the observation present at index n-1]

print(sma_data.columns)
print("Answer 1 - ", sma_data.iloc[9, 9])

print("\n")
print("Question 2")
#Select the physicians column. Get the last value from physicians column.
print(sma_data.shape)
print("Answer 2 - ", sma_data.loc[98, 'physicians'])

print(sma_data.physicians.tail())

print("\n")
print("Question 3")
# Select the records with index labels (numerical positions) - 1, 3, 5, 7, 9 and 13 and
# columns -  'land_area', 'work_force', 'income', 'region' and 'crime_rate'.
# Assign the result to a variable sample_data1.
# Select the correct statement about this sample_data1.
# [Hint: Use label-based selection technique]

sample_data1 = sma_data.loc[[1,3,5,7,9,13], ['land_area', 'work_force', 'income', 'region', 'crime_rate']]
print(sample_data1)

print("\n")
print("Question 4")
# Select the observations for which the region is equal to 2.
# Assign the result to a variable sample_data2.
# How many observations are there in the dataframe sample_data2?
# [Hint: sma_data.region is equal to?]

sample_data2 = sma_data[sma_data['region']==2]
print(sample_data2)
print(sample_data2.shape)
print(sample_data2.region)