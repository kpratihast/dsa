class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = None


treeMap = dict()


def verticalOrder(root, hd):
    #root.hd = 0
    if root:
        #root.hd = 0
        try:
            treeMap[hd].append(root.data)
        except:
            treeMap[hd] = [root.data]
        if root.left is not None:
            hd = hd - 1
            verticalOrder(root.left, hd)
        if root.right is not None:
            hd = hd + 1
            verticalOrder(root.right, hd)

    print(treeMap)


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

verticalOrder(root, 0)
