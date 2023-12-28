import pandas as pd

url = "https://raw.githubusercontent.com/dphi-official/Datasets/master/exam_scores.csv"
exam_scores = pd.read_csv(url)

pd.set_option('display.width', 320)
pd.set_option('display.max_columns',10)
print(exam_scores.sort_values(by = 'math score').head(10), "\n")
print(exam_scores.sort_values(by = 'math score', ascending=False).head(10))