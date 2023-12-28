"""
* 2 data structures in Pandas (Python Data Analysis Library - Srries and Dataframes)

Series objects are one dimensional, ie, 1D labelled arrays
Data can be homogeneous or heterogeneous
"""

import pandas as pd

data = [1,2,3,4,5]
srs = pd.Series(data, index=["a", "b", "c", "d", "e"])
print(srs)
print(type(srs))
print(srs["a":"c"])