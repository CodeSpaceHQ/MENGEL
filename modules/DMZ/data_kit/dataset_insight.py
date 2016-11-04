# This is for analyzing columns or datasets, to figure out how to best act upon them.

import csv
import pandas as pd

# This will take the target "predicted" column and decide if classification or regression should be used.
def get_prediction_type(target_column):
    sorted_data = sorted(target_column)

    prediction_type = "classification"

    last = 0

    for val in sorted_data:
        if not isinstance(val, (int, float)):
            prediction_type = "invalid"
        if not last:
            last = val
        else:
            if last == val - 1:
                last = val
            elif last != val:
                prediction_type = "regression"
                break

    return prediction_type


# Gets the delimiter of the data that is targeted by the file path.
def get_delimiter(path):
    with open(path, 'rb') as csvfile:
        return csv.Sniffer().sniff(csvfile.read(), delimiters=';,').delimiter


# Gets the ratio of missing values to existing values in a dataframe. Either operates on rows or columns, depending
# on input.
def get_missing_ratios(pandas_data, method):

    if method == "column":
        missing_data_counts = pandas_data.isnull().sum(axis=0)
        shape_axis = 1
        index_axis = 0
    elif method == "row":
        missing_data_counts = pandas_data.isnull().sum(axis=1)
        shape_axis = 0
        index_axis = 1
    else:
        print("Please input row or column.")
        return pandas_data
    ratios = []
    for i in range(0, pandas_data.shape[shape_axis]):
        ratio = float(missing_data_counts[i]) / pandas_data.shape[index_axis]
        ratios.append(ratio)
    return ratios


# Takes a dataframe and returns the ratio of missing data for each column and the dtypes for each column.
def get_composition(pandas_data):
    missing_ratios = get_missing_ratios(pandas_data)
    column_types = pandas_data.dtypes
    return missing_ratios, column_types

