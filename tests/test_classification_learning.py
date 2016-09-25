import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.ml_models import scikit_classification_learners
import setup

class TestClassificationLearning(TestCase):
    def test_random_forest(self):
        result = scikit_classification_learners.run_random_forest(setup.get_datasets_path(), "titanic_train.csv", ',')
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_knn(self):
        result = scikit_classification_learners.run_knn(setup.get_datasets_path(), "titanic_train.csv", ',')
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_svc(self):
        result = scikit_classification_learners.run_svc(setup.get_datasets_path(), "titanic_train.csv", ',')
        print(result)
        self.assertGreater(result, 0, msg="Failed to beat baseline")
