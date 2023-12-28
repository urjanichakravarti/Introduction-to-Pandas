import pandas as pd

url = 'https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv'
sma_data = pd.read_csv(url)

print("Question 1")
# Sort the dataframe by crime rate in descending order.

print(sma_data.columns)

print(sma_data.sort_values(by = 'crime_rate', ascending=False))