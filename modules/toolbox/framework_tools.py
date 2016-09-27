# Helper functions for the whole framework to use

import pandas as pd
from sklearn import cross_validation
from sklearn import preprocessing


def get_train_test(pandas_data, target_col):
    # Selection of training/target data and scaling of the training data.
    # Scaling is important because if the variables are too different from
    # one another, it can throw off the model.
    # EX: If one variable has an average of 1000, and another has an average
    # of .5, then the model won't be as accurate.
    data = pd.DataFrame.as_matrix(pandas_data)
    target_loc = pandas_data.columns.get_loc(target_col)
    y = data[:, target_loc]

    x = pandas_data.drop(target_col, 1)
    x = pd.DataFrame.as_matrix(x)

    x = preprocessing.scale(x)

    # Selecting training and test sets
    return cross_validation.train_test_split(x, y, test_size=0.2)


# works for CSVs, not images. Might want to pass in the target column instead of the file
def get_prediction_type(target_column):
    classification = is_classification(target_column)
    regression = is_regression(target_column)

    if not (regression or classification):
        return "invalid"
    elif classification:
        return "classification"
    else:
        return "regression"


def get_data(path, filename, separator):
    return pd.read_csv(path + filename, sep=separator)
    # return pd.DataFrame.as_matrix(pandas_data)


# not positive that this is a good enough check. TODO: Test thoroughly
def is_classification(data):
    is_class = True
    for value in data:
        if not isinstance(value, int):
            is_class = False

    return is_class


# not positive that this is a good enough check. TODO: Test thoroughly
def is_regression(data):
    is_reg = True
    for value in data:
        if not isinstance(value, (int, float)):
            is_reg = False

    return is_reg
