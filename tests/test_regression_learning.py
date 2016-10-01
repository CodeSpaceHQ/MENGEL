import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.ml_models import scikit_regression_learners
from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners as mr
import setup


class TestRegressionLearning(TestCase):

    def test_bayesian_ridge(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "winequality-red.csv", ";")
        x_train, x_test, y_train, y_test = ft.get_train_test(data, "quality")

        # Act
        model = scikit_regression_learners.train_bayesian_ridge(x_train, y_train)
        result = mr.model_score(model, x_test, y_test)

        # Assert
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_support_vector_regression(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "winequality-red.csv", ";")
        x_train, x_test, y_train, y_test = ft.get_train_test(data, "quality")

        # Act
        model = scikit_regression_learners.train_support_vector_regression(x_train, y_train)
        result = mr.model_score(model, x_test, y_test)

        # Assert
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_adaboost_dtr(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "winequality-red.csv", ";")
        x_train, x_test, y_train, y_test = ft.get_train_test(data, "quality")

        # Act
        model = scikit_regression_learners.train_adaboost_dtr(x_train, y_train)
        result = mr.model_score(model, x_test, y_test)

        # Assert
        self.assertGreater(result, 0, msg="Failed to beat baseline")



