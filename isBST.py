class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


a = []


def isBST(root):
    if root:
        isBST(root.left)
        a.append(root.data)
        isBST(root.right)


root = Node(10)
root.left = Node(7)
root.right = Node(39)
# root.left.left = Node(4)
root.left.right = Node(8)
# root.left.left.left = Node(6)

isBST(root)

if sorted(a) == a:
    print("1")
else:
    print('0')
