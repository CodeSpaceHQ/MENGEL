from modules.DMZ.data_kit import data_io
import path_handler
import pandas


# Handles training and retraining models
class Gym(object):

    def __init__(self):
        self.score = 0
        self.trained_model = None

    # Trains a model and returns the score it gets when applied to a subset of the
    # labeled data.
    def validate_model(self, data_control, model_control):
        self.trained_model = model_control.model[1].fit(data_control.validation_pack.x_train,
                                                   data_control.validation_pack.y_train)

        self.score = self.trained_model.score(data_control.validation_pack.x_test,
                                         data_control.validation_pack.y_test)

        print(self.score)

    def make_predictions(self, data_control):
        return self.trained_model.predict(data_control.unlabeled_data)
