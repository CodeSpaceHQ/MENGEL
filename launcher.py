import sys
import os
sys.path.insert(0, os.path.abspath(''))

from modules.toolbox import ml_runners
from modules.toolbox import data_package
from modules.toolbox import validation_package

# This is the "starting point" for the framework.
# Functions
# - Check against training data
# - Train and run against test data


# Gets potential results for training data when run against common
# algorithms.
# training_file_name : name of the file including extension.
# prediction_type : "classification" vs "regression", standard is auto-select
def run_framework(validation_pack, package, prediction_type):
    if prediction_type == "regression":
        results = ml_runners.run_regressions(validation_pack, package)
    else:
        return # I need to add classification

    for val in results:
        print(val)


def pre_ml_setup():

    # Getting parameters before running.
    run_type = raw_input("'train' or 'test': ")
    training_file_name = raw_input("Provide the file name: ")
    separator_type = raw_input("Provide the separator for the data file: ")
    prediction_type = raw_input("Type of prediction being done, auto, regression, or classification: ")
    target_col = raw_input("Which column should be predicted? Provide the name: ")

    # Setting up data
    package = data_package.DataPackage()
    package.set_output_style(run_type)
    validation_pack = validation_package.ValidationPackage()
    validation_pack.split_file(training_file_name, target_col)

    if package.output_style == "invalid":
        print("Must input either 'train' or 'test' as output style.")
        return

    # Getting the type of algorithm that should be run against the data
    if prediction_type != "regression" and prediction_type != "classification":
        print("Please input a type of prediction to be doing")
        return

    run_framework(validation_pack, package, prediction_type)

pre_ml_setup()
