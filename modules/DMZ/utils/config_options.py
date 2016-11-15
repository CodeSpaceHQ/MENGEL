class ConfigOptions(object):

    # Initialize the class, currently mocking the config setup.
    def __init__(self):
        self.training_file_name = "titanic_train.csv"
        self.test_file_name = "titanic_test.csv"
        self.prediction_type = "classification"
        self.target_column = "Survived"
        self.id_column = "PassengerId"

    # Get input from user
    def get_config_options(self):
        self.training_file_name = raw_input("Provide the training file name: ")
        self.test_file_name = raw_input("Provide the testing file name: ")
        self.prediction_type = raw_input("Provide the type of prediction being done (Regression or Classification: ")
        self.target_column = raw_input("Provide the name of the column to be predicted: ")

    # Check input from user
    def validate_options(self):
        predict = self.prediction_type.lower()
        if predict != "regression" and predict != "classification":
            print("Please input the type of prediction to be done.")
            return
