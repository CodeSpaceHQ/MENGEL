import pandas as pd
import dataset_insight
import data_filler

class FillerStrategy(object):

    def __init__(self):
        self.file_name = None
        self.pandas_dataset = None
        self.missing_ratios_dict = None
        self.avg_thresh = None
        self.value_thresh = None
        self.drop_thresh = None
        self.fill_value = None
        self.column_types = None

        self.get_config_options()
        self.get_dataset()
        self.get_dataset_composition()
        #self.get_missing_ratios()
        self.run_fillers()


    def get_config_options(self):
        # self.file_name = raw_input("Please input the file name: ")
        # self.avg_thresh = raw_input("Please input the avg threshold: ")
        # self.value_thresh = raw_input("Please input the value threshold: ")
        # self.drop_thresh = raw_input("Please input the drop threshold: ")
        self.file_name = "titanic_train.csv"
        self.avg_thresh = .50
        self.value_thresh = .80
        self.fill_value = -9999

    def get_dataset(self):
        self.pandas_dataset = pd.read_csv(self.file_name, sep=None)

    def get_dataset_composition(self):
        missing_ratios, self.column_types = dataset_insight.get_composition(self.pandas_dataset)
        self.missing_ratios_dict = dict(zip(self.pandas_dataset.columns.values, missing_ratios))

    # def get_missing_ratios(self):
    #     missing_ratios = dataset_insight.get_missing_ratios(self.pandas_dataset, "column")
    #     self.missing_ratios_dict = dict(zip(self.pandas_dataset.columns.values, missing_ratios))

    def run_fillers(self):

        for col in self.pandas_dataset:
            if self.pandas_dataset[col].dtype != "object":
                if self.missing_ratios_dict[col] > 0:
                    if self.missing_ratios_dict[col] <= self.avg_thresh:
                        self.pandas_dataset[col] = data_filler.fill_missing_data_average(self.pandas_dataset[col])
                    elif self.missing_ratios_dict[col] <= self.value_thresh:
                        self.pandas_dataset[col] = data_filler.fill_missing_data(self.pandas_dataset[col], self.fill_value)
                    else:
                        self.pandas_dataset[col] = self.pandas_dataset.drop(col, axis = 1, inplace = True)
            # We'd eventually like to run data fillers on all nonstring values and use their filled values to
            # predict what should fill missing string data, but that's an icebox goal.


x = FillerStrategy()
print x.pandas_dataset
