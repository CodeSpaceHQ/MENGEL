# This file is responsible for controlling the delegation of tasks

import sys
import os
sys.path.insert(0, os.path.abspath('../..'))

from modules.DMZ.models import model_filter
from modules.worker import worker
from modules.DMZ import ticket
from modules.DMZ.project_config import configuration
from modules.DMZ.data_kit import data_io
from modules.DMZ.data_kit import data_splitting
import setup
import pandas


class Hub(object):

    def __init__(self):

        file_name = raw_input("Input XML file name: ")
        self.configuration = configuration.Configuration(file_name)
        self.training_data = data_io.get_data(setup.get_datasets_path(), self.configuration.train_files[0])
        self.testing_data = data_io.get_data(setup.get_datasets_path(), self.configuration.test_files[0])

        self.models = set()
        self.tickets = []
        self.result_tickets = []

        self.select_models()
        self.create_tickets()
        self.launch_workers()
        self.save_best_result()

    # This function takes in the configuration options and gets the
    # models that fit those configuration options.
    def select_models(self):
        self.models = model_filter.get_models(self.configuration.config_data["Prediction"]["type"])

    # Currently will only launch a single worker until we get the
    # distributed code working.
    def launch_workers(self):
        worker.Worker(self)

    # Creates the Tickets which are given to Workers.
    def create_tickets(self):
        for model in self.models:
            new_ticket = ticket.Ticket(model, self.training_data, self.testing_data,
                                       self.configuration.config_data["Prediction"]["target"],
                                       self.configuration.config_data["ID_label"]["id_column"])
            self.tickets.append(new_ticket)

    # A function that is called by Workers which returns a Ticket.
    def get_ticket(self):
        if len(self.tickets) <= 0:
            return None

        return self.tickets.pop()

    def receive_result(self, finished_ticket):
        self.result_tickets.append(finished_ticket)

    def save_best_result(self):
        self.result_tickets.sort(key=lambda x: x.validation_results)

        for result in self.result_tickets:
            test_id_column = data_splitting.separate_target(self.testing_data,
                                                            self.configuration.config_data["ID_label"]["id_column"])[1]
            test_results = pandas.DataFrame(result.test_results, columns=None)
            final_predictions = pandas.concat([test_id_column, test_results], axis=1)
            final_predictions = final_predictions.values

            ml_name = result.ml_algorithm.__name__
            col_names = []
            col_names.append(result.id_column)
            col_names.append(result.target)

            data_io.save_predictions(setup.get_datasets_path(), final_predictions, ml_name, col_names)

hub = Hub()
