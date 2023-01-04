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
