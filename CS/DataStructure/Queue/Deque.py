import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from List.DoublyLinkedList import DoublyLinkedList

class Deque:
    def __init__(self):
        self.data = DoublyLinkedList()

    def pushFront(self, data):
        self.data.prepend(data)
        return True

    def pushRear(self, data):
        self.data.append(data)
        return True
    
    def popFront(self):
        return self.data.removeNode(self.data.head)
    
    def popRear(self):
        return self.data.removeNode(self.data.tail)
    
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
    deque = Deque()
    print(deque.popFront())
    deque.pushRear(1)
    deque.pushRear(2)
    deque.pushRear(3)
    deque.pushFront(4)
    deque.pushFront(5)
    deque.pushFront(6)
    deque.printQueue()
    print(deque.popFront())
    print(deque.popFront())
    deque.printQueue()
    print(deque.popRear())
    print(deque.popRear())
    deque.printQueue()
    print(deque.popFront())
    print(deque.popFront())
    deque.printQueue()
    print(deque.popFront())
    deque.printQueue()