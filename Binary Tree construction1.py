
class Queue:
    def __init__(self, max):
        self.max = max
        self.Q = []
        self.rear = -1
        self.front = 0

    def enqueue(self, ele):
        if self.rear < self.max:
            self.rear += 1
            self.Q.insert(self.rear, ele)
        else:
            print("Queue is full")

    def dequeue(self):
        if self.front <= self.rear:
            ele = self.Q[self.front]
            self.front += 1
            return ele
        else:
            print("Queue is empty")
            return -1

    def display(self):
        print("Elements in the Queue are")
        for i in range(self.front, self.rear + 1):
            print(self.Q[i], end=" ")
        print()


# driver program

q = Queue(5)


def displaymenu():
    print("\nEnter 1.Enqueue 2. Dequeue 3. Display 4.Exit ")


choice = 1
while choice != 4:
    displaymenu()
    choice = int(input("Enter your choice:"))
    if choice == 1:
        ele = int(input("Enter element to enqueue"))
        q.enqueue(ele)
    elif choice == 2:
        ele = q.dequeue()
        print("The deleted element is : ", ele)
    elif choice == 3:
        q.display()


SIZE = 50


# A class named node is created that will acts a single node of the complete binary tree
class node:

    # A constructor of the Node class with one paramter of integer type holding the data is created that will be used to add a new node to the complete binary tree
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    # A class named Queue is created that provide all the utilities of the Queue class




def newNode(data):
    # logic of adding a new node to the complete binary tree
    temp = node(data)
    return temp


# A utility function named createQueue is written that will be used to create a new Queue

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