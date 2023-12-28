"""
We can also use the individual methods like mean(), median(), unique()
to get this information on a DataFrame or a series.
"""

import pandas as pd

url = "https://raw.githubusercontent.com/dphi-official/Datasets/master/exam_scores.csv"
exam_scores = pd.read_csv(url)

print(exam_scores.mean(numeric_only=True))
print(exam_scores.gender.unique())
print(exam_scores.gender.value_counts())