# This file has functions which call different machine learning algorithms and handle results.
import sys
import os
sys.path.insert(0, os.path.abspath('../..'))

from modules.ml_models import scikit_online_regressors
from modules.ml_models import scikit_regression


# Automatically gets all regression models and runs them. This is brute force, more elegant solution to follow later.
def run_regressions(path, filename, separator):
    for function in dir(scikit_regression):
        item = getattr(scikit_regression, function)
        if callable(item):
            print(item(path, filename, separator))


def run_classifications():
    return
