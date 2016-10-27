import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.DMZ.models.regression import scikit_regression_learners
from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners as mr
import setup

from modules.toolbox.data_package import DataPackage
from modules.toolbox.validation_package import ValidationPackage


class TestRegressionLearning(TestCase):

    def test_bayesian_ridge(self):
        # Arrange
        data, validation_pack = self.setup_data()

        # Act
        model = scikit_regression_learners.train_bayesian_ridge()
        result = mr.model_use(model[1], validation_pack, data)

        # Assert
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_support_vector_regression(self):
        # Arrange
        data, validation_pack = self.setup_data()

        # Act
        model = scikit_regression_learners.train_support_vector_regression()
        result = mr.model_use(model[1], validation_pack, data)

        # Assert
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def setup_data(self):
        data = DataPackage()
        validation_pack = ValidationPackage()
        data.setup_training_data("winequality-red.csv", ";", "quality")
        data.set_output_style("train")
        validation_pack.setup_package(data)
        return data, validation_pack
