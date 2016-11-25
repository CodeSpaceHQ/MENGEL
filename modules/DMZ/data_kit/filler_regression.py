from modules.DMZ.data_kit import data_splitting
from modules.DMZ.data_kit import data_filler
from sklearn import svm
import pandas as pd


class RegressionFiller(object):

    def __init__(self, train, test):
        self.model = None
        self.total_data = pd.concat([train, test])
        print(self.total_data)
        self.total_missing = self.select_incomplete_data(self.total_data)
        self.train_data = train
        self.test_data = test
        self.total_data = self.select_complete_data(self.total_data)
        print(self.total_data)
        print(self.total_missing)
        return

        self.complete_data = self.select_complete_data(train)
        self.incomplete_data = self.select_incomplete_data(train)
        self.filled_data = self.select_missing_column(self.incomplete_data, self.complete_data)

        self.complete_data = self.select_complete_data(test)
        self.incomplete_data = self.select_incomplete_data(test)
        self.filled_test_data = self.fill_test(self.incomplete_data, self.complete_data)

    def select_complete_data(self, data):
        data = data_splitting.remove_non_numeric_columns(data)
        return data_filler.drop_missing_data_rows(data, 0)

    def select_incomplete_data(self, data):
        data = data_splitting.remove_non_numeric_columns(data)
        return data_filler.drop_complete_data_rows(data)

    def select_missing_column(self, data, complete_data):
        for col in data:
            if data[col].isnull().sum(0) > 0:
                data, target_col = data_splitting.separate_target(data, col)
                target_indices = target_col.index.values
                train, training_target = data_splitting.separate_target(complete_data, col)

                self.model = svm.SVR(kernel="poly", degree=1)
                self.model = self.model.fit(train, training_target)
                print(self.model)
                predictions = self.model.predict(data)
                new_data = pd.DataFrame(data=predictions, index=target_indices, columns=[col])
                final = pd.concat([data, new_data], axis=1)
                frames = [final, complete_data]
                return pd.concat(frames)

    def fill_test(self, data, complete_data):
        missing_cols = []

        for col in data:
            if data[col].isnull().sum(0) > 0:
                data, target_col = data_splitting.separate_target(data, col)
                missing_cols.append((target_col, col))

        for column in missing_cols:
            target_indices = column[0].index.values

            print(data)
            predictions = self.model.predict(data)
            new_data = pd.DataFrame(data=predictions, index=target_indices, columns=[column[1]])
            final = pd.concat([data, new_data], axis=1)
            frames = [final, complete_data]
            return pd.concat(frames)

    def print_full(self, x):
        pd.set_option('display.max_rows', len(x))
        print(x)
        pd.reset_option('display.max_rows')

    def train_filler(self):
        return

    def fill_missing(self):
        return

    def fill_missing_columns(self):
        return

    def get_filled_data(self):
        return self.filled_data

    def get_filled_test_data(self):
        return self.filled_test_data
