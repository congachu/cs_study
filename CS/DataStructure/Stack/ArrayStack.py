import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from adts import StackADT
from Array.Array import Array
    
class ArrayStack(StackADT):
    def __init__(self, size):
        self.top = -1
        self.data = Array(size)

    def push(self, data):
        if self.isFull():
            print("배열이 가득 찼습니다.")
            return False
        self.top += 1
        self.data.set(self.top, data)
        return True
    
    def pop(self):
        if self.isEmpty():
            print("배열이 비어있습니다.")
            return None
        result = self.data.get(self.top)
        self.data.set(self.top, None)
        self.top -= 1
        return result
    
    def peek(self):
        if self.isEmpty():
            print("배열이 비어있습니다.")
            return None
        return self.data.get(self.top)
    
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    
    def isFull(self):
        if self.data.len() == (self.top + 1):
            return True
        return False
    
    def printStack(self):
        if self.isEmpty():
            print("배열이 비어있습니다.")
            return False
        print("-"*10)
        for i in range(self.top, -1, -1):
            print(f"| {self.data.get(i)} |")
        print("-"*10)
        return True

if __name__ == "__main__":
    aStack = ArrayStack(5)
    print(aStack.pop())
    aStack.push(1)
    aStack.push(2)
    aStack.push(3)
    aStack.printStack()
    aStack.push(4)
    aStack.push(5)
    aStack.push(6)
    aStack.printStack()
    print(aStack.peek())
    print(aStack.pop())
    print(aStack.pop())
    print(aStack.peek())
    print(aStack.pop())
    print(aStack.pop())
    print(aStack.pop())
    print(aStack.pop())