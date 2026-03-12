import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from adts import ListADT

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None
        self.prev: Node = None

class CircularLinkedList(ListADT):
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.head.prev = self.tail
        self.tail.next = self.head
        self.size += 1
        return True
    
    def remove(self, data):
        if self.size == 0:
            return False
        cur_node = self.head
        count = 0
        while count < self.size and cur_node.data != data:
            cur_node = cur_node.next
            count += 1
        if cur_node == None:
            return False
        cur_node.next.prev = cur_node.prev
        cur_node.prev.next = cur_node.next
        self.size -= 1
        return True
    
    def insert(self, data, index):
        if index >= self.size:
            self.append(data)
            return True
        elif index <= 0:
            new_node = Node(data)
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.head = new_node
        else:
            cur_node = self.head
            for _ in range(index - 1):
                cur_node = cur_node.next
            new_node = Node(data)
            new_node.next = cur_node.next
            new_node.prev = cur_node
            cur_node.next = new_node
        self.size += 1
        return True
    
    def search(self, data):
        cur_node = self.head
        for _ in range(self.size):
            if cur_node.data == data:
                return True
            cur_node = cur_node.next
        return False
    
    def print(self):
        if self.size == 0:
            return False
        cur_node = self.head
        print("[노드 번호 | 데이터 | 이전 노드 값 | 다음 노드 값 ]")
        for num in range(self.size):
            print(f"[ {num} | {cur_node.data} | {cur_node.prev} | {cur_node.next} ]")
            cur_node = cur_node.next
    

if __name__ == "__main__":
    cll = CircularLinkedList()
    print(cll.append(1))
    print(cll.append(2))
    print(cll.append(3))
    print(cll.append(4))
    cll.print()
    print(cll.search(3))
    print(cll.remove(3))
    print(cll.search(3))
    cll.print()
    print(cll.insert(3, 2))
    cll.print()