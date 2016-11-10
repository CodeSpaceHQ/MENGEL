import os
import sys
sys.path.insert(0, os.path.abspath('../../../..'))


from unittest import TestCase
from modules.DMZ.data_kit import filler_strategy
from modules.DMZ.data_kit import data_io
import setup
import pandas as pd
import numpy as np

class TestFillerStrategy(TestCase):

    def test_run_fillers_nonsense(self):

        # Arrange
        data = filler_strategy.FillerStrategy()
        data.pandas_dataset["Nonsense"] = np.nan

        # Act
        data.get_missing_ratios_dict()
        data.get_to_do_list()
        data.run_fillers()

        # Assert
        self.assertFalse("Nonsense" in data.pandas_dataset.columns.values, msg="Failed to remove empty column")

    def test_run_fillers_average(self):

        # Arrange
        data = filler_strategy.FillerStrategy()

        # Act
        data.run_fillers()
        data.get_missing_ratios_dict()

        # Assert
        self.assertTrue(data.missing_ratios_dict["Age"] == 0, msg="Failed to fill empty values")

    def test_run_fillers_value(self):

        # Arrange
        data = filler_strategy.FillerStrategy()
        data.pandas_dataset = self.setup_data()
        data.avg_range = [0,.10]
        data.value_range = [.10, .20]

        # Act
        data.get_to_do_list()
        data.run_fillers()
        data.get_missing_ratios_dict()

        # Assert
        self.assertTrue(data.missing_ratios_dict["Age"] == 0 and any(data.pandas_dataset["Age"] == data.fill_value),
                        msg="Failed to fill empty values")

    def setup_data(self):
        data = data_io.get_data(setup.get_datasets_path(), "titanic_train.csv")
        return data