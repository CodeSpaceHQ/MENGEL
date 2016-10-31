import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.DMZ.data_kit import data_io
from modules.DMZ.data_kit import data_filler
import setup
import numpy as np
import pandas as pd

from modules.toolbox.data_package import DataPackage
from modules.toolbox.validation_package import ValidationPackage

class TestDataFilling(TestCase):

    def test_drop_missing_data_columns(self):

        #Arrange
        data, start, target = self.setup_data()

        #Act
        end = (data_filler.drop_missing_data_columns(data, 1)).shape

        #Assert
        self.assertLess(end[1], start[1], msg="Failed to beat baseline")


    def test_drop_missing_data_rows(self):

        #Arrange
        data, start, target = self.setup_data()

        #Act
        end = (data_filler.drop_missing_data_rows(data, 100)).shape

        #Assert
        self.assertLess(end[0], start[0], msg="Failed to beat baseline")

    def test_drop_all_missing_data_columns(self):
        #Arrange
        data, start, target = self.setup_data()

        #Act
        end = (data_filler.drop_all_missing_data_columns(data)).shape

        #Assert
        self.assertLess(end[1], start[1], msg="Failed to beat baseline")


    def test_drop_all_missing_data_rows(self):

        #Arrange
        data, start, target = self.setup_data()

        #Act
        end = (data_filler.drop_all_missing_data_rows(data)).shape

        #Assert
        self.assertEqual(end[0], start[0], msg="Failed to beat baseline")

    def test_fill_missing_data(self):

        #Arrage
        data, start, target = self.setup_data()

        #Act
        data = data_filler.fill_missing_data(data, 7)

        #Assert
        self.assertFalse(data.isnull().values.any(), msg="Failed to beat baseline")

    def test_fill_missing_data_average(self):
        # Arrage
        data, start, target = self.setup_data()

        # Act

        data = data_filler.drop_all_missing_data_columns(data)
        data = data_filler.fill_missing_data_average(data)

        # Assert
        self.assertFalse(data.isnull().values.any(), msg="Failed to beat baseline")

    def setup_data(self):
        data = data_io.get_data(setup.get_datasets_path(), "titanic_train.csv")
        data["Nonsense"] = np.nan
        data = data.apply(pd.to_numeric,errors='coerce')
        target = 'Survived'
        start = data.shape
        return data, start, target
