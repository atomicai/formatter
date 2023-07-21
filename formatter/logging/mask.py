import abc


class ILogger(abc.ABC):
    @abc.abstractmethod
    def init_experiment(self):
        pass

    @abc.abstractmethod
    def log_metrics(self):
        pass
