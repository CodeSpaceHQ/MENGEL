import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.DMZ.data_kit import data_io
from modules.DMZ.data_kit import text_handler
import setup

import pandas as pd
from sklearn import preprocessing
from modules.toolbox.data_package import DataPackage
from modules.toolbox.validation_package import ValidationPackage

class TestDataFilling(TestCase):

    def test_text_column_to_numeric(self):

        #Arrange
        data = self.setup_data()
        column = data["Sex"]

        #Act
        data["Sex"] = text_handler.text_column_to_numeric(column)

        #Assert
        self.assertTrue(data["Sex"].dtype != "object", msg="Failed to convert text to categorical values")

    def test_convert_dataframe_text(self):

        #Arrange
        data = self.setup_data()

        #Act
        data = text_handler.convert_dataframe_text(data, .5)

        #Assert
        self.assertTrue(data["Sex"].dtype != "object" and data["Name"].dtype == "object", msg="Converted incorrect features")

    def test_convert_nonpredictive_text(self):

        #Arrange
        data = self.setup_data()

        #Act
        data = text_handler.convert_nonpredictive_text(data)

        #Assert
        self.assertTrue(data["Name"].isnull, msg = "Failed to convert text to NaN")

    def setup_data(self):
        data = data_io.get_data(setup.get_datasets_path(), "titanic_train.csv")
        return data
