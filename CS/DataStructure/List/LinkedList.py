import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from adts import ListADT

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(ListADT):
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return True

    def remove(self, data):
        prev = None
        if self.head == None:
            return False
        cur_node = self.head
        while cur_node != None and cur_node.data != data:
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node == None:
            return False
        if cur_node == self.head:
            if self.size == 1:
                self.__init__()
                return True
            else:
                self.head = self.head.next
                cur_node.next = None
        elif cur_node == self.tail:
            self.tail = prev
            self.tail.next = None
        else:
            prev.next = cur_node.next
        
        self.size -= 1
        return True
    
    def insert(self, data, index):
        if self.size <= 0:
            self.append(data)
            return True
        elif index <= 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        elif index >= self.size:
            self.append(data)
            return True
        else:
            cur_node = self.head
            for _ in range(index - 1):
                cur_node = cur_node.next
            new_node = Node(data)
            new_node.next = cur_node.next
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
        cur_num = 0
        print("[노드 번호 | 데이터]")
        while cur_node:
            print(f"[ {cur_num} | {cur_node.data} ]")
            cur_node = cur_node.next
            cur_num += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
        return True
    
    def popFront(self):
        if self.size == 0:
            return None
        result = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.size -= 1
        return result
    
    def peekHead(self):
        if self.size == 0:
            return None
        return self.head.data
    
    def removeNode(self, node: Node):
        prev = None
        if self.head == None:
            return False
        cur_node = self.head
        while cur_node != None and cur_node != node:
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node == None:
            return False
        if cur_node == self.head:
            if self.size == 1:
                self.__init__()
                return True
            else:
                self.head = self.head.next
                cur_node.next = None
        elif cur_node == self.tail:
            self.tail = prev
            self.tail.next = None
        else:
            prev.next = cur_node.next
        
        self.size -= 1
        return True


if __name__ == "__main__":
    linkedList = LinkedList()
    print(linkedList.append(1))
    print(linkedList.append(2))
    linkedList.print()
    print(linkedList.insert(1.5, 1))
    linkedList.print()
    print(linkedList.insert(3, 9999))
    linkedList.print()
    print(linkedList.insert(-1, -222))
    linkedList.print()
    print(linkedList.search(2))
    print(linkedList.remove(2))
    print(linkedList.search(2))
    print(linkedList.remove(2))
    linkedList.print()
    print(linkedList.remove(1))
    linkedList.print()