# The ticket is a task that has been assigned to a worker.
# Each ticket should comprise all of the information needed for the worker to
# complete the task.


class Ticket(object):

    def __init__(self, algorithm, train, test, label, train_folder=False, test_folder=False):
        self.ml_algorithm = algorithm
        self.training = train
        self.testing = test
        self.target = label
        self.training_data_in_folder = train_folder
        self.testing_data_in_folder = test_folder
