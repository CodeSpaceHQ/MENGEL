import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import unittest
from modules.ml_models import scikit_classification_learners
from modules.toolbox import framework_tools as ft
import setup


class TestClassificationLearning(unittest.TestCase):
    def test_random_forest(self):
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        result = scikit_classification_learners.run_random_forest(data, "Survived")
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_knn(self):
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        result = scikit_classification_learners.run_knn(data, "Survived")
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_svc(self):
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        result = scikit_classification_learners.run_svc(data, "Survived")
        self.assertGreater(result, 0, msg="Failed to beat baseline")
