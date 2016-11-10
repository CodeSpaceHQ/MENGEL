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
        self.avg_range = None
        self.value_range = None
        self.fill_value = None
        self.pandas_dataset = None
        self.missing_ratios_dict = None
        self.to_do_list = dict()

        self.get_config_options()
        self.get_dataset()
        self.get_missing_ratios_dict()
        self.get_to_do_list()
        self.run_fillers()

    def get_config_options(self):
        # TODO: Update with configuration options
        self.file_name = "titanic_train.csv"
        # self.avg_thresh = .50
        # self.value_thresh = .70
        self.avg_range = [0, .15]
        self.value_range = [.15, .90]
        self.fill_value = -9999

    def get_dataset(self):
        self.pandas_dataset = data_io.get_data(setup.get_datasets_path(), self.file_name)

    def get_missing_ratios_dict(self):
        missing_ratios = dataset_insight.get_missing_ratios(self.pandas_dataset, "column")
        self.missing_ratios_dict = dict(zip(self.pandas_dataset.columns.values, missing_ratios))

    def get_to_do_list(self):
        for col in self.missing_ratios_dict:
            value = self.missing_ratios_dict[col]
            if value > self.avg_range[0] and value <= self.avg_range[1]:
                self.to_do_list[col] = "avg"
            elif value > self.value_range[0] and value <= self.value_range[1]:
                self.to_do_list[col] = "value"
            elif value != 0:
                self.to_do_list[col] = "drop"


    def run_fillers(self):
        print self.to_do_list
        dispatcher = {"avg": lambda pandas_data, _: data_filler.fill_missing_data_average(pandas_data),
                      "value": lambda pandas_data, filler: data_filler.fill_missing_data(pandas_data, filler),
                      "drop": lambda pandas_data, _: data_filler.drop_column(pandas_data)}
        for col in self.to_do_list:
            if(self.pandas_dataset[col].dtype != "object"):
                self.pandas_dataset[col] = dispatcher[self.to_do_list[col]](self.pandas_dataset, self.fill_value)


        # for col in self.pandas_dataset:
        #     if self.pandas_dataset[col].dtype != "object":
        #         if self.missing_ratios_dict[col] > 0:
        #             if self.missing_ratios_dict[col] <= self.avg_thresh:
        #                 self.pandas_dataset[col] = data_filler.fill_missing_data_average(self.pandas_dataset[col])
        #             elif self.missing_ratios_dict[col] <= self.value_thresh:
        #                 self.pandas_dataset[col] = data_filler.fill_missing_data(self.pandas_dataset[col], self.fill_value)
        #             else:
        #                 self.pandas_dataset.drop(col, axis=1, inplace=True)


x = FillerStrategy()
x.get_missing_ratios_dict()
print x.missing_ratios_dict
print x.pandas_dataset


