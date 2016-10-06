import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.ml_models import scikit_online_regressors
from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners as mr
import setup
from modules.toolbox.data_package import DataPackage
from modules.toolbox.validation_package import ValidationPackage


class TestOnlineLearning(TestCase):

    def test_sgd_regressor(self):
        # Arrange
        data, validation_pack = self.setup_data()

        # Act
        model = scikit_online_regressors.train_sgd_regressor(validation_pack, data)
        result = mr.model_use(model, validation_pack, data)

        # Assert
        self.assertGreater(result, 0, msg="Failed to beat baseline")
    
    def test_passive_aggressive_regressor(self):
        # Arrange
        data, validation_pack = self.setup_data()

        # Act
        model = scikit_online_regressors.train_passive_aggressive_regressor(validation_pack, data)
        result = mr.model_use(model, validation_pack, data)

        # Assert
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def setup_data(self):
        data = DataPackage()
        validation_pack = ValidationPackage()
        data.setup_training_data("winequality-red.csv", ";", "quality")
        data.set_output_style("train")
        validation_pack.setup_package(data)
        return data, validation_pack
