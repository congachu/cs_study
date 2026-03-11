from abc import *

class ListADT(metaclass = ABCMeta):
    @abstractmethod
    def append(self, data):
        pass

    def remove(self, data):
        pass

    def insert(self, data, index):
        pass

    def search(self, data):
        pass

    def print(self):
        pass