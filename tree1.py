class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class Tree:

    def __init__(self, data):
        self.root = Node(data)

    def insertNode(self, n, data):
        if n is None:
            return Node(data)
        if data < n.data:
            n.left = self.insertNode(n.left, data)
        if data > n.data:
            n.right = self.insertNode(n.right, data)
        return n

    def inorder(self, r):
        if r is not None:
            self.inorder(r.left)
            print(r.data, end=" ")
            self.inorder(r.right)

    def preorder(self, r):
        if r is not None:
            print(r.data, end=" ")
            self.preorder(r.left)
            self.preorder(r.right)

    def postorder(self, r):
        if r is not None:
            self.postorder(r.left)
            self.postorder(r.right)
            print(r.data, end=" ")


# driver code

t1 = Tree(5)

root = t1.root

# print(root.data)

t1.insertNode(root, 2)
t1.insertNode(root, 10)
t1.insertNode(root, 7)
t1.insertNode(root, 15)
t1.insertNode(root, 12)
t1.insertNode(root, 20)
t1.insertNode(root, 30)
t1.insertNode(root, 6)
t1.insertNode(root, 8)

print("\ninorder traversal")
t1.inorder(root)
print("\npreorder traversal")
t1.preorder(root)
print("\npostorder traversal")
t1.postorder(root)
