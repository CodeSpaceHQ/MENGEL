import data_controller, model_controller, gym


# This is the starting point for a worker, this will be changed when we
# start deploying workers with C code across the network.
class Worker(object):

    def __init__(self, hub):
        self.ticket = hub.get_ticket()
        self.data_control = None
        self.model_control = None
        self.model_gym = None

        self.setup_controllers()
        self.run_algorithm()

    # Creates controllers that are used to setup data, models, and use those two
    # in order to train a specific machine learning algorithm.
    def setup_controllers(self):
        self.data_control = data_controller.DataController(self.ticket.training, self.ticket.testing, self.ticket.target)
        self.model_control = model_controller.ModelController(self.ticket.ml_algorithm)
        self.model_gym = gym.Gym()

    # Runs the model using the prepped data. Validation results will be saved
    # with MLTA, results from the trained model applied to test data will be returned
    # and used on their own or by another service.
    # TODO: Integrate test data application.
    def run_algorithm(self):
        self.model_gym.validate_model(self.data_control, self.model_control)
