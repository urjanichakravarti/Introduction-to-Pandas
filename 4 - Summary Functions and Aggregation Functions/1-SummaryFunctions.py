"""
Pandas has many simple "summary functions" that help you to restructure your data
in a very useful way and displays useful information about the data.

Ex: dataset.info()
"""
import pandas as pd

url = "https://raw.githubusercontent.com/dphi-official/Datasets/master/exam_scores.csv"
exam_scores = pd.read_csv(url)

print("------> describe()", "\n")
# By default, the describe() method returns a summary of numerical columns only
# If we want to get a summary of categorical columns separately, then we can use the parameter 'include'.
# Also, we can get a summary of numerical and categorical columns together using the same parameter 'include'.
print(exam_scores.describe(), "\n")
print(exam_scores.describe(include=object), "\n")
print(exam_scores.describe(include='all'))

"""
count - the count of non-null entries in the particular column. For example, gender column has 1000 non-null entries.
unique - the count of unique values in a column. Only for categorical columns. For example, gender column has 2 unique values - male and female.
top - this is also for only categorical columns. This tells us which category is occurring maximum number of times. For example in gender column 'female' is occurring maximum number of times.
freq - this is again for categorical columns only. This tells you the number of occurrences of the top category in that column. For example, 'female' in gender column is occurring 502 times.
mean - the mean value of the numerical column. For example, the mean math score is 67.128.
std - this is the standard deviation of the numerical column. This tells you about the variation in the data. Don't worry if you don't know about it.
min - the minimum value in the numerical column. For example, the minimum math score is 15.0
25% - the 25th percentile (or 1st quartile) value in the numerical column. For example, the 25th percentile value for math score is 58.0.
50% - the 50th percentile (or 2nd quartile or the median) value in the numerical column. For example, the median math score is 67.0.
75% - the 75th percentile (or 3rd quartile) value in the numerical column. For example, the 75th percentile value for math score is 78.0.
max - the maximum value in the numerical column. For example, the maximum math score is 100.0.
NaN values means that for a particular column, a particular summary value is not available. For example, gender (a categorical column), does not have mean value or median value as these are the properties of a numerical column only
"""