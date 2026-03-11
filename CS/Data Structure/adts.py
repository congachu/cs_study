from abc import *

class ListADT(metaclass = ABCMeta):
    @abstractmethod
    def append(self, data):
        pass

    @abstractmethod
    def remove(self, data):
        pass

    @abstractmethod
    def insert(self, data, index):
        pass

    @abstractmethod
    def search(self, data):
        pass

    @abstractmethod
    def print(self):
        pass