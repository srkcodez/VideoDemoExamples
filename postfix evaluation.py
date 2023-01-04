class Stack:
    def __init__(self, maxsize):
        """
        initializing data members of the stack,
        the maximum size and top
        """
        self.max = maxsize
        self.data = []
        self.top = -1

    def push(self, data):
        """
        insertion in the stack is called as push function.
        push function takes data as argument
        and inserts the data on to the top of stack
        until stack is not full
        """
        if self.top + 1 >= self.max:
            print('Stack overflow')
        else:
            self.top = self.top + 1
            self.data.insert(self.top, data)

    def pop(self):
        """
        Deleting an element in the stack is called as pop.
        pop function returns top element in the stack
        until stack is not empty
        """
        if self.top < 0:
            return -1
        else:
            ele = self.data[self.top]
            self.top = self.top - 1
            return (ele)

    def isEmpty(self):
        """
        checks whether stack is empty or not.
        if stack is empty return true
        """
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        """ checks whether stack is full or not """
        if self.top >= self.max:
            return True
        else:
            return False

    def peak(self):
        """
        peak function returns the element on the
        top of stack without modifying the top
        position. it helps to check the top element.
        """
        return self.data[self.top]


s1 = Stack(100)  # creates stack object with maximum size of 100
postfix_expression = input("enter postfix expression")
postfix_expression_list = postfix_expression.split(" ")  # seperates the lexical symbols.

def isoper(chr):
    if chr in ['+','-','*','/','%']:
        return True
    else:
        return False

def calculate(op1, op2, i):
    op1=int(op1)
    op2=int(op2)
    res = 0
    if i == '+':
        res = op1 + op2
    elif i == '-':
        res = op1 - op2
    elif i == '*':
        res = op1 * op2
    elif i == '/':
        res = op1 / op2
    elif i == '%':
        res = op1 % op2
    return res

for i in postfix_expression_list:
    if isoper(i) != True:
        s1.push(i)
    else:
        op2 = s1.pop()
        op1 = s1.pop()
        res = calculate(op1, op2, i)
        s1.push(res)

print("Result is :",s1.pop())
