import pandas as pd

#Example 1
url = "https://raw.githubusercontent.com/dphi-official/Datasets/master/exam_scores.csv"
exam_scores = pd.read_csv(url)

print("Shape of Dataset: ", exam_scores.shape, "\n")
print("First five rows of Dataset: ", "\n",  exam_scores.head(), "\n")
print("Last five rows of Dataset: ", "\n", exam_scores.tail(), "\n")
print("Datatypes of Dataset: ", "\n", exam_scores.dtypes, "\n")
print("Concise info of Dataset: ", "\n", exam_scores.info(), "\n")

#Example 2
url = "https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv"

sma_data = pd.read_csv(url)
print(sma_data.shape)
print(sma_data.dtypes)

