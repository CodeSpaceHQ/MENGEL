class ConfigOptions(object):

    #Initialize the class
    def __init__(self):
        self.training_file_name = None
        self.test_file_name = None
        self.separator_type = None
        self.prediction_type = None
        self.target_column = None
        self.get_config_options()

    #Get input from user
    def get_config_options(self):
        self.training_file_name = raw_input("Provide the training file name: ")
        self.test_file_name = raw_input("Provide the testing file name: ")
        self.separator_type = raw_input("Provide the separator for the data files: ")
        self.prediction_type = raw_input("Provide the type of prediction being done (Auto, Regression, or Classification: ")
        self.target_column = raw_input("Provide the name of the column to be predicted: ")


