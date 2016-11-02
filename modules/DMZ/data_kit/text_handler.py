import pandas as pd
import numpy as np
from sklearn import preprocessing


# http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html
# Takes a pandas dataframe column and converts all values to categorical numeric values.
# If given a column of nontext values, it will return the passed column unaltered.
def text_column_to_numeric(col):
    if(col.dtype == object):
        le = preprocessing.LabelEncoder()
        col = le.fit_transform(col)
    return col


# Iterates over every column of the given dataframe and checks if the column contains text. If so, and if it has fewer
# than n unique values, the column will be converted to categorical numeric values.
def convert_dataframe_text(pandas_data, desired_ratio):
    length = pandas_data.shape[0]
    for column in pandas_data:
        if pandas_data[column].dtype == object:
            uniques = set(pandas_data[column])
            ratio = len(uniques) / float(length) #The closer this value is to 0, the fewer unique values we have
            if ratio <= desired_ratio:
                pandas_data[column] = text_column_to_numeric(pandas_data[column])
    return pandas_data


# Converts text columns left over from convert_dataframe to numpy nans for later removal
def convert_nonpredictive_text(pandas_data):
    pandas_data = pandas_data.apply(pd.to_numeric, errors='coerce')
    return pandas_data

