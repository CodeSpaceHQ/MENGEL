# This file is responsible for controlling the delegation of tasks

class Hub(object):

    def __init__(self):
        self.models = None
        self.training_data = None
        self.testing_data = None
        self.configuration = None

        self.select_models(self.configuration)


    def select_models(self, config):
        return

    # Currently will only launch a single worker until we get the
    # distributed code working.
    def launch_workers(self):
        return
