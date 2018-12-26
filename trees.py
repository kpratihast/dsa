class BinaryTree:
    def __init__(self, rootObject):
        self.key = rootObject
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def setRootVal(self,obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild

r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
r.getRightChild().insertRight('e')
r.getRightChild().insertLeft('f')
#r.insertLeft('f')
# q = BinaryTree('c')
# q.insertLeft('e')
# q.insertRight('f')
# r.insertRight(q)
print(r.getRootVal())
print(r.getRightChild().getRightChild().getRootVal())
print(r.getRightChild().getLeftChild().getRootVal())