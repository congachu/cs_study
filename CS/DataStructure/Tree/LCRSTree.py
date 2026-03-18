class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightSibling = None

class LCRSTree:
    def __init__(self):
        self.root = None

    def createRoot(self, node: Node):
        if self.root != None:
            print("이미 루트가 존재합니다.")
            return False
        self.root = node
        return True
    
    def addChild(self, parent: Node, child: Node):
        if parent.leftChild != None:
            self.addSibling(parent.leftChild, child)
        else:
            parent.leftChild = child
        return True
    
    def addSibling(self, sibling:Node, node:Node):
        cur_node = sibling
        while cur_node.rightSibling != None:
            cur_node = cur_node.rightSibling
        cur_node.rightSibling = node
        return True
    
    def printTree(self):
        print("-"*10)
        self.preorder(self.root)
        print("\n" + "-"*10)
        return True
    
    def preorder(self, node:Node):
        if node == None:
            return
        print(node.data, end=" ")
        if node.leftChild != None:
            self.preorder(node.leftChild)
        if node.rightSibling != None:
            self.preorder(node.rightSibling)
        return
            

if __name__ == "__main__":
    lcrsTree = LCRSTree()
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")

    lcrsTree.createRoot(nodeA)
    lcrsTree.createRoot(nodeB)
    lcrsTree.addChild(nodeA, nodeB)
    lcrsTree.addSibling(nodeB, nodeC)
    lcrsTree.addSibling(nodeB, nodeD)
    lcrsTree.addSibling(nodeD, nodeE)
    lcrsTree.addChild(nodeB, nodeF)
    lcrsTree.printTree()