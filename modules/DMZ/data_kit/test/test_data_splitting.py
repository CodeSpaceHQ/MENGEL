from __future__ import division # Forcing floating point division
from unittest import TestCase
from modules.DMZ.data_kit import data_splitting
from modules.DMZ.data_kit import data_io
import path_handler


class TestDataSplitting(TestCase):

    def test_data_split(self):

        # Arrange
        data = data_io.get_data(path_handler.get_test_data() + "winequality-red.csv")

        # Act
        x_train, x_test, y_train, y_test = data_splitting.get_train_test(data, "quality")

        # Assert
        self.assertEqual(len(x_train[:, 0]), len(y_train))
        self.assertEqual(len(x_test[:, 0]), len(y_test))
        self.assertAlmostEqual(len(y_train)/len(y_test), 4, 2)
