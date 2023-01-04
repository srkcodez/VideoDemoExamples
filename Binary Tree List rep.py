class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class CBT_LL:
    def __init__(self):
        self.root = None

    def newNode(self, data):
        temp = Node(data)
        return temp

    def constructTree(self, elelist):
        self.root=None
        q = Queue(50)
        for i in elelist:
            self.insert(i, q)
        return self.root

    def hasBothChild(self, temp):
        return (temp and temp.left and temp.right);

    def insert(self, data, q):
        # Create a new node for given data
        temp = self.newNode(data);
        # If the tree is empty, initialize the root with new node.
        if not self.root:
            self.root = temp;
        else:
            # check what is the front node in the queue
            front = q.getFront();
            # if front node doesn't have left child  set new node to it's left
            if not front.left:
                front.left = temp;
            # if front node doesn't have right child  set new node to it's right
            elif not front.right:
                front.right = temp;
            # If the front node has both the left child and right child, Dequeue() it.
            if self.hasBothChild(front):
                q.Dequeue();
        # Enqueue() the new node for later insertions
        q.Enqueue(temp);
        return self.root

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



class Queue:
    def __init__(self, max):
        self.front = self.rear = -1
        self.size = max
        self.array = []
        self.array = [None for i in range(self.size)]

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return self.rear == self.size - 1;

    def hasOnlyOneItem(self):
        return self.front == self.rear;

    def Enqueue(self, root):
        if self.isFull():
            return;
        self.rear += 1
        self.array[self.rear] = root;
        if self.isEmpty():
            self.front += 1;

    # A function named Dequeue is created to remove data from the Queue object that is passed as a paramter
    def Dequeue(self):
        if self.isEmpty():
            return None;
        temp = self.array[self.front];
        if self.hasOnlyOneItem():
            self.front = self.rear = -1;
        else:
            self.front += 1
        return temp;

    def getFront(self):
        return self.array[self.front];


class CompleteBinaryTree:
    def __init__(self):
        self.bintree = []
        self.bintree.append(0)

    def insert(self, data):
        self.bintree.append(data)
        self.bintree[0] = self.bintree[0] + 1

    def display(self):
        for i in range(1, len(self.bintree)):
            print(self.bintree[i], end=',')
        print()

    def Delete(self, data):
        if self.bintree[0] == 0:
            print('tree is empty')
        else:
            pos = self.bintree.index(data)
            if pos == self.bintree[0]:
                self.bintree.pop()
                self.bintree[0] = self.bintree[0] - 1
            else:
                self.bintree[pos] = self.bintree.pop()
                self.bintree[0] = self.bintree[0] - 1
        self.display()

    def search(self, data):
        for i in range(1, len(self.bintree)):
            if self.bintree[i] == data:
                print("Element Found")
                return True
        print("Element not Found")

    def inorder(self):
        t1= CBT_LL()
        r1 = t1.constructTree(self.bintree[1:])
        t1.inorder(r1)

    def preorder(self):
        t1 = CBT_LL()
        r1 = t1.constructTree(self.bintree[1:])
        t1.preorder(r1)


    def postorder(self):
        t1 = CBT_LL()
        r1 = t1.constructTree(self.bintree[1:])
        t1.postorder(r1)


btree = CompleteBinaryTree()

while True:
    ch = int(input('enter 1 for insert, 2 for delete,3 for display, 4 for search, 5 for inorder traversal, 6 for preorder 7 for post order 8 for exit'))
    if ch == 1:
        ele = input('enter element to be inserted')
        btree.insert(ele)

    elif ch == 2:
        ele = input('enter element to be deleted')
        btree.Delete(ele)

    elif ch == 3:
        btree.display()

    elif ch == 4:
        ele = input('enter element to be searched')
        btree.search(ele)

    elif ch == 5:
        btree.inorder()

    elif ch == 6:
        btree.preorder()

    elif ch == 7:
        btree.postorder()
    elif ch==8:
        break

