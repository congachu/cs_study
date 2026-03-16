import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from adts import QueueADT
from Array.Array import Array

class CircularQueue(QueueADT):
    def __init__(self, size):
        self.data = Array(size)
        self.size = size
        self.front = 0
        self.rear = 0

    def enqueue(self, data):
        if self.isFull():
            print("큐가 가득 찼습니다.")
            return False
        self.data.set(self.rear, data)
        self.rear = (self.rear + 1) % self.size
        return True

    def dequeue(self):
        if self.isEmpty():
            print("큐가 비어있습니다.")
            return None
        result = self.data.get(self.front)
        self.data.set(self.front, None)
        self.front = (self.front + 1) % self.size
        return result
    
    def peek(self):
        if self.isEmpty():
            print("큐가 비어있습니다.")
            return None
        return self.data.get(self.front)
    
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return (self.rear + 1) % self.size == self.front
    
    def printQueue(self):
        print("-"*10)
        for i in range(0, self.data.len()):
            print(f"| {self.data.get(i)}", end=" ")
        print("|")
        print("-"*10)
        return True
    
if __name__ == "__main__":
    cQueue = CircularQueue(5)
    print(cQueue.dequeue())
    cQueue.enqueue(1)
    cQueue.enqueue(2)
    cQueue.enqueue(3)
    cQueue.printQueue()
    cQueue.enqueue(4)
    cQueue.enqueue(5)
    cQueue.printQueue()
    print(cQueue.dequeue())
    print(cQueue.dequeue())
    cQueue.printQueue()
    print(cQueue.peek())
    print(cQueue.dequeue())
    print(cQueue.dequeue())
    print(cQueue.dequeue())
    cQueue.enqueue(5)
    cQueue.enqueue(1)
    cQueue.printQueue()
    cQueue.enqueue(2)
    cQueue.enqueue(3)
    cQueue.enqueue(4)
    cQueue.printQueue()