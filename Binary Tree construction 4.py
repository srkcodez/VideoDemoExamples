# A class named node is created that will acts a single node of the complete binary tree
class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def newNode(self, data):
        temp = node(data)
        return temp

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

    def search(self, val):
        temp = self.root
        q = Queue(50)
        if not temp:
            print('tree is empty')
            return
        else:
            q.Enqueue(temp)
            while True:
                ele = q.getFront()
                if val == ele.data:
                    print('element found')
                elif val == temp.left.data:
                    print('element found at left child')
                elif val == temp.right.data:
                    print('element found at right child')
                q.Dequeue()
                if self.hasBothChild(ele):
                    q.Enqueue(ele.left)
                    q.Enqueue(ele.right)
                elif ele.left:
                    q.Enqueue(ele.left)
                else:
                    break

    def dispTree(self):
        q = Queue(50);
        q.Enqueue(self.root)
        while not q.isEmpty():
            temp = q.Dequeue()
            print(temp.data, end=' ')
            if temp.left:
                q.Enqueue(temp.left)
            if temp.right:
                q.Enqueue(temp.right)

    def deleteNode(self, val):
        if self.root.data==val and self.left==None and self.right==None:
            self.root=None
        q = Queue(50);
        if self.root:
            q.Enqueue(self.root)
            while not q.isEmpty():
                temp = q.Dequeue()
                # print(temp.data, end=' ')
                if temp.left:
                    q.Enqueue(temp.left)
                if temp.right:
                    q.Enqueue(temp.right)
            print(temp.data, 'deleted successfully')

            if lp.right:
                lp.right=None
            else:
                lp.left=
            self.dispTree()


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


#  A Function named insert is written that will be used to insert a new node in complete binary tree
def main():
    root = None
    queue = Queue(50)
    t1 = BinaryTree()
    while (True):
        # Display messages
        menu = ''' Please Choose one of the Operations 1. Insert 2. Display 3. Search 4. Delete'''
        choice = int(input(menu))
        # insert case
        if choice == 1:
            ele = int(input("Enter element to be inserted"))
            root = t1.insert(ele, queue);
            print("Data inserted Successfully.")
        # delete case
        elif choice == 2:
            # Display message
            print("Contents of the Complete binary tree are::")
            t1.dispTree();
        elif choice == 3:
            # Display message
            ele = int(input("Enter element to be searched"))
            t1.search(ele);
        elif choice == 4:
            # Display message
            ele = int(input("Enter element to be deleted"))
            t1.deleteNode(ele);

        else:
            print("\ninvalid choice\n")

        ch = input("\nType any key to continue and [N or n] to terminate:")
        if ((ch == 'N' or ch == 'n')):
            break

        # call to the main function


if __name__ == "__main__":
    main()
