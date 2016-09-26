import sys
import os
sys.path.insert(0, os.path.abspath(''))

from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners
import setup

# This is the "starting point" for the framework.
# Functions
# - Check against training data
# - Train and run against test data


# Gets potential results for training data when run against common
# algorithms.
# training_file_name : name of the file including extension.
# prediction_type : "classification" vs "regression", standard is auto-select
def get_potential_results(training_file_name, separator, prediction_type = "auto"):

    if prediction_type == "auto":
        prediction_type = ft.get_prediction_type(setup.get_datasets_path(), training_file_name, separator)

    if prediction_type == "regression":
        ml_runners.run_regressions(setup.get_datasets_path(), training_file_name, separator)


def main():
    type = raw_input("'train' or 'test': ")
    training_file_name = raw_input("Provide the file name: ")
    separator_type = raw_input("Provide the separator for the data file: ")
    prediction_type = raw_input("Type of prediction being done, auto, regression, or classification: ")

    if type == "train":
        get_potential_results(training_file_name, separator_type, prediction_type)
    else:
        return # for applying on testing data, will need to both train the models and apply the trained models.


main()