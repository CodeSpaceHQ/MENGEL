from unittest import TestCase
from modules.DMZ.data_kit import data_io
from modules.DMZ.data_kit import text_handler
import path_handler


class TestDataFilling(TestCase):

    def setUp(self):
        self.data = data_io.get_data(path_handler.get_test_data(), "unittest_data.csv")

    def test_text_column_to_numeric(self):

        # Arrange
        column = self.data["gender"]

        # Act
        self.data["gender"] = text_handler.text_column_to_numeric(column)

        # Assert
        self.assertTrue(self.data["gender"].dtype != "object", msg="Failed to convert text to categorical values")

    def test_convert_dataframe_text(self):
        # Act
        data = text_handler.convert_dataframe_text(self.data, .5)

        # Assert
        self.assertTrue(data["gender"].dtype != "object" and data["Name"].dtype == "object",
                        msg="Converted incorrect features")

    def test_convert_nonpredictive_text(self):
        # Act
        data = text_handler.convert_nonpredictive_text(self.data)

        # Assert
        self.assertTrue(data["Name"].isnull, msg="Failed to convert text to NaN")
