from modules.DMZ.data_kit import validation_package


# This class will manage the data for the worker and prep it for use.
# Eventually it will make changes to the data. Currently it does not.
class DataController(object):

    def __init__(self, training, target):
        self.validation_pack = validation_package.ValidationPackage().prepare_package(training, target)
