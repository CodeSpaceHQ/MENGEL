from modules.toolbox import framework_tools as ft
import setup


class DataPackage(object):

    def __init__(self):
        self.test_data = None
        self.train_data = None
        self.target_column = None
        self.output_style = None

    def setup_training_data(self, train_file, separator):
        # Loading training data
        self.train_data = ft.get_data(setup.get_datasets_path(), train_file, separator)

        # Setting what to predict
        self.target_column = raw_input("Which column should be predicted? Provide the name: ")

    def setup_test_data(self, test_file, separator):
        # Loading testing data
        self.test_data = ft.get_data(setup.get_datasets_path(), test_file, separator)

    def set_output_style(self, style):
        if style == "train" or style == "test":
            self.output_style = style
        else:
            self.output_style = "invalid"

