class ConfigReader(object):
    """Abstract Class which should be used to implement the reading of the config for different notification services"""

    def __init__(self, config):
        self._config = config

    def get_device(self, device_number):
        raise NotImplementedError("Should have implemented this")
