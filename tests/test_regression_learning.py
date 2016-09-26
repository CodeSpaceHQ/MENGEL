import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.ml_models import scikit_regression_learners
import setup


class TestRegressionLearning(TestCase):

    def test_bayesian_ridge(self):
        result = scikit_regression_learners.run_bayesian_ridge(setup.get_datasets_path(), "winequality-red.csv", ';')
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_support_vector_regression(self):
        result = scikit_regression_learners.run_support_vector_regression(setup.get_datasets_path(), "winequality-red.csv", ';')
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_adaboost_dtr(self):
        result = scikit_regression_learners.run_adaboost_dtr(setup.get_datasets_path(), "winequality-red.csv", ';')
        self.assertGreater(result, 0, msg="Failed to beat baseline")



