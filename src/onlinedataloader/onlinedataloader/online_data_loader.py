class OnlineDataLoader:
    config = None

    def __init__(self, config: dict):
        self.config = config

    def load_data(self):
        # TODO: Implement grpc to access data from the online data feeders as propagated by the data orchestrator
        pass

    def get_next_batch(self):
        # TODO: Get what data to feed from data orchestrator
        pass

    def get_next(self):
        # TODO: Connect instance with trainer to feed data fast and efficiently
        pass
