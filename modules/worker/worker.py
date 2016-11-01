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

    def setup_controllers(self):
        self.data_control = data_controller.DataController(self.ticket.training, self.ticket.testing, self.ticket.target)
        self.model_control = model_controller.ModelController(self.ticket.ml_algorithm, self.ticket.target)
        self.model_gym = gym.Gym()

    def run_algorithm(self):
        print(self.model_control.model)
        print(self.model_control.model[0])
        print(self.model_control.model[1])
        self.model_gym.validate_model(self.data_control, self.ticket.ml_algorithm[1])
