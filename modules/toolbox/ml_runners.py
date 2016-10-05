# This file has functions which call different machine learning algorithms and handle results.
import sys
import os
sys.path.insert(0, os.path.abspath('../..'))

from modules.toolbox import scikit_regression_learners, setup
from validation_package import ValidationPackage


# Automatically gets all regression models and runs them. This is brute force, more elegant solution to follow later.
def run_regressions(package):
    validation_pack = ValidationPackage()
    validation_pack.setup_package(package)

    for function in dir(scikit_regression_learners):
        item = getattr(scikit_regression_learners, function)
        if callable(item):
            print(item(validation_pack, package)) # Todo: Look into the possibility of spawning threads


# TODO: Finish this runner or build it into an overall runner
def run_classifications():
    return


# In case we want to change the scoring method down the road, this is a easy way to standardize that system.
def model_score(model, x_test, y_test):
    # Scores the model using the coefficient of determination R^2 of the prediction.
    return model.score(x_test, y_test) # Todo: should send to logger instead


# Applies the trained model to test data and saves results
def model_predict(model, package):
    return model.predict(package.test_data)