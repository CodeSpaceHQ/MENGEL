import pandas as pd
from sklearn import cross_validation
import data_prepping
import numpy as np


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
    x = data_prepping.scale_numeric_data(x)

    # Selection of training/target data for validation and training.
    target_loc = pandas_data.columns.get_loc(target_col)
    data = pd.DataFrame.as_matrix(pandas_data)
    y = data[:, target_loc]
    x = pd.DataFrame.as_matrix(x)

    # Selecting training and test sets
    return cross_validation.train_test_split(x, y, test_size=0.2)


# Removes the target column from the input data.
def separate_target(pandas_data, target_col):
    # Selection of training/target data for validation and training.
    data = pd.DataFrame.as_matrix(pandas_data)
    target_loc = pandas_data.columns.get_loc(target_col)
    y = data[:, target_loc]

    x = pandas_data.drop(target_col, 1)
    x = pd.DataFrame.as_matrix(x)

    return x, y
