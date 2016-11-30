import os
import sys

sys.path.insert(0, os.path.abspath('../../../..'))

from unittest import TestCase
from modules.DMZ.models.regression import scikit_regression_learners
from modules.toolbox import ml_runners as mr

from modules.toolbox.data_package import DataPackage
from modules.DMZ.data_kit.validation_package import ValidationPackage
from modules.DMZ.utils import ml_test_utils


class TestRegressionLearning(TestCase):

    def setUp(self):
        self.data = DataPackage()
        self.validation_pack = ValidationPackage()
        self.data.setup_training_data("winequality-red.csv", "quality")
        self.data.set_output_style("train")
        self.validation_pack.setup_package(self.data)

    def test_bayesian_ridge(self):
        ml_test_utils.ml_test(scikit_regression_learners.train_bayesian_ridge(), self.validation_pack)

    def test_support_vector_regression(self):
        ml_test_utils.ml_test(scikit_regression_learners.train_support_vector_regression(), self.validation_pack)
