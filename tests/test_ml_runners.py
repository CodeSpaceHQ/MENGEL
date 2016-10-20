import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import data_package
from modules.toolbox import validation_package
from modules.toolbox import ml_runners as mr


class TestMLRunners(TestCase):

    # The difficulty in testing machine learning code is the fact that the splitting functions cause
    # it to be random within a certain range. We might need to create a seed.
    def test_run_regressions(self):

        # Arrange
        package = data_package.DataPackage()
        package.set_output_style("train")
        validation_pack = validation_package.ValidationPackage()
        validation_pack.split_file("winequality-red.csv", "quality")

        # Act
        results = mr.run_regressions(validation_pack, package)

        # Assert
        self.assertAlmostEqual(results[0], 0.329824925476, 0)
        self.assertAlmostEqual(results[1], -0.0179604853689, 0)