import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners as mr
from reducers import scikit_component_analyzers
import setup

class TestDimensionalityReduction(TestCase):

    def test_Principle_Component_Analyzer(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        start = data.shape

        #Act
        analyzer = scikit_component_analyzers.Principle_Component_Analyzer(data)
        end = analyzer.shape

        #Assert fewer rows
        self.assertLess(end[0], start[0], msg = "Failed to beat baseline")

    def test_Independent_Component_Analyzer(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        start = data.shape

        #Act
        analyzer = scikit_component_analyzers.Independent_Component_Analyzer(data)
        end = analyzer.shape

        #Assert fewer rows
        self.assertLess(end[0], start[0], msg = "Failed to beat baseline")

    def test_Factor_Component_Analyzer(self):
        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        start = data.shape

        # Act
        analyzer = scikit_component_analyzers.Factor_Component_Analyzer(data)
        end = analyzer.shape

        # Assert fewer rows
        self.assertLess(end[0], start[0], msg="Failed to beat baseline")


    def test_Gaussian_Random_Projection(self):
        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        start = data.shape

        # Act
        analyzer = scikit_component_analyzers.Gaussian_Random_Projection(data)
        end = analyzer.shape

        # Assert fewer rows
        self.assertLess(end[0], start[0], msg="Failed to beat baseline")
