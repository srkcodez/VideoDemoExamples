

SIZE = 50


# A class named node is created that will acts a single node of the complete binary tree
class node:

    # A constructor of the Node class with one paramter of integer type holding the data is created that will be used to add a new node to the complete binary tree
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    # A class named Queue is created that provide all the utilities of the Queue class




class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        self.array = []

    # A utility function named newNode with one paramter of integer type holding the data is created that will be used to add a new node to the complete binary tree


def newNode(data):
    # logic of adding a new node to the complete binary tree
    temp = node(data)
    return temp


# A utility function named createQueue is written that will be used to create a new Queue
def createQueue(size):
    global queue
    queue = Queue();
    queue.front = queue.rear = -1;
    queue.size = size;

    # all the elements in the Queue object are initialized with NULL
    queue.array = [None for i in range(size)]

    # And in the end an object of the Queue is returned
    return queue;


# A function named isEmpty is created to check whether the Queue object that is passed as a paramter is Empty or not
def isEmpty(queue):
    return queue.front == -1


# A function named isFull is created to check whether the Queue object that is passed as a paramter is full or not
def isFull(queue):
    return queue.rear == queue.size - 1;


# A function named hasOnlyOneItem is created to check whether the Queue object that is passed as a paramter has one element or more
def hasOnlyOneItem(queue):
    return queue.front == queue.rear;


# A function named Enqueue is created to add data to the Queue object that is passed as a paramter and root of the complete binary tree
def Enqueue(root):
    if (isFull(queue)):
        return;

    queue.rear += 1
    queue.array[queue.rear] = root;

    if (isEmpty(queue)):
        queue.front += 1;

    # A function named Dequeue is created to remove data from the Queue object that is passed as a paramter


def Dequeue():
    if (isEmpty(queue)):
        return None;

    temp = queue.array[queue.front];

    if (hasOnlyOneItem(queue)):
        queue.front = queue.rear = -1;
    else:
        queue.front += 1

    return temp;


# A function named getFront is written to get the front element from the Queue object that is passed as a paramter
def getFront(queue):
    return queue.array[queue.front];


#  A utility function named hasBothChild is written to check whether the a particular node has both the children nodes present or not
def hasBothChild(temp):
    return (temp and temp.left and temp.right);


#  A Function named insert is written that will be used to insert a new node in complete binary tree
def insert(root, data, queue):
    # Create a new node for
    # given data
    temp = newNode(data);

    # If the tree is empty,
    # initialize the root
    # with new node.
    if not root:
        root = temp;
    else:

        # get the front node of
        # the queue.
        front = getFront(queue);

        # If the left child of this
        # front node doesn't exist,
        # set the left child as the
        # new node
        if (not front.left):
            front.left = temp;

            # If the right child of this
        # front node doesn't exist, set
        # the right child as the new node
        elif (not front.right):
            front.right = temp;

            # If the front node has both the
        # left child and right child,
        # Dequeue() it.
        if (hasBothChild(front)):
            Dequeue();

            # Enqueue() the new node for
    # later insertions
    Enqueue(temp);
    return root


# Standard level order traversal to test above function
# This function will the data associated with all the nodes of the complete binary tree
def levelOrder(root):
    queue = createQueue(SIZE);
    Enqueue(root);

    while (not isEmpty(queue)):
        temp = Dequeue();
        print(temp.data, end=' ')
        if (temp.left):
            Enqueue(temp.left);
        if (temp.right):
            Enqueue(temp.right);

        # main function


def main():
    root = None

    queue = createQueue(SIZE)

    while (True):

        # Menu
        # Display messages
        print("Please Choose one of the Operations::")
        print("1. To Insert Data in the Complete binary tree.")
        print("2. To Display Data from the Complete binary tree.")
        print("\n")

        choice = int(input())

        # case 1
        if choice == 1:
            # Display message
            print("Enter the data that you want to add to the Complete binary tree::")
            key = int(input())
            root = insert(root, key, queue);
            print("Data Added Successfully.")
            # Break statement to terminate a case
            # break

        # Case 2
        if choice == 2:
            # Display message
            print("Contents of the Complete binary tree are::")
            levelOrder(root);
            # Break statement to terminate a case
            # break

        print("\nType [N or n] to terminate the program.\nType [Y or y] to continue the program.\n")
        ch = input()

        if ((ch == 'N' or ch == 'n')):
            break

        # call to the main function


if __name__ == "__main__":
    main()