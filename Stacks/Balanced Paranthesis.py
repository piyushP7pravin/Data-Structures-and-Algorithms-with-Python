"""
------------------------------------------- Balanced Paranthesis -----------------------------------------

Given a string expression, check if brackets present in the expression are balanced or not. Brackets are 
balanced if the bracket which opens last, closes first.

You need to return true if it is balanced, false otherwise.

Note: This problem was asked in initial rounds in Facebook

#### Sample Input 1 :
    { a + [ b+ (c + d)] + (e + f) }
#### Sample Output 1 :
    true

#### Sample Input 2 :
    { a + [ b - c } ]
#### Sample Output 2 :
    false
"""

class Stack:
    def __init__(self):
        self.__data=[]
    def push(self,item):
        self.__data.append(item)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.__data.pop()
    def top(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.__data[len(self.__data)-1]
    def size(self):
        return len(self.__data)
    def isEmpty(self):
        return self.size()==0
    
def checkBalanced(expr):
    str=""
    for i in expr:
        if i in ["[","]","{","}","(",")"]:
            str=str+i
    s=Stack()
    for i in str:
        if i in ["[","{","("]:
            s.push(i)
        elif i is "]":
            if s.top()=="[":
                s.pop()
            else:
                return False
        elif i is "}":
            if s.top()=="{":
                s.pop()
            else:
                return False
        elif i is ")":
            if s.top()=="(":
                s.pop()
            else:
                return False
    return s.isEmpty()

exp=input()
if checkBalanced(exp):
    print('true')
else:
    print('false')

