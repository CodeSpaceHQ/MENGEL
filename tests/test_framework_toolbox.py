from __future__ import division # Forcing floating point division
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.DMZ.data_kit import data_splitting
from modules.DMZ.data_kit import data_analysis
from modules.DMZ.data_kit import data_io
import setup
import pandas as pd


class TestFrameworkTools(TestCase):

    def test_get_prediction_type_regression(self):

        # Arrange
        data = data_io.get_data(setup.get_datasets_path(), "housing_train.csv")

        # Act
        ml_type = data_analysis.get_prediction_type(data["SalePrice"])

        # Assert
        self.assertEqual(ml_type, "regression", "Type should be regression.")

    def test_get_prediction_type_classification(self):

        # Arrange
        data = data_io.get_data(setup.get_datasets_path(), "winequality-red.csv")

        # Act
        ml_type = data_analysis.get_prediction_type(data["quality"])

        # Assert
        self.assertEqual(ml_type, "classification", "Type should be classification.")

    def test_data_split(self):

        # Arrange
        data = data_io.get_data(setup.get_datasets_path(), "winequality-red.csv")

        # Act
        x_train, x_test, y_train, y_test = data_splitting.get_train_test(data, "quality")

        # Assert
        self.assertEqual(len(x_train[:, 0]), len(y_train))
        self.assertEqual(len(x_test[:, 0]), len(y_test))
        self.assertAlmostEqual(len(y_train)/len(y_test), 4, 2)

    def test_scaling(self):

        # Arrange
        data = data_io.get_data(setup.get_datasets_path(), "winequality-red.csv")

        # Act
        target = data_splitting.scale_numeric_data(data)
        target = pd.DataFrame.as_matrix(target)

        # Assert
        self.assertAlmostEqual(target.mean(), 0, 5)
        self.assertAlmostEqual(target.std(), 1, 5)
