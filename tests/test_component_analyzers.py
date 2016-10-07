import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners as mr
from reducers import scikit_component_analyzers
import setup

class TestDimensionalityReduction(TestCase):

    def test_principle_component_analyzer(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        start = data.shape

        # Act
        analyzer = scikit_component_analyzers.principle_component_analyzer(data)
        end = analyzer.shape

        # Assert fewer rows
        self.assertLess(end[0], start[0], msg = "Failed to beat baseline")

    def test_independent_component_analyzer(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        start = data.shape

        # Act
        analyzer = scikit_component_analyzers.independent_component_analyzer(data)
        end = analyzer.shape

        # Assert fewer rows
        self.assertLess(end[0], start[0], msg = "Failed to beat baseline")

    def test_factor_component_analyzer(self):
        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        start = data.shape

        # Act
        analyzer = scikit_component_analyzers.factor_component_analyzer(data)
        end = analyzer.shape

        # Assert fewer rows
        self.assertLess(end[0], start[0], msg="Failed to beat baseline")


    def test_gaussian_random_projection(self):
        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        start = data.shape

        # Act
        analyzer = scikit_component_analyzers.gaussian_random_projection(data)
        end = analyzer.shape

        # Assert fewer rows
        self.assertLess(end[0], start[0], msg="Failed to beat baseline")
