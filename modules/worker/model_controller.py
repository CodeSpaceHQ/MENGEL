from modules.DMZ.models import model_filter


# This class will control the model and hyperparameter selection.
# We still need to figure out how to organize hyperparameter selection so that it
# is not an ugly mess, so this class will be mostly empty for now.
class ModelController(object):

    def __init__(self, ticket_model, target):
        self.model_name = ticket_model
        self.model = None

        self.get_model(target)

    def get_model(self, target):
        self.model = model_filter.find_model(self.model_name, target)
