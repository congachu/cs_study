import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from adts import QueueADT
from List.LinkedList import LinkedList

class LinkedQueue(QueueADT):
    def __init__(self):
        self.data = LinkedList()

    def enqueue(self, data):
        self.data.append(data)
        return True

    def dequeue(self):
        result = self.data.popFront()
        return result
    
    def peek(self):
        return self.data.peekHead()
    
    def isEmpty(self):
        return self.data.size == 0
    
    def printQueue(self):
        if self.isEmpty():
            print("큐가 비어있습니다.")
            return False
        cur_node = self.data.head
        print("-"*10)
        for _ in range(self.data.size):
            print(f"| {cur_node.data}", end=" ")
            cur_node = cur_node.next
        print("|\n" + "-"*10)


if __name__ == "__main__":
    lQueue = LinkedQueue()
    print(lQueue.dequeue())
    lQueue.enqueue(1)
    lQueue.enqueue(2)
    lQueue.enqueue(3)
    lQueue.enqueue(4)
    lQueue.enqueue(5)
    lQueue.enqueue(6)
    lQueue.printQueue()
    print(lQueue.peek())
    print(lQueue.dequeue())
    print(lQueue.dequeue())
    lQueue.printQueue()
    print(lQueue.dequeue())
    print(lQueue.dequeue())
    lQueue.printQueue()
    print(lQueue.dequeue())
    print(lQueue.dequeue())
    lQueue.printQueue()
    print(lQueue.dequeue())
    lQueue.printQueue()