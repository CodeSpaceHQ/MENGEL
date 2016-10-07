import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners as mr
from reducers import scikit_feature_selectors
import setup

class TestFeatureSelection(TestCase):
    def test_VarianceThreshold_selector(self):

        #Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        target = 'Survived'
        start = data.shape

        #Act
        reducer = scikit_feature_selectors.VarianceThreshold_selector(data,target)
        end = reducer.shape

        #Assert fewer columns
        self.assertLess(end[1], start[1], msg = "Failed to beat baseline")

    def test_SelectPercentile_selector(self):

        #Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        target = 'Survived'
        start = data.shape

        #Act
        reducer = scikit_feature_selectors.SelectPercentile_selector(data,target)
        end = reducer.shape

        # Assert fewer columns
        self.assertLess(end[1], start[1], msg = "Failed to beat baseline")

    def test_SelectKBest_selector(self):

        #Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        target = 'Survived'
        start = data.shape

        #Act
        reducer = scikit_feature_selectors.SelectKBest_selector(data,target)
        end = reducer.shape

        # Assert fewer columns
        self.assertLess(end[1], start[1], msg = "Failed to beat baseline")