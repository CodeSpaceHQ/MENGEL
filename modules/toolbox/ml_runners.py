# This file has functions which call different machine learning algorithms and handle results.
import sys
import os
sys.path.insert(0, os.path.abspath('../..'))

from modules.ml_models import scikit_online_regressors
from modules.ml_models import scikit_regression_learners


# Automatically gets all regression models and runs them. This is brute force, more elegant solution to follow later.
def run_regressions(data, target_col):
    for function in dir(scikit_regression_learners):
        item = getattr(scikit_regression_learners, function)
        if callable(item):
            print(item(data, target_col))


def run_classifications():
    return
