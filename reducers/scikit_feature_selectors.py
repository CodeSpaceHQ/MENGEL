import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import numpy
from modules.toolbox import framework_tools as ft
import setup
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectPercentile

#http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html
def VarianceThreshold_selector(data):

    #Select Model
    selector = VarianceThreshold(0) #Defaults to 0.0, e.g. only remove features with the same value in all samples

    #Fit the Model
    selector.fit(data)
    features = selector.get_support(indices = True) #returns an array of integers corresponding to nonremoved features
    features = [column for column in data[features]] #Array of all nonremoved features' names

    #Format and Return
    selector = pd.DataFrame(selector.transform(data))
    selector.columns = features
    return selector


def SelectPercentile_selector(data):
    x_train, x_test, y_train, y_test = ft.get_train_test(data, "Survived")

    #Select Model
    selector = SelectPercentile(percentile = 75) #Default is 10%

    #Fit the model
    selector.fit(x_train, y_train)
    features = selector.get_support(indices=True)
    features = [column for column in data[features]]
    print(features)

    #Format and Return
    selector = selector.transform(data)
    # selector.columns = features
    return selector

data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
x = SelectPercentile_selector(data)
print(x)