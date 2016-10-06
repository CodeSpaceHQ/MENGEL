# This file has functions which call different machine learning algorithms and handle results.
import sys
import os
sys.path.insert(0, os.path.abspath('../..'))

from modules.ml_models import scikit_regression_learners
from validation_package import ValidationPackage
import setup
from modules.toolbox import framework_tools as ft


# Automatically gets all regression models and runs them. This is brute force, more elegant solution to follow later.
def run_regressions(package):
    validation_pack = ValidationPackage()
    validation_pack.setup_package(package)

    for function in dir(scikit_regression_learners):
        item = getattr(scikit_regression_learners, function)
        if callable(item):
            model = item(validation_pack, package)
            print(model_use(model, validation_pack, package))


# TODO: Finish this runner or build it into an overall runner
def run_classifications():
    return


def model_use(model, validation_pack, data_pack):
    model = model.fit(validation_pack.x_train, validation_pack.y_train)

    if data_pack.output_style == "train":
        return model.score(validation_pack.x_test, validation_pack.y_test)
    elif data_pack.output_style == "test":
        predictions = model.predict(model, data_pack)
        ft.save_predictions(setup.get_datasets_path(), predictions, "random_forest")