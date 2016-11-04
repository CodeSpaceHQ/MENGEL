from __future__ import division # Forcing floating point division
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.DMZ.data_kit import data_scaling
from modules.DMZ.data_kit import data_io
import setup
import pandas as pd


class TestDataScaling(TestCase):

    def test_scaling(self):

        # Arrange
        data = data_io.get_data(setup.get_datasets_path(), "winequality-red.csv")

        # Act
        target = data_scaling.scale_numeric_data(data)
        target = pd.DataFrame.as_matrix(target)

        # Assert
        self.assertAlmostEqual(target.mean(), 0, 5)
        self.assertAlmostEqual(target.std(), 1, 5)
