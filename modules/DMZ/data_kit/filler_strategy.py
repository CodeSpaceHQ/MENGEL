import pandas as pd
import dataset_insight
import data_filler
import data_io
import path_handler


class FillerStrategy(object):

    def __init__(self, pandas_data):
        self.file_name = None
        self.avg_range = None
        self.value_range = None
        self.fill_value = None
        self.pandas_dataset = pandas_data
        self.missing_ratios_dict = None
        self.to_do_list = dict()
        self.get_config_options()
        self.get_missing_ratios_dict()
        self.get_to_do_list()
        self.run_fillers()

    def get_config_options(self):
        # TODO: Update with configuration options
        self.file_name = "titanic_train.csv"
        self.avg_range = [0, .50]
        self.value_range = [.50, .90]
        self.fill_value = -9999

    def get_missing_ratios_dict(self):
        missing_ratios = dataset_insight.get_missing_ratios(self.pandas_dataset, "column")
        self.missing_ratios_dict = dict(zip(self.pandas_dataset.columns.values, missing_ratios))

    def get_to_do_list(self):
        for col in self.missing_ratios_dict:
            col_ratio = self.missing_ratios_dict[col]
            if self.avg_range[0] < col_ratio <= self.avg_range[1]:
                self.to_do_list[col] = "avg"
            elif self.value_range[0] < col_ratio <= self.value_range[1]:
                self.to_do_list[col] = "value"
            elif col_ratio > self.value_range[1] and col_ratio > self.avg_range[1]:
                self.to_do_list[col] = "drop"

    def run_fillers(self):
        dispatcher = {"avg": lambda pandas_data, _: data_filler.fill_missing_data_average(pandas_data),
                      "value": lambda pandas_data, filler: data_filler.fill_missing_data(pandas_data, filler)}

        for col in self.to_do_list:
            if self.pandas_dataset[col].dtype != "object":
                if self.to_do_list[col] == "drop":
                    self.pandas_dataset.drop(col, axis=1, inplace=True)
                else:
                    self.pandas_dataset[col] = dispatcher[self.to_do_list[col]](self.pandas_dataset[col], self.fill_value)

