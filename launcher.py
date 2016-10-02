import sys
import os
sys.path.insert(0, os.path.abspath(''))

from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners
from modules.toolbox import data_package

# This is the "starting point" for the framework.
# Functions
# - Check against training data
# - Train and run against test data


# Gets potential results for training data when run against common
# algorithms.
# training_file_name : name of the file including extension.
# prediction_type : "classification" vs "regression", standard is auto-select
def run_framework(package, prediction_type):
    if prediction_type == "regression":
        ml_runners.run_regressions(package)
    else:
        return # I need to add classification


def pre_ml_setup():

    # Getting parameters before running.
    run_type = raw_input("'train' or 'test': ")
    training_file_name = raw_input("Provide the file name: ")
    separator_type = raw_input("Provide the separator for the data file: ")
    prediction_type = raw_input("Type of prediction being done, auto, regression, or classification: ")

    # Setting up data
    package = data_package.DataPackage()
    package.setup_training_data(training_file_name, separator_type)
    package.set_output_style(run_type)

    if package.output_style == "invalid":
        return

    # Getting the type of algorithm that should be run against the data
    if prediction_type == "auto":
        prediction_type = ft.get_prediction_type(package.train_data[package.target_column])

    run_framework(package, prediction_type)



pre_ml_setup()