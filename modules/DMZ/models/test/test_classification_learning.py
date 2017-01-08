# Citation: I used http://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
# as an example of doing raw input.

import unittest
from modules.DMZ.models.classification import scikit_classification_learners
from modules.DMZ.data_kit import data_package
from modules.DMZ.data_kit.validation_package import ValidationPackage
from modules.DMZ.utils import ml_test_utils


class TestClassificationLearning(unittest.TestCase):

    def setUp(self):
        self.data = data_package.DataPackage()
        self.validation_pack = ValidationPackage()
        self.data.setup_training_data("winequality-red.csv", "quality")
        self.data.set_output_style("train")
        self.validation_pack.setup_package(self.data)

    def test_random_forest(self):
        ml_test_utils.ml_test(self, scikit_classification_learners.train_random_forest(), self.validation_pack)

    def test_knn(self):
        ml_test_utils.ml_test(self, scikit_classification_learners.train_knn(), self.validation_pack)

    def test_svc(self):
        ml_test_utils.ml_test(self, scikit_classification_learners.train_svc(), self.validation_pack)
