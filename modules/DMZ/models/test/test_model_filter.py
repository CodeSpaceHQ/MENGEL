from __future__ import division # Forcing floating point division
import sys
import os
sys.path.insert(0, os.path.abspath('../../../..'))

from unittest import TestCase
from modules.DMZ.models import model_filter


class TestModelFilter(TestCase):

    def test_model_filter(self):

        # Arrange
        pred_type = "regression"
        expected_functions = {"train_passive_aggressive_regressor",
                              "train_support_vector_regression",
                              "train_bayesian_ridge",
                              "train_sgd_regressor"}

        # Act
        model_functions = model_filter.get_models(pred_type)

        # Assert
        for model in model_functions:
            self.assertIn(model.__name__, expected_functions, "Function does not exist as expected")
