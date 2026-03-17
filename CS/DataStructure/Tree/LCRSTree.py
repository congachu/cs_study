class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightSibling = None

class LCRSTree:
    def __init__(self):
        self.root = None