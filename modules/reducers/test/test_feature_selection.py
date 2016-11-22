import os
import sys

sys.path.insert(0, os.path.abspath('../../..'))

from unittest import TestCase
from modules.DMZ.data_kit import data_io
from modules.reducers import scikit_feature_selectors as st
import setup


class TestFeatureSelection(TestCase):

    def setUp(self):
        self.data = data_io.get_data(setup.get_datasets_path(), "winequality-red.csv")
        self.target = 'quality'
        self.start = self.data.shape

    def standard_feature_selection(self, reducer):
        # Act
        end = reducer.shape

        # Assert fewer columns
        self.assertLess(end[1], self.start[1], msg="Failed to beat baseline")

    def test_variance_threshold_selector(self):
        self.standard_feature_selection(st.variance_threshold_selector(self.data, self.target))

    def test_select_percentile_selector(self):
        self.standard_feature_selection(st.select_percentile_selector(self.data, self.target))

    def test_select_k_best_selector(self):
        self.standard_feature_selection(st.select_k_best_selector(self.data, self.target))
