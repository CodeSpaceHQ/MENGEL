from modules.DMZ.data_kit import data_splitting
from modules.DMZ.data_kit import data_filler


class RegressionFiller(object):

    def __init__(self, train, test):
        self.complete_data = self.select_complete_data(train)
        self.incomplete_data = self.select_incomplete_data(train)
        self.testing_data = test
        self.select_missing_column(self.incomplete_data)
        self.select_missing_column(self.complete_data)

    def select_complete_data(self, data):
        data = data_splitting.remove_non_numeric_columns(data)
        return data_filler.drop_missing_data_rows(data, 0)

    def select_incomplete_data(self, data):
        data = data_splitting.remove_non_numeric_columns(data)
        return data_filler.drop_complete_data_rows(data)

    def select_missing_column(self, data):
        print data

    def train_filler(self):
        return

    def fill_missing(self):
        return

    def fill_missing_columns(self):
        return
