import pandas as pd
import numpy as np
import dataset_insight


# Drops rows which have fewer than threshold observations.
# e.g. if threshold = 5, any rows with fewer than 5 observations will be removed from pandas_data.
# def drop_missing_data_rows(pandas_data, threshold):
#     pandas_data = pandas_data.dropna(thresh=threshold)
#     return pandas_data
#
# def drop_missing_data_rows(pandas_data, desired_ratio):
#


# Drops columns which have a missing to existing component ratio greater than the desired_ratio.
# e.g. if desired_ratio is .5, and a column is missing 60% of its components, the column will be dropped.
def drop_missing_data_columns(pandas_data, desired_ratio):
    ratios = dataset_insight.get_missing_ratios(pandas_data)
    for i in range(0, len(ratios)):
        if ratios[i] > desired_ratio:
            pandas_data = pandas_data.drop(pandas_data.columns[i], axis=1)

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


# Will replace all "NaN"s with the average value for the column
def fill_missing_data_average(pandas_data):
    features = pandas_data.columns.values
    for feature in features:
        pandas_data[feature].fillna(pandas_data[feature].mean(), inplace=True)

    return pandas_data


x = pd.read_csv("titanic_train.csv", sep=",")
L = dataset_insight.get_missing_ratios_rows(x)
print(L)