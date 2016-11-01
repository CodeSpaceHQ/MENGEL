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
