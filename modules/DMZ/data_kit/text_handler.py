import pandas as pd
import numpy as np
from sklearn import preprocessing


# http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html
def text_column_to_numeric(col):
    le = preprocessing.LabelEncoder()
    col = le.fit_transform(col)
    return col


# Iterates over every column of the given dataframe and checks if the column contains text. If so, and if it has fewer
# than n unique values, the column will be converted to categorical numeric values.
def convert_dataframe_text(pandas_data, n):
    for column in pandas_data:
        if pandas_data[column].dtype == object:
            uniques = set(pandas_data[column])
            if len(uniques) < n:
                pandas_data[column] = text_column_to_numeric(pandas_data[column])
    return pandas_data


# Converts text columns left over from convert_dataframe to numpy nans for later removal
def convert_nonpredictive_text(pandas_data):
    pandas_data = pandas_data.apply(pd.to_numeric, errors='coerce')
    return pandas_data
