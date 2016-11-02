from modules.DMZ.data_kit import validation_package
from modules.DMZ.data_kit import data_filler
from modules.DMZ.data_kit import data_scaling
from modules.DMZ.data_kit import data_splitting


# This class will manage the data for the worker and prep it for use.
# Eventually it will make changes to the data. Currently it does not.
class DataController(object):

    def __init__(self, training, testing, target):
        # self.validation_pack = validation_package.ValidationPackage().prepare_package(training, target)
        self.validation_pack = validation_package.ValidationPackage()
        self.unlabeled_data = None

        self.prepare_data(training, testing, target)

    def prepare_data(self, training, testing, target):
        # Separating label data from training data.
        training, label_data = data_splitting.separate_target(training, target)

        # Temporary until we properly handle strings and text data.
        training = data_splitting.remove_non_numeric_columns(training)
        testing = data_splitting.remove_non_numeric_columns(testing)

        # Will need a function which governs what missing data system is used.
        training = data_filler.fill_missing_data(training, -9999)
        testing = data_filler.fill_missing_data(testing, -9999)

        # Scaling data. Will need a function which governs scaling method.
        training, testing = data_scaling.scale_data(training, testing)

        # Splitting into training and testing data
        self.validation_pack.prepare_package(training, label_data, .2)
        self.unlabeled_data = testing
