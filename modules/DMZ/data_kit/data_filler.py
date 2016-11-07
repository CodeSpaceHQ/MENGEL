import pandas as pd
import numpy as np
import dataset_insight


# Drops rows which have a missing to existing component ratio greater than the desired_ratio.
# e.g. if desired_Ratio is .5, and a row is missing 60% of its components, the row will be dropped.
def drop_missing_data_rows(pandas_data, desired_ratio):
    ratios = dataset_insight.get_missing_ratios(pandas_data, "row")
    ratios_dict = dict(zip(range(0, pandas_data.shape[0]), ratios))
    for i in range(0, len(ratios)):
        if ratios_dict[i] > desired_ratio:
            pandas_data = pandas_data.drop(i, 0)
    return pandas_data


# Drops columns which have a missing to existing component ratio greater than the desired_ratio.
# e.g. if desired_ratio is .5, and a column is missing 60% of its components, the column will be dropped.
def drop_missing_data_columns(pandas_data, desired_ratio):
    ratios = dataset_insight.get_missing_ratios(pandas_data, "column")
    ratios_dict = dict(zip(pandas_data.columns.values, ratios))
    for col in pandas_data:
        if ratios_dict[col] > desired_ratio:
            pandas_data = pandas_data.drop(col, 1)
    return pandas_data


# Drop rows in which every single component is NaN
def drop_all_missing_data_rows(pandas_data):
    pandas_data = pandas_data.dropna(how='all')
    return pandas_data


# Drop columns in which every single component is NaN
def drop_all_missing_data_columns(pandas_data):
    pandas_data = pandas_data.dropna(axis=1, how='all')
    return pandas_data


# Will replace all "NaN"s within pandas_data with filler.
# e.g. if filler = 0, all NaNs will be replaced with 0s.
def fill_missing_data(pandas_data, filler):
    pandas_data = pandas_data.fillna(filler)
    return pandas_data

def fill_missing_data_average(pandas_data):
    pandas_data.fillna(pandas_data.mean(), inplace=True)
    return pandas_data

# # Will replace all "NaN"s with the average value for the column
# def fill_missing_data_average(pandas_data):
#     #features = pandas_data.columns.values
#     #for feature in features:
#     pandas_data[feature].fillna(pandas_data[feature].mean(), inplace=True)
#     return pandas_data
