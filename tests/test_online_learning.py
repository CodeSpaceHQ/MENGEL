import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.ml_models import scikit_online_regressors
from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners as mr
import setup


class TestOnlineLearning(TestCase):

    def test_sgd_regressor(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "winequality-red.csv", ";")
        x_train, x_test, y_train, y_test = ft.get_train_test(data, "quality")

        # Act
        model = scikit_online_regressors.train_sgd_regressor(x_train, y_train)
        result = mr.model_score(model, x_test, y_test)

        # Assert
        self.assertGreater(result, 0, msg="Failed to beat baseline")
    
    def test_passive_aggressive_regressor(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "winequality-red.csv", ";")
        x_train, x_test, y_train, y_test = ft.get_train_test(data, "quality")

        # Act
        model = scikit_online_regressors.train_passive_aggressive_regressor(x_train, y_train)
        result = mr.model_score(model, x_test, y_test)

        # Assert
        self.assertGreater(result, 0, msg="Failed to beat baseline")
