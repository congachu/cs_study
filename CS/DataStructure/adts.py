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

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

class QueueADT(metaclass = ABCMeta):
    @abstractmethod
    def enqueue(self, data):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def peek(self):
        pass