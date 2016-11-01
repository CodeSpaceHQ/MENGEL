import pandas as pd
import numpy as np
from sklearn import preprocessing

# Takes a given column of a pandas dataframe and returns the column with all
# text values changed to categorical numeric values
def text_column_to_numeric(column):
    le=preprocessing.LabelEncoder()
    le.fit(column)
    column = le.transform(column)
    return column

def convert_dataframe(pandas_data, n):
    #For every column, check if the column is text. If so, and it has fewer than n unique values, convert it.
    for column in pandas_data:
        if(pandas_data[column].dtype == object):
            uniques = set(pandas_data[column])
            if(len(uniques) < n):
                pandas_data[column] = text_column_to_numeric(pandas_data[column])
    return pandas_data





x = pd.read_csv("titanic_train.csv", sep = ',')
print(x)

x = convert_dataframe(x,10)
#print(x)
# le=preprocessing.LabelEncoder()
# le.fit(x["Sex"])
# x["Sex"] = le.transform(x["Sex"])
# print(x)