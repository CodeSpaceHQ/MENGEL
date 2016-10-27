# This file is responsible for controlling the delegation of tasks

import sys
import os
sys.path.insert(0, os.path.abspath('../..'))

from modules.DMZ.models import model_filter
from modules.worker import worker
from modules.DMZ import ticket


class Hub(object):

    def __init__(self):
        self.models = set()
        self.training_data = None
        self.testing_data = None
        self.configuration = None
        self.tickets = []

        self.select_models()
        self.create_tickets()
        self.launch_workers()

    # This function takes in the configuration options and gets the
    # models that fit those configuration options.
    def select_models(self):
        self.models = model_filter.get_models(self.configuration.predict_type)

    # Currently will only launch a single worker until we get the
    # distributed code working.
    def launch_workers(self):
        worker.Worker(self)

    def create_tickets(self):
        for model in self.models:
            new_ticket = ticket.Ticket(model, self.training_data, self.testing_data, self.configuration.target)
            self.tickets.append(new_ticket)

    def get_ticket(self):
        return self.tickets.pop()

hub = Hub()
