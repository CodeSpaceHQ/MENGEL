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
import setup

class TestDimensionalityReduction(TestCase):

    def test_principle_component_analyzer(self):

        # Arrange
        data, start = self.pre_test()

        #Act
        analyzer = scikit_component_analyzers.run_analyzer(PCA, 3, data)
        end = analyzer.shape

        # Assert fewer rows
        self.assertLess(end[0], start[0], msg="Failed to beat baseline")

    def test_independent_component_analyzer(self):

        # Arrange
        data, start = self.pre_test()

        #Act
        analyzer = scikit_component_analyzers.run_analyzer(FastICA, 3, data)
        end = analyzer.shape

        # Assert fewer rows
        self.assertLess(end[0], start[0], msg="Failed to beat baseline")

    def test_factor_component_analyzer(self):

        # Arrange
        data, start = self.pre_test()

        # Act
        analyzer = scikit_component_analyzers.run_analyzer(FactorAnalysis, 3, data)
        end = analyzer.shape

        # Assert fewer rows
        self.assertLess(end[0], start[0], msg="Failed to beat baseline")

    def test_gaussian_random_projection(self):

        # Arrange
        data, start = self.pre_test()

        # Act
        analyzer = scikit_component_analyzers.run_analyzer(GaussianRandomProjection, 3, data)
        end = analyzer.shape

        # Assert fewer rows
        self.assertLess(end[0], start[0], msg="Failed to beat baseline")

    def pre_test(self):
        data = data_io.get_data(setup.get_datasets_path(), "winequality-red.csv")
        start = data.shape

        return data, start

