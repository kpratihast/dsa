class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
    if lheight > rheight:
        return lheight+1
    else:
        return rheight+1


def spiral(root):
    h = height(root)
    flip = False
    print(root.data)
    for i in range(2, h+1):
        # print(root.data)
        printGivenLevel(root, i, flip)
        flip = not flip


def printGivenLevel(root, lvl, flip):
    if root is None:
        return
    if lvl == 1:
        return print(root.data)
    elif lvl > 1:
        if not flip:
            printGivenLevel(root.left, lvl-1, flip)
            printGivenLevel(root.right, lvl-1, flip)
        else:
            printGivenLevel(root.right, lvl-1, flip)
            printGivenLevel(root.left, lvl-1, flip)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.left = Node(5)
spiral(root)
