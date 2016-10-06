import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import data_package
from modules.toolbox import ml_runners as mr


class TestMLRunners(TestCase):

    # The difficulty in testing machine learning code is the fact that the splitting functions cause
    # it to be random within a certain range. We might need to create a seed.
    def test_run_regressions(self):

        # Arrange
        package = data_package.DataPackage()
        package.setup_training_data("winequality-red.csv", ";", "quality")
        package.set_output_style("train")

        # Act
        results = mr.run_regressions(package)

        # Assert
        self.assertAlmostEqual(results[0], 0.329240031815, 0)
        self.assertAlmostEqual(results[1], 0.373687993227, 0)