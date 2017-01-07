import os
import sys
sys.path.insert(0, os.path.abspath('../../../..'))


from unittest import TestCase
from modules.DMZ.data_kit import filler_strategy
from modules.DMZ.data_kit import data_io
import path_handler
import pandas as pd
import numpy as np

class TestFillerStrategy(TestCase):

    def setUp(self):
        self.data = data_io.get_data(path_handler.get_datasets_path(), "winequality-red.csv")
        self.strategy = filler_strategy.FillerStrategy(self.data)

    def test_run_fillers_nonsense(self):

        # Arrange
        self.strategy.pandas_dataset["Nonsense"] = np.nan

        # Act
        self.strategy.get_missing_ratios_dict()
        self.strategy.get_to_do_list()
        self.strategy.run_fillers()

        # Assert
        self.assertFalse("Nonsense" in self.strategy.pandas_dataset.columns.values, msg="Failed to remove empty column")

    def test_run_fillers_average(self):
        # Act
        self.strategy.run_fillers()
        self.strategy.get_missing_ratios_dict()

        # Assert
        self.assertTrue(self.strategy.missing_ratios_dict["density"] == 0, msg="Failed to fill empty values")

    def test_run_fillers_value(self):

        # Arrange
        self.strategy.pandas_dataset = self.data
        self.strategy.pandas_dataset.loc[self.data.shape[0]] = np.nan 
        self.strategy.avg_range = [.9,1]
        self.strategy.value_range = [.0, .899]

        # Act
        self.strategy.get_missing_ratios_dict()
        self.strategy.get_to_do_list()
        self.strategy.run_fillers()
        self.strategy.get_missing_ratios_dict()

        # Assert
        verify_has = self.strategy.missing_ratios_dict["density"] == 0
        self.assertTrue(verify_has and any(self.strategy.pandas_dataset["density"] == self.strategy.fill_value),
                        msg="Failed to fill empty values")
