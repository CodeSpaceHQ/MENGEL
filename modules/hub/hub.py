# This file is responsible for controlling the delegation of tasks

import sys
import os
sys.path.insert(0, os.path.abspath('../..'))

from modules.DMZ.models import model_filter
from modules.worker import worker
from modules.DMZ import ticket
from modules.DMZ.utils import config_options
from modules.DMZ.data_kit import data_io
import setup


class Hub(object):

    def __init__(self):
        self.models = set()
        self.configuration = config_options.ConfigOptions()
        self.training_data = data_io.get_data(setup.get_datasets_path(), self.configuration.training_file_name)
        self.testing_data = data_io.get_data(setup.get_datasets_path(), self.configuration.test_file_name)
        self.tickets = []

        self.select_models()
        self.create_tickets()
        self.launch_workers()

    # This function takes in the configuration options and gets the
    # models that fit those configuration options.
    def select_models(self):
        self.models = model_filter.get_models(self.configuration.prediction_type)

    # Currently will only launch a single worker until we get the
    # distributed code working.
    def launch_workers(self):
        worker.Worker(self)

    # Creates the Tickets which are given to Workers.
    def create_tickets(self):
        for model in self.models:
            new_ticket = ticket.Ticket(model, self.training_data, self.testing_data, self.configuration.target_column)
            self.tickets.append(new_ticket)

    # A function that is called by Workers which returns a Ticket.
    def get_ticket(self):
        return self.tickets.pop()

hub = Hub()
