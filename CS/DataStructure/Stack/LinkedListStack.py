import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from adts import StackADT
from List.LinkedList import LinkedList

class LinkedListStack(StackADT):
    def __init__(self):
        self.data = LinkedList()

    def push(self, data):
        return self.data.prepend(data)
    
    def pop(self):
        return self.data.popFront()
    
    def peek(self):
        return self.data.peekHead()
    
    def isEmpty(self):
        return self.data.size == 0
    
    def printStack(self):
        if self.isEmpty():
            print("스택이 비어있습니다.")
            return False
        cur_node = self.data.head
        print("-"*10)
        for i in range(self.data.size-1, -1, -1):
            print(f"| {i}번째 | {cur_node.data} |")
            cur_node = cur_node.next

if __name__ == "__main__":
    lls = LinkedListStack()
    print(lls.push(1))
    print(lls.push(2))
    print(lls.push(3))
    lls.printStack()
    print(lls.peek())
    print(lls.pop())
    print(lls.pop())
    lls.printStack()
    print(lls.pop())
    print(lls.pop())