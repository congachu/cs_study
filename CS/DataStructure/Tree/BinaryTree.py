class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def createRoot(self, node:Node):
        if self.root != None:
            print("루트가 이미 존재합니다.")
            return False
        self.root = node
        return True
    
    def addChildLeft(self, parent:Node, child:Node):
        if parent.left != None:
            print("이미 왼쪽 자식 노드가 존재합니다.")
            return False
        parent.left = child
        return True

    def addChildRight(self, parent:Node, child:Node):
        if parent.right != None:
            print("이미 오른쪽 자식 노드가 존재합니다.")
            return False
        parent.right = child
        return True
    
    def printTree(self):
        if self.root == None:
            print("트리 비어있음")
            return False
        print("전위" + "-"*10)
        self.preorder(self.root)
        print("\n중위" + "-"*10)
        self.inorder(self.root)
        print("\n후위" + "-"*10)
        self.postorder(self.root)
        print("\n" + "-"*10)

    def preorder(self, node:Node):
        if node == None:
            return
        print(node.data, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
        return

    def inorder(self, node:Node):
        if node == None:
            return
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)
        return

    def postorder(self, node:Node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=" ")
        return

if __name__ == "__main__":
    bTree = BinaryTree()
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")

    bTree.createRoot(nodeA)
    bTree.addChildLeft(nodeA, nodeB)
    bTree.addChildLeft(nodeB, nodeC)
    bTree.addChildRight(nodeB, nodeD)
    bTree.addChildRight(nodeA, nodeE)
    bTree.addChildLeft(nodeE, nodeF)
    bTree.addChildRight(nodeE, nodeG)
    bTree.printTree()