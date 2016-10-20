# Citation: I used http://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
# as an example of doing raw input.

import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import unittest
from modules.ml_models import scikit_classification_learners
from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners as mr
import setup

from modules.toolbox.data_package import DataPackage
from modules.toolbox.validation_package import ValidationPackage
from modules.toolbox import ml_runners as mr


class TestClassificationLearning(unittest.TestCase):
    def test_random_forest(self):
        # Arrange
        data, validation_pack = self.setup_data()

        # Act
        model = scikit_classification_learners.train_random_forest()
        result = mr.model_use(model, validation_pack, data)

        # Assert
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_knn(self):
        # Arrange
        data, validation_pack = self.setup_data()

        # Act
        model = scikit_classification_learners.train_knn()
        result = mr.model_use(model, validation_pack, data)

        # Assert
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_svc(self):
        # Arrange
        data, validation_pack = self.setup_data()

        # Act
        model = scikit_classification_learners.train_svc()
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
