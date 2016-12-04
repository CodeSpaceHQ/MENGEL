from modules.DMZ.data_kit import data_splitting
from modules.DMZ.data_kit import data_filler
from sklearn import svm
import xgboost
import pandas as pd


class RegressionFiller(object):

    def __init__(self, train, test):
        self.model = None
        self.filled_data = None
        self.filled_test_data = None
        self.train_data = train
        self.test_data = test

        self.total_data = pd.concat([train, test], ignore_index=True)
        self.total_missing = self.select_incomplete_data(self.total_data)
        self.total_data = self.select_complete_data(self.total_data)
        self.filled_data = self.fill_missing_columns(self.train_data, self.total_data)
        self.filled_test_data = self.fill_missing_columns(self.test_data, self.total_data)

    def select_complete_data(self, data):
        data = data_splitting.remove_non_numeric_columns(data)
        return data_filler.drop_missing_data_rows(data, 0)

    def select_incomplete_data(self, data):
        data = data_splitting.remove_non_numeric_columns(data)
        return data_filler.drop_complete_data_rows(data)

    def select_missing_columns(self, data):
        training_columns = []
        target_columns = []

        for col in data:
            if data[col].isnull().sum(0) > 0:
                target_columns.append(col)
            else:
                training_columns.append(col)

        return training_columns, target_columns

    def apply_filler(self, x_train, y_train, x_test):
        model = xgboost.XGBRegressor()
        model = model.fit(x_train, y_train)
        return model.predict(x_test)

    def fill_missing(self, y_test, results, data, target_col):
        for value in range(0, y_test.shape[0]):
            if str(y_test.iloc[value].values[0]) == "nan":
                row = y_test.iloc[value].name
                value = results[int(y_test.iloc[value].name)]
                data.set_value(row, target_col, value)

        return data

    def fill_missing_columns(self, data, complete_data):
        training_columns, target_columns = self.select_missing_columns(data)

        for target_col in target_columns:
            x_train, y_train = data_splitting.separate_target(complete_data, target_col)
            x_test, y_test = data_splitting.separate_target(data, target_col)
            results = self.apply_filler(x_train, y_train, x_test)
            data = self.fill_missing(y_test, results, data, target_col)

        return data

    def get_filled_data(self):
        return self.filled_data

    def get_filled_test_data(self):
        return self.filled_test_data
