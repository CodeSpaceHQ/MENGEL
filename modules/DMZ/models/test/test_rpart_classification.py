import os
import sys

sys.path.insert(0, os.path.abspath('../../../..'))

from unittest import TestCase
from modules.DMZ.models.regression import rpart_classification

from modules.toolbox.data_package import DataPackage
from modules.DMZ.data_kit.validation_package import ValidationPackage



class TestRpartLearning(TestCase):


    def test_rpart(self):
        # Arrange
        data, validation_pack = self.setup_data()

        #Act
        rpart = rpart_classification.Rpart()
        rpart_model = rpart.fit(data.train_data, data.target_column)
        rpart.predict(rpart_model, data.test_data)
        result = rpart.score()

        #Assert
        self.assertGreater(result, 0, Msg = "Failed to beat baseline")


    def setup_data(self):
        data = DataPackage()
        validation_pack = ValidationPackage()
        data.setup_training_data("winequality-red.csv", "quality")
        data.set_output_style("train")
        validation_pack.setup_package(data)
        return data, validation_pack
