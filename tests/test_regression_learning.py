import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.ml_models import scikit_regression_learners
from modules.toolbox import framework_tools as ft
import setup


class TestRegressionLearning(TestCase):

    def test_bayesian_ridge(self):
        data = ft.get_data(setup.get_datasets_path(), "winequality-red.csv", ";")
        result = scikit_regression_learners.run_bayesian_ridge(data, "quality")
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_support_vector_regression(self):
        data = ft.get_data(setup.get_datasets_path(), "winequality-red.csv", ";")
        result = scikit_regression_learners.run_support_vector_regression(data, "quality")
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_adaboost_dtr(self):
        data = ft.get_data(setup.get_datasets_path(), "winequality-red.csv", ";")
        result = scikit_regression_learners.run_adaboost_dtr(data, "quality")
        self.assertGreater(result, 0, msg="Failed to beat baseline")



