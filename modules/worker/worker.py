

# This is the starting point for a worker, this will be changed when we
# start deploying workers with C code across the network.
class Worker(object):

    def __init__(self, hub):
        self.ticket = hub.get_ticket()
        self.validation_pack = 0  # TODO finish

    def split_data(self):
        return 0  # TODO finish


# WTF
