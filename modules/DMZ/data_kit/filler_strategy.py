import pandas as pd
import dataset_insight
import data_filler
import data_io
import setup

class FillerStrategy(object):

    def __init__(self):
        self.file_name = None
        self.avg_thresh = None
        self.value_thresh = None
        self.fill_value = None
        self.pandas_dataset = None
        self.missing_ratios_dict = None

        self.get_config_options()
        self.get_dataset()
        self.get_missing_ratios_dict()
        self.run_fillers()

    def get_config_options(self):
        # TODO: Update with configuration options
        self.file_name = "titanic_train.csv"
        self.avg_thresh = .50
        self.value_thresh = .70
        self.fill_value = -9999

    def get_dataset(self):
        self.pandas_dataset = data_io.get_data(setup.get_datasets_path(), "titanic_train.csv")

    def get_missing_ratios_dict(self):
        missing_ratios = dataset_insight.get_missing_ratios(self.pandas_dataset, "column")
        self.missing_ratios_dict = dict(zip(self.pandas_dataset.columns.values, missing_ratios))

    def run_fillers(self):

        for col in self.pandas_dataset:
            if self.pandas_dataset[col].dtype != "object":
                if self.missing_ratios_dict[col] > 0:
                    if self.missing_ratios_dict[col] <= self.avg_thresh:
                        self.pandas_dataset[col] = data_filler.fill_missing_data_average(self.pandas_dataset[col])
                    elif self.missing_ratios_dict[col] <= self.value_thresh:
                        self.pandas_dataset[col] = data_filler.fill_missing_data(self.pandas_dataset[col], self.fill_value)
                    else:
                        self.pandas_dataset.drop(col, axis=1, inplace=True)
