# Helper functions for the whole framework to use

import pandas as pd
from sklearn import cross_validation
from sklearn import preprocessing


def get_train_test(path, filename, separator):
    pandas_data = pd.read_csv(path + filename, sep=separator)
    numpy_data = pd.DataFrame.as_matrix(pandas_data)

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

