import sys
import csv

import numpy as np
import pandas as pd
from pandas import read_csv, DataFrame
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

sys.path.insert(0, '../../datasets')

def run_SGDRegressor(path, filename):
    pandas_data = pd.read_csv(path + filename, sep=';')
    numpy_data = pd.DataFrame.as_matrix(pandas_data)

    # Selection of training/target data and scaling of the training data.
    # Scaling is important because if the variables are too different from
    # one another, it can throw off the model.
    # EX: If one variable has an average of 1000, and another has an average
    # of .5, then the model won't be as accurate.
    y = numpy_data[:,11]
    X = numpy_data[:,0:11]
    X = preprocessing.scale(X)

    # Feature Selection, didn't help
    # X = SelectKBest(f_regression, k = 8).fit_transform(X, y)

    # Selecting training and test sets
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2, random_state = 123123)

    # Picking model
    SGD_model = linear_model.SGDRegressor()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    SGD_model.fit(X_train, y_train)

    # Scores the model using the coefficient of determination R^2 of the prediction.
    return SGD_model.score(X_test, y_test)
