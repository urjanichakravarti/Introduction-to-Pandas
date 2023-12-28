import pandas as pd

"""
- Indexing in Pandas means selecting particular rows and columns from a DataFrame.
- Indexing in Pandas is the same as we did for a Python List and a NumPy array.

There are two different methods of indexing in Pandas:
1. loc - label based selection
2. iloc - index-based selection
"""

print("Index Based Selecting - iloc")
"""
---> Index-based selection is to select data based on its numerical position in DataFrame.
---> iloc is used for selecting data based on numerical position.
"""

url = "https://raw.githubusercontent.com/dphi-official/Datasets/master/exam_scores.csv"
exam_scores = pd.read_csv(url)
print(exam_scores.head())
print(exam_scores.iloc[0,0]) #0th row and 0th column
print(exam_scores.iloc[0:5, 4]) #rows 0,1,2,3,4 and column 4
print(exam_scores.iloc[[0,1,2,3], 2]) #rows 0,1,2,3 and 2 same method as above
print(exam_scores.iloc[-5: , 0:2]) #last 5 rows till the end, columns 0 and 1
print(exam_scores.iloc[:,:]) #all rows and columns

print("\n")
print("Label Based Indexing - loc")
print(exam_scores.loc[0, "race/ethnicity"]) #row 0 entry of label race/ethnicity
print(exam_scores.loc[0:2, ["race/ethnicity", "gender", "lunch", "math score"]])