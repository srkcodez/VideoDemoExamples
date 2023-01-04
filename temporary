#  a + b -->  a b +

class Stack:
    def __init__(self, maxsize):
        self.max = maxsize
        self.data = []
        self.top = -1

    def push(self, data):
        if self.top + 1 >= self.max:
            print('Stack overflow')
        else:
            self.top = self.top + 1
            self.data.insert(self.top, data)

    def pop(self):
        if self.top < 0:
            return -1
        else:
            ele = self.data[self.top]
            self.top = self.top - 1
            return (ele)

    def isEmpty(self):
        if self.top == -1:
            return True

    def isFull(self):
        if self.top >= self.max:
            return True
        else:
            return False

    def peak(self):
        return self.data[self.top]


### infix to postfix notation:

operator_list = {'^': 0, '*': 1, '/': 1, '+': 2, '-': 2, '(': 3, ')': 3}

def isoper(chr):
    if chr in operator_list.keys():
        return True
    else:
        return False


def priority(chr):
    return operator_list.get(chr)


expression = input('enter expression')
expression_elements = expression.split(' ')
s1 = Stack(100)

for i in range(len(expression_elements)):
    ics = expression_elements[i]
    if isoper(ics):
        if s1.isEmpty():
            s1.push(ics)
        elif ics == ')':
            while s1.peak() != '(':
                print(s1.pop(), end=' ')
            s1.pop()
        else:
            while priority(s1.peak()) < priority(ics):
                print(s1.pop(), end=' ')
            s1.push(ics)
    else:
        print(ics, end=' ')
while 1:
    ele = s1.pop()
    if ele != -1:
        print(ele, end=' ')
    else:
        exit(0)
