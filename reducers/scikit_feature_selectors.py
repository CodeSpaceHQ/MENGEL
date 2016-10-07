import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import numpy
from modules.toolbox import framework_tools as ft
import setup
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import SelectKBest


# Stores nonremoved feature names, transforms data, and returns formatted selector
def format_selector(selector,data, target):
    data.drop(target, 1, inplace=True)  # Remove target feature
    features = selector.get_support(indices = True)  # Returns array of indexes of nonremoved features
    features = [column for column in data[features] if column != target]  # Gets feature names
    selector = pd.DataFrame(selector.transform(data))
    selector.columns = features
    return selector


# http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html
def variance_threshold_selector(data,target):
    x_train, x_test, y_train, y_test = ft.get_train_test(data, target)

    # Select Model
    selector = VarianceThreshold(0)  # Defaults to 0.0, e.g. only remove features with the same value in all samples

    # Fit the Model
    selector.fit(x_train, y_train)

    # Format and Return
    selector = format_selector(selector,data,target)
    return selector


# http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html
def select_percentile_selector(data,target):
    x_train, x_test, y_train, y_test = ft.get_train_test(data, target)

    # Select Model
    selector = SelectPercentile(percentile = 75)  # Default is 10%

    # Fit the Model
    selector.fit(x_train, y_train)

    # Format and Return
    selector = format_selector(selector, data, target)
    return selector


# http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html
def select_k_best_selector(data,target):
    x_train, x_test, y_train, y_test = ft.get_train_test(data, target)

    # Select Model
    selector = SelectKBest(k=3)  # default is 10 features

    # Fit the Model
    selector.fit(x_train, y_train)

    # Format and Return
    selector = format_selector(selector, data, target)
    return selector
