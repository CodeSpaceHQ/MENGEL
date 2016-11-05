from __future__ import division # Forcing floating point division
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.DMZ.data_kit import dataset_insight
from modules.DMZ.data_kit import data_io
from modules.DMZ.models import model_filter
import setup


class TestDatasetInsight(TestCase):

    def test_get_prediction_type_regression(self):

        # Arrange
        data = data_io.get_data(setup.get_datasets_path(), "housing_train.csv")

        # Act
        ml_type = dataset_insight.get_prediction_type(data["SalePrice"])

        # Assert
        self.assertEqual(ml_type, "regression", "Type should be regression.")

    def test_get_prediction_type_classification(self):

        # Arrange
        data = data_io.get_data(setup.get_datasets_path(), "winequality-red.csv")

        # Act
        ml_type = dataset_insight.get_prediction_type(data["quality"])

        # Assert
        self.assertEqual(ml_type, "classification", "Type should be classification.")

    def test_get_delim_comma(self):

        # Arrange
        file_name = "housing_train.csv"

        # Act
        delim = dataset_insight.get_delimiter(setup.get_datasets_path() + file_name)

        # Assert
        self.assertEqual(delim, ",", "Delimiter detected incorrectly.")

    def test_get_delim_semicolon(self):

        # Arrange
        file_name = "winequality-red.csv"

        # Act
        delim = dataset_insight.get_delimiter(setup.get_datasets_path() + file_name)

        # Assert
        self.assertEqual(delim, ";", "Delimiter detected incorrectly.")

    def test_model_filter(self):

        # Arrange
        pred_type = "regression"
        expected_functions = {"train_passive_aggressive_regressor",
                              "train_support_vector_regression",
                              "train_bayesian_ridge",
                              "train_sgd_regressor"}

        # Act
        model_functions = model_filter.get_models(pred_type)

        # Assert
        for model in model_functions:
            self.assertIn(model.__name__, expected_functions, "Function does not exist as expected")

    def test_get_missing_ratios_col(self):

        # Arrange
        data = self.setup_data()

        #Act
        ratios = (dataset_insight.get_missing_ratios(data, "column"))
        ratios_dict = dict(zip(data.columns.values, ratios))

        #Assert
        self.assertTrue(ratios_dict["Nonsense"] == 1 and ratios_dict["Filled"] == 0, msg= "Calculation failed!")

    def test_get_missing_ratios_row(self):

        # Arrange
        data = self.setup_data()
        data.loc[data.shape[0]] = [np.nan] * data.shape[1]
        data.loc[data.shape[0]] = [7] * data.shape[1]

        #Act
        ratios = (dataset_insight.get_missing_ratios(data, "row"))
        ratios_dict = dict(zip(range(0, data.shape[0]), ratios))

        #Assert
        self.assertTrue(ratios_dict[data.shape[0]-1] == 0 and ratios_dict[data.shape[0]-2] == 1, msg = "Calculation failed!")

    def setup_data(self):
        data = data_io.get_data(setup.get_datasets_path(), "titanic_train.csv")
        data["Nonsense"] = np.nan
        data["Filled"] = 1
        data = data.apply(pd.to_numeric,errors='coerce')
        return data

