from __future__ import division # Forcing floating point division
from unittest import TestCase
from modules.DMZ.data_kit import dataset_insight
from modules.DMZ.data_kit import data_io
import path_handler
import numpy as np
import pandas as pd


class TestDatasetInsight(TestCase):

    def setUp(self):
        self.data = data_io.get_data(path_handler.get_datasets_path(), "titanic_train.csv")
        self.data["Nonsense"] = np.nan
        self.data["Filled"] = 1
        self.data = self.data.apply(pd.to_numeric,errors='coerce')

    def standard_pred_type(self, filename, target, goal, message):
        # Arrange
        data = data_io.get_data(path_handler.get_datasets_path(), filename)

        # Act
        ml_type = dataset_insight.get_prediction_type(data[target])

        # Assert
        self.assertEqual(ml_type, goal, msg=message)

    def standard_delim(self, filename, target_delim):
        # Act
        delim = dataset_insight.get_delimiter(path_handler.get_datasets_path() + filename)

        # Assert
        self.assertEqual(delim, target_delim, "Delimiter detected incorrectly.")

    def test_get_prediction_type_regression(self):
        self.standard_pred_type("housing_train.csv", "SalePrice", "regression", "Type should be regression.")

    def test_get_prediction_type_classification(self):
        self.standard_pred_type("winequality-red.csv", "quality", "classification", "Type should be classification.")

    def test_get_delim_comma(self):
        self.standard_delim("housing_train.csv", ",")

    def test_get_delim_semicolon(self):
        self.standard_delim("winequality-red.csv", ";")

    def test_get_missing_ratios_col(self):
        # Act
        ratios = (dataset_insight.get_missing_ratios(self.data, "column"))
        ratios_dict = dict(zip(self.data.columns.values, ratios))

        # Assert
        self.assertTrue(ratios_dict["Nonsense"] == 1 and ratios_dict["Filled"] == 0, msg="Calculation failed!")

    def test_get_missing_ratios_row(self):

        # Arrange
        self.data.loc[self.data.shape[0]] = [np.nan] * self.data.shape[1]
        self.data.loc[self.data.shape[0]] = [7] * self.data.shape[1]

        # Act
        ratios = (dataset_insight.get_missing_ratios(self.data, "row"))
        ratios_dict = dict(zip(range(0, self.data.shape[0]), ratios))

        # Assert
        self.assertTrue(ratios_dict[self.data.shape[0]-1] == 0 and ratios_dict[self.data.shape[0]-2] == 1, msg="Calculation failed!")
