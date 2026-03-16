import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from adts import ListADT

class Node:
    def __init__(self, data):
        self.data = data
        self.prev:Node = None
        self.next:Node = None

class DoublyLinkedList(ListADT):
    def __init__(self):
        self.head:Node = None
        self.tail:Node = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return True
    
    def prepend(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        return True

    def remove(self, data):
        if self.size == 0:
            return False
        cur_node = self.head
        while cur_node != None and cur_node.data != data:
            cur_node = cur_node.next
        if cur_node == None:
            return False
        if cur_node == self.head:
            if self.size == 1:
                self.__init__()
                return True
            else:
                self.head.next.prev = None
                self.head = self.head.next
                cur_node.next = None
        elif cur_node == self.tail:
            self.tail = cur_node.prev
            self.tail.next = None
        else:
            cur_node.prev.next = cur_node.next
            cur_node.next.prev = cur_node.prev
        self.size -= 1
        return True
    
    def removeNode(self, node: Node):
        if node == None:
            return False
        if node == self.head:
            if self.size == 1:
                self.__init__()
                return node.data
            else:
                self.head.next.prev = None
                self.head = self.head.next
                node.next = None
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1
        return node.data

    def insert(self, data, index):
        if self.size == 0 or index >= self.size:
            self.append(data)
            return True
        elif index <= 0:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            cur_node = self.head
            for _ in range(index - 1):
                cur_node = cur_node.next
            new_node = Node(data)
            new_node.next = cur_node.next
            new_node.prev = cur_node
            cur_node.next.prev = new_node
            cur_node.next = new_node
        self.size += 1
        return True


    def search(self, data):
        cur_node = self.head
        while cur_node != None:
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
    dll = DoublyLinkedList()
    print(dll.append(1))
    print(dll.append(2))
    print(dll.append(3))
    print(dll.append(4))
    dll.print()
    print(dll.search(3))
    print(dll.remove(3))
    print(dll.search(3))
    dll.print()
    print(dll.insert(3, 2))
    dll.print()