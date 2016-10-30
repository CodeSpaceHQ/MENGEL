from modules.DMZ.data_kit import validation_package


# This is the starting point for a worker, this will be changed when we
# start deploying workers with C code across the network.
class Worker(object):

    def __init__(self, hub):
        self.ticket = hub.get_ticket()
        # Next step is to add data_controller and model_controller
