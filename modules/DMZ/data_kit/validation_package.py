from modules.DMZ.data_kit import data_splitting
from modules.DMZ.data_kit import data_io
from modules.DMZ.data_kit import dataset_insight
from modules.toolbox import splitter as sp
import setup


class ValidationPackage(object):

    def __init__(self):
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None

    # Deprecated
    def setup_package(self, pack):
        self.x_train, self.x_test, self.y_train, self.y_test = data_splitting.get_train_test(pack.train_data, pack.target_column)

    # This will be replacing the old function above. It sets up the split between training and testing data.
    def prepare_package(self, x, y, ratio):
        self.x_train, self.x_test, self.y_train, self.y_test = data_splitting.random_split(x, y, ratio)
