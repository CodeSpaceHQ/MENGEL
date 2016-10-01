import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners as mr
from reducers import scikit_dimensionality_reducers
import setup

class TestDimensionalityReduction(TestCase):

    def test_pca_reducer(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        #Act
        model = scikit_dimensionality_reducers.PCA_reducer(data)
        print(model)
