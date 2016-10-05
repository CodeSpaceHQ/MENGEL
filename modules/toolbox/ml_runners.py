# This file has functions which call different machine learning algorithms and handle results.
import sys
import os
sys.path.insert(0, os.path.abspath('../..'))

from modules.toolbox import framework_tools as ft, scikit_regression_learners, setup


# Automatically gets all regression models and runs them. This is brute force, more elegant solution to follow later.
def run_regressions(package):
    x_train, x_test, y_train, y_test = ft.get_train_test(package.train_data, package.target_column)

    for function in dir(scikit_regression_learners):
        item = getattr(scikit_regression_learners, function)
        if callable(item):
            model = item(x_train, y_train) # Todo: Look into the possibility of spawning threads

            if package.output_style == "train":
                model_score(model, x_test, y_test)
            elif package.output_style == "test":
                predictions = model_predict(model, package)
                ft.save_predictions(setup.get_datasets_path(), predictions, function.__name__)


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