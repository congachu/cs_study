import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from adts import QueueADT
from List.DoublyLinkedList import DoublyLinkedList

class Deque(QueueADT):
    def __init__(self):
        self.data = DoublyLinkedList()

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