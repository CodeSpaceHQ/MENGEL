import data_controller, model_controller
from modules.DMZ.data_kit import validation_package


# Handles training and retraining models
class Gym(object):

    def __init__(self):
        self.score = 0

    def validate_model(self, data_control, model_control):
        trained_model = model_control.model[1].fit(data_control.validation_pack.x_train,
                                                   data_control.validation_pack.y_train)

        self.score = trained_model.score(data_control.validation_pack.x_test,
                                         data_control.validation_pack.y_test)

        print(self.score)
