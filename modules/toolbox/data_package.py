from modules.DMZ.data_kit import data_io
from modules.DMZ.data_kit import data_splitting
import setup


class DataPackage(object):

    def __init__(self):
        self.test_data = None
        self.train_data = None
        self.target_column = None
        self.output_style = None

    def setup_training_data(self, train_file, target):
        # Loading training data
        self.train_data = data_io.get_data(setup.get_datasets_path(), train_file)

        # Setting what to predict
        self.target_column = target

    def setup_test_data(self, test_file):
        # Loading testing data
        self.test_data = data_io.get_data(setup.get_datasets_path(), test_file)

    def set_output_style(self, style):
        if style == "train" or style == "test":
            self.output_style = style
        else:
            self.output_style = "invalid"

