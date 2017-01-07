import os
import sys

sys.path.insert(0, os.path.abspath('../../../..'))

from unittest import TestCase
from modules.DMZ.data_kit import data_io
from modules.reducers import scikit_component_analyzers
from sklearn.random_projection import GaussianRandomProjection
from sklearn.decomposition import PCA
from sklearn.decomposition import FactorAnalysis
from sklearn.decomposition import FastICA
import path_handler


class TestDimensionalityReduction(TestCase):

    def setUp(self):
        self.data = data_io.get_data(path_handler.get_datasets_path(), "winequality-red.csv")
        self.start = self.data.shape

    def standard_check(self, check):
        # Act
        analyzer = scikit_component_analyzers.run_analyzer(check, 3, self.data)
        end = analyzer.shape

        # Assert fewer rows
        self.assertLess(end[0], self.start[0], msg="Failed to beat baseline")

    def test_principle_component_analyzer(self):
        self.standard_check(PCA)

    def test_independent_component_analyzer(self):
        self.standard_check(FastICA)

    def test_factor_component_analyzer(self):
        self.standard_check(FactorAnalysis)

    def test_gaussian_random_projection(self):
        self.standard_check(GaussianRandomProjection)
