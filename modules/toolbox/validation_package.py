from modules.toolbox import framework_tools as ft
from modules.toolbox import splitter as sp
import setup


class ValidationPackage(object):

    def __init__(self):
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None

    def setup_package(self, pack):
        self.x_train, self.x_test, self.y_train, self.y_test = ft.get_train_test(pack.train_data, pack.target_column)

    def split_file(self, train_file, target):
        splitter = sp.Splitter()
        splitter.Split(setup.get_datasets_path() + train_file)
        train = ft.get_data(setup.get_datasets_path(), "training.data.csv", ",")
        test = ft.get_data(setup.get_datasets_path(), "testing.data.csv", ",")
        self.x_train, self.y_train = ft.separate_target(train, target)
        self.x_test, self.y_test = ft.separate_target(test, target)

