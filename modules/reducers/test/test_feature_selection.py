import os
import sys

sys.path.insert(0, os.path.abspath('../../..'))

from unittest import TestCase
from modules.DMZ.data_kit import data_io
from modules.reducers import scikit_feature_selectors
import setup


class TestFeatureSelection(TestCase):
    def test_variance_threshold_selector(self):

        # Arrange
        data, start, target = self.setup_data()

        # Act
        reducer = scikit_feature_selectors.variance_threshold_selector(data, target)
        end = reducer.shape

        # Assert fewer columns
        self.assertLess(end[1], start[1], msg="Failed to beat baseline")

    def test_select_percentile_selector(self):

        # Arrange
        data, start, target = self.setup_data()

        # Act
        reducer = scikit_feature_selectors.select_percentile_selector(data, target)
        end = reducer.shape

        # Assert fewer columns
        self.assertLess(end[1], start[1], msg="Failed to beat baseline")

    def test_select_k_best_selector(self):

        # Arrange
        data, start, target = self.setup_data()

        # Act
        reducer = scikit_feature_selectors.select_k_best_selector(data, target)
        end = reducer.shape

        # Assert fewer columns
        self.assertLess(end[1], start[1], msg="Failed to beat baseline")

    def setup_data(self):
        data = data_io.get_data(setup.get_datasets_path(), "winequality-red.csv")
        target = 'quality'
        start = data.shape
        return data, start, target
