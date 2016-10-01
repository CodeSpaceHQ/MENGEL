# This file has functions which call different machine learning algorithms and handle results.
import sys
import os
sys.path.insert(0, os.path.abspath('../..'))

from modules.ml_models import scikit_online_regressors
from modules.ml_models import scikit_regression_learners
from modules.toolbox import *



# Automatically gets all regression models and runs them. This is brute force, more elegant solution to follow later.
def run_regressions(data, target_col):
    x_train, x_test, y_train, y_test = ft.get_train_test(data, target_col)
    model = None

    for function in dir(scikit_regression_learners):
        item = getattr(scikit_regression_learners, function)
        if callable(item):
            model = item(x_train, y_train)

    return model_score(model, x_test, y_test)


# TODO: Finish this runner or build it into an overall runner
def run_classifications():
    return


# In case we want to change the scoring method down the road, this is a easy way to standardize that system.
def model_score(model, x_test, y_test):
    # Scores the model using the coefficient of determination R^2 of the prediction.
    return model.score(x_test, y_test)


#