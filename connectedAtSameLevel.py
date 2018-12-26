class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)


def height(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    if lheight > rheight:
        return lheight+1
    else:
        return rheight+1


def printGivenLevel(root, lvl):
    if root is None:
        return
    if lvl == 1:
        print(root.data)
    elif lvl > 1:
        printGivenLevel(root.left, lvl - 1)
        printGivenLevel(root.right, lvl - 1)


def levelOrder(root):
    if root is None:
        return
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.right = Node(60)
root.left.left = Node(40)
inOrder(root)
print("##")
levelOrder(root)
