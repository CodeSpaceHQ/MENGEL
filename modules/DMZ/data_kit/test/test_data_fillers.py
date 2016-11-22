import os
import sys

sys.path.insert(0, os.path.abspath('../../../..'))

from unittest import TestCase
from modules.DMZ.data_kit import data_io
from modules.DMZ.data_kit import data_filler
import setup
import numpy as np
import pandas as pd

from modules.toolbox.data_package import DataPackage
from modules.toolbox.validation_package import ValidationPackage


class TestDataFilling(TestCase):

    def setUp(self):
        self.data = data_io.get_data(setup.get_datasets_path(), "titanic_train.csv")
        self.data["Nonsense"] = np.nan
        self.data = self.data.apply(pd.to_numeric, errors='coerce')
        self.data.loc[self.data.shape[0]] = [np.nan] * self.data.shape[1]
        self.target = 'Survived'
        self.start = self.data.shape

    def test_drop_missing_data_rows(self):
        # Act
        end = (data_filler.drop_missing_data_rows(self.data, .99)).shape

        # Assert
        self.assertLess(end[0], self.start[0], msg="Failed to remove any rows")

    def test_drop_missing_data_columns(self):
        # Act
        end = (data_filler.drop_missing_data_columns(self.data, .99)).shape

        # Assert
        self.assertLess(end[1], self.start[1], msg="Failed to remove any columns")

    def test_drop_all_missing_data_columns(self):
        # Act
        end = (data_filler.drop_all_missing_data_columns(self.data)).shape

        # Assert
        self.assertLess(end[1], self.start[1], msg="Failed to remove any columns")

    def test_drop_all_missing_data_rows(self):
        # Act
        end = (data_filler.drop_all_missing_data_rows(self.data)).shape

        # Assert
        self.assertLess(end[0], self.start[0], msg="Failed to remove any rows")

    def test_fill_missing_data(self):
        # Act
        data = data_filler.fill_missing_data(self.data, 7)

        # Assert
        self.assertFalse(data.isnull().values.any(), msg="Failed to replace all NaNs")

    def test_fill_missing_data_average(self):
        # Act
        data = data_filler.drop_all_missing_data_columns(self.data)
        data = data_filler.fill_missing_data_average(data)

        # Assert
        self.assertFalse(data.isnull().values.any(), msg="Failed to replace all NaNs")
