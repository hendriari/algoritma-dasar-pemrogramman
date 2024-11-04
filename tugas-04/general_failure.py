from abc import ABC, abstractmethod

class Failure(ABC):
    @abstractmethod
    def message(self):
        pass

class GeneralFailure(Exception, Failure):
    def __init__(self, message):
        self._message = message

    def message(self):
        return self._message