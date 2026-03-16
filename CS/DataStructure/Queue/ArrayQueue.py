import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from adts import QueueADT
from Array.Array import Array

class ArrayQueue(QueueADT):
    def __init__(self, size):
        self.data = Array(size)
        self.front = 0
        self.rear = 0

    def enqueue(self, data):
        if self.isFull():
            print("큐가 가득 찼습니다.")
            return False
        self.data.set(self.rear, data)
        self.rear += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            print("큐가 비어있습니다.")
            return None
        result = self.data.get(self.front)
        self.data.set(self.front, None)
        self.front += 1
        return result
    
    def peek(self):
        if self.isEmpty():
            print("큐가 비어있습니다.")
            return None
        return self.data.get(self.front)
    
    def isEmpty(self):
        return self.rear == self.front
    
    def isFull(self):
        return self.data.len() == self.rear
    
    def printQueue(self):
        print("-"*10)
        for i in range(0, self.data.len()):
            print(f"| {self.data.get(i)}", end=" ")
        print("|")
        print("-"*10)
        return True
    
if __name__ == "__main__":
    aQueue = ArrayQueue(5)
    print(aQueue.dequeue())
    aQueue.enqueue(1)
    aQueue.enqueue(2)
    aQueue.enqueue(3)
    aQueue.printQueue()
    aQueue.enqueue(4)
    aQueue.enqueue(5)
    aQueue.enqueue(6)
    aQueue.printQueue()
    print(aQueue.dequeue())
    print(aQueue.dequeue())
    aQueue.printQueue()
    print(aQueue.peek())
    print(aQueue.dequeue())
    print(aQueue.dequeue())
    print(aQueue.dequeue())
    print(aQueue.dequeue())
    aQueue.enqueue(1)
    aQueue.printQueue()