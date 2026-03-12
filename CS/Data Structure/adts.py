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

class StackADT(metaclass = ABCMeta):
    @abstractmethod
    def push(self, data):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def print(self):
        pass

    def isEmpty(self):
        pass

    def isFull(self):
        pass

    def size(self):
        pass