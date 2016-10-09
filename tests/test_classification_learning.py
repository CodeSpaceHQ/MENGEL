import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import unittest
from modules.ml_models import scikit_classification_learners
from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners as mr
import setup


class TestClassificationLearning(unittest.TestCase):
    def test_random_forest(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        x_train, x_test, y_train, y_test = ft.get_train_test(data, "Survived")
        
        # Act
        model = scikit_classification_learners.train_random_forest(x_train, y_train)
        result = mr.model_score(model, x_test, y_test)

        # Assert
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_knn(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        x_train, x_test, y_train, y_test = ft.get_train_test(data, "Survived")

        # Act
        model = scikit_classification_learners.train_knn(x_train, y_train)
        result = mr.model_score(model, x_test, y_test)

        # Assert
        self.assertGreater(result, 0, msg="Failed to beat baseline")

    def test_svc(self):

        # Arrange
        data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
        x_train, x_test, y_train, y_test = ft.get_train_test(data, "Survived")

        # Act
        model = scikit_classification_learners.train_svc(x_train, y_train)
        result = mr.model_score(model, x_test, y_test)

        # Assert
        self.assertGreater(result, 0, msg="Failed to beat baseline")
