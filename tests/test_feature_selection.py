import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners as mr
from reducers import scikit_feature_selectors
from modules.toolbox.validation_package import ValidationPackage
import setup


class TestFeatureSelection(TestCase):
    def test_variance_threshold_selector(self):

        # Arrange
        data, start, target = self.setup_data()

        # Act
        reducer = scikit_feature_selectors.variance_threshold_selector(data, target)
        end = reducer.shape

        # Assert fewer columns
        self.assertLess(end[1], start[1], msg = "Failed to beat baseline")

    def test_select_percentile_selector(self):

        # Arrange
        data, start, target = self.setup_data()

        # Act
        reducer = scikit_feature_selectors.select_percentile_selector(data, target)
        end = reducer.shape

        # Assert fewer columns
        self.assertLess(end[1], start[1], msg = "Failed to beat baseline")

    def test_select_k_best_selector(self):

        # Arrange
        data, start, target = self.setup_data()

        # Act
        reducer = scikit_feature_selectors.select_k_best_selector(data, target)
        end = reducer.shape

        # Assert fewer columns
        self.assertLess(end[1], start[1], msg = "Failed to beat baseline")

    def setup_data(self):
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        target = 'Survived'
        start = data.shape
        return data, start, target
