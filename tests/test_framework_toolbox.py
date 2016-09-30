import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import framework_tools as ft
import setup


class TestFrameworkTools(TestCase):

    def test_get_prediction_type_regression(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "housing_train.csv", ",")

        # Act
        ml_type = ft.get_prediction_type(data["SalePrice"])

        # Assert
        self.assertEqual(ml_type, "regression", "Type should be regression.")

    def test_get_prediction_type_classification(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "winequality-red.csv", ";")

        # Act
        ml_type = ft.get_prediction_type(data["quality"])

        # Assert
        self.assertEqual(ml_type, "classification", "Type should be classification.")
