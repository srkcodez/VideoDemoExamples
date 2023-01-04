class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class Tree:
    def __int__(self):
        pass
    def createNode(self,data):
        return Node(data)
    def insertNode(self,Node,data):
        if Node is None:
            return self.createNode(data)
        if data < Node.data:
            Node.left= self.insertNode(Node.left,data)
        if data > Node.data:
            Node.right= self.insertNode(Node.right,data)
        return Node

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
    def preorder(self,root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

#driver code

t1=Tree()
root=t1.createNode(5)

#print(root.data)

t1.insertNode(root,2)
t1.insertNode(root,10)
t1.insertNode(root,7)
t1.insertNode(root,15)
t1.insertNode(root,12)
t1.insertNode(root,20)
t1.insertNode(root,30)
t1.insertNode(root,6)
t1.insertNode(root,8)


print("\ninorder traversal")
t1.inorder(root)
print("\npreorder traversal")
t1.preorder(root)
print("\npostorder traversal")
t1.postorder(root)

