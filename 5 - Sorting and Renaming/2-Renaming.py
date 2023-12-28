import pandas as pd

url = "https://raw.githubusercontent.com/dphi-official/Datasets/master/exam_scores.csv"
exam_scores = pd.read_csv(url)

print(exam_scores.columns)

exam_scores.rename(columns = {'race/ethnicity':'race', 'parental level of education': 'parentEducation'}, inplace=True)
print(exam_scores.columns)

print(exam_scores.rename(index = {0: "zero", 1: "one", 2:"two"}).head())