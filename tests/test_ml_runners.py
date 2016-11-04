import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.DMZ.data_kit import validation_package
from modules.toolbox import ml_runners as mr, data_package


class TestMLRunners(TestCase):

    # The difficulty in testing machine learning code is the fact that the splitting functions cause
    # it to be random within a certain range. We might need to create a seed.
    def test_run_regressions(self):

        # Arrange
        package = data_package.DataPackage()
        package.set_output_style("train")
        package.setup_training_data("winequality-red.csv", "quality")
        validation_pack = validation_package.ValidationPackage()
        validation_pack.setup_package(package)

        # Act
        results = mr.run_regressions(validation_pack, package)

        # Assert
        self.assertAlmostEqual(results[0], 0.329824925476, 0)
        self.assertAlmostEqual(results[1], -0.0179604853689, 0)