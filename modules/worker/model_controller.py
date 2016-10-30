

# This class will control the model and hyperparameter selection.
# We still need to figure out how to organize hyperparameter selection so that it
# is not an ugly mess, so this class will be mostly empty for now.
class ModelController(object):

    def __init__(self, ticket_model):
        self.model = ticket_model
