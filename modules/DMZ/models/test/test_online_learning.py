from unittest import TestCase
from modules.DMZ.models.regression import scikit_online_regressors
from modules.DMZ.data_kit.data_package import DataPackage
from modules.DMZ.data_kit.validation_package import ValidationPackage
from modules.DMZ.utils import ml_test_utils
import path_handler


class TestOnlineLearning(TestCase):

    def setUp(self):
        self.data = DataPackage()
        self.validation_pack = ValidationPackage()
        self.data.setup_training_data(path_handler.get_test_data() + "winequality-red.csv", "quality")
        self.data.set_output_style("train")
        self.validation_pack.setup_package(self.data)

    def test_sgd_regressor(self):
        ml_test_utils.ml_test(self, scikit_online_regressors.train_sgd_regressor(), self.validation_pack)
    
    def test_passive_aggressive_regressor(self):
        ml_test_utils.ml_test(self, scikit_online_regressors.train_passive_aggressive_regressor(), self.validation_pack)
