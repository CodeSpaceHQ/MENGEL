import sys
import os
sys.path.insert(0, os.path.abspath(''))

from modules.toolbox import framework_tools as ft
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

    if prediction_type != "auto":
        prediction_type = ft.get_prediction_type(setup.get_datasets_path(), training_file_name, separator)
