import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import framework_tools as ft
import setup


class TestFrameworkTools(TestCase):

    def test_get_prediction_type_regression(self):
        ml_type = ft.get_prediction_type(setup.get_datasets_path(), "winequality-red.csv", ";")
        self.assertEqual(ml_type, "regression", "Type should be regression.")

    def test_get_prediction_type_classification(self):
        ml_type = ft.get_prediction_type(setup.get_datasets_path(), "titanic_train.csv", ";")
        self.assertEqual(ml_type, "classification", "Type should be classification.")
