import pandas as pd
from sklearn import cross_validation
import data_scaling
import numpy as np


# Leaving as a separate function in case we want to change how this works later.
def random_split(x, y, ratio):
    return cross_validation.train_test_split(x, y, test_size=ratio)


# Gets the training and testing splits for training.
# Input:
# - Pandas Dataframe
# - The target column or "label"
# Output:
# - target_train
# - target_test
# - input_data_train
# - input_data_test
def get_train_test(pandas_data, target_col):

    # Separating target from the rest of the data
    x = pandas_data.drop(target_col, 1)
    x = data_scaling.scale_numeric_data(x)

    # Selection of training/target data for validation and training.
    target_loc = pandas_data.columns.get_loc(target_col)
    data = pd.DataFrame.as_matrix(pandas_data)
    y = data[:, target_loc]
    x = pd.DataFrame.as_matrix(x)

    # Selecting training and test sets
    return cross_validation.train_test_split(x, y, test_size=0.2)


# Removes the target column from the input data.
# Returns two DataFrames.
def separate_target(pandas_data, target_col):
    # Selection of training/target data for validation and training.
    x = pandas_data.drop(target_col, 1)
    y = pandas_data[[target_col]]

    return x, y


# Removes all non-numeric columns from the dataset.
def remove_non_numeric_columns(pandas_data):
    return pandas_data._get_numeric_data()
