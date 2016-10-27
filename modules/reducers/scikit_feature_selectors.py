import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from modules.DMZ.data_kit import data_io
from modules.DMZ.data_kit import data_splitting
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import SelectKBest


# Stores nonremoved feature names, transforms data, and returns formatted selector
def format_selector(selector,data, target):
    x_train, x_test, y_train, y_test = data_splitting.get_train_test(data, target)

    # Fit the model
    data.drop(target, 1, inplace=True)  # Remove target feature
    selector.fit(x_train, y_train)

    # Retain the feature names
    features = selector.get_support(indices = True)  # Returns array of indexes of nonremoved features
    features = [column for column in data[features] if column != target]  # Gets feature names

    # Transform, Format, Return
    selector = pd.DataFrame(selector.transform(data))
    selector.columns = features
    return selector


# http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html
def variance_threshold_selector(data,target):

    # Select Model
    selector = VarianceThreshold(0)  # Defaults to 0.0, e.g. only remove features with the same value in all samples

    # Fit, Format, and Return
    return format_selector(selector,data,target)


# http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html
def select_percentile_selector(data,target):

    # Select Model
    selector = SelectPercentile(percentile = 75)  # Default is 10%

    # Fit, Format, and Return
    return format_selector(selector, data, target)


# http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html
def select_k_best_selector(data,target):

    # Select Model
    selector = SelectKBest(k=3)  # default is 10 features

    # Fit, Format, and Return
    return format_selector(selector, data, target)


