# This is for analyzing columns or datasets, to figure out how to best act upon them.
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
import csv
import pandas as pd
from utils import toggle

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
    axis_toggle = toggle.get_axis_toggle(method)

    if axis_toggle != 2:

        missing_data_counts = pandas_data.isnull().sum(axis_toggle)
        ratios = []

        for i in range(0, pandas_data.shape[not axis_toggle]):
            ratio = float(missing_data_counts[i]) / pandas_data.shape[axis_toggle]
            ratios.append(ratio)
        return ratios

    return pandas_data


# Takes a dataframe and returns the ratio of missing data for each and dtypes for each column.
def get_composition(pandas_data):
    column_types = pandas_data.dtypes
    return missing_ratios, column_types

