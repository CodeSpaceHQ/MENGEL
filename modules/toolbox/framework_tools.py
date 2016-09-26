# Helper functions for the whole framework to use

import pandas as pd
from sklearn import cross_validation
from sklearn import preprocessing


def get_train_test(path, filename, separator):
    numpy_data = get_data(path, filename, separator)

    # Selection of training/target data and scaling of the training data.
    # Scaling is important because if the variables are too different from
    # one another, it can throw off the model.
    # EX: If one variable has an average of 1000, and another has an average
    # of .5, then the model won't be as accurate.
    y = numpy_data[:, numpy_data.shape[1] - 1]
    x = numpy_data[:, 0:numpy_data.shape[1] - 1]
    x = preprocessing.scale(x)

    # Selecting training and test sets
    return cross_validation.train_test_split(x, y, test_size = 0.2)


# works for CSVs, not images. Might want to pass in the target column instead of the file
def get_prediction_type(path, filename, separator):
    numpy_data = get_data(path, filename, separator)

    y = numpy_data[:, numpy_data.shape[1] - 1]

    classification = is_classification(y)
    regression = is_regression(y)

    if not (regression or classification):
        return "invalid"
    elif classification:
        return "classification"
    else:
        return "regression"


def get_data(path, filename, separator):
    pandas_data = pd.read_csv(path + filename, sep=separator)
    return pd.DataFrame.as_matrix(pandas_data)


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
