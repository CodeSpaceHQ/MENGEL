from modules.DMZ.data_kit import data_splitting
from modules.DMZ.data_kit import data_io
from modules.toolbox import splitter as sp
import setup


class ValidationPackage(object):

    def __init__(self):
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None

    def setup_package(self, pack):
        self.x_train, self.x_test, self.y_train, self.y_test = data_splitting.get_train_test(pack.train_data, pack.target_column)

    def split_file(self, train_file, target):
        splitter = sp.Splitter()
        splitter.Split(setup.get_datasets_path() + train_file, target)
        train = data_io.get_data(setup.get_datasets_path(), "training.data.csv", ",")
        test = data_io.get_data(setup.get_datasets_path(), "testing.data.csv", ",")
        self.x_train, self.y_train = data_splitting.separate_target(train, target)
        self.x_test, self.y_test = data_splitting.separate_target(test, target)
