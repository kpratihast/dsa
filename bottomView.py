class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = None


def bottomView(root):
    if root is None:
        return

    q = []

    root.hd = 0

    treeMap = {}

    q.append(root)

    while(len(q) > 0):

        temp = q[0]

        treeMap[q[0].hd] = q[0].data

        node = q.pop(0)

        if node.left is not None:
            node.left.hd = temp.hd - 1
            q.append(node.left)

        if node.right is not None:
            node.right.hd = temp.hd + 1
            q.append(node.right)

    for key in sorted(treeMap):
        print(treeMap[key])


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

bottomView(root)
