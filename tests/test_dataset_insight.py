import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.DMZ.data_kit import data_io
from modules.DMZ.data_kit import dataset_insight
import setup
import numpy as np
import pandas as pd

from modules.toolbox.data_package import DataPackage
from modules.toolbox.validation_package import ValidationPackage

class TestDataFilling(TestCase):

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
