"""
------------------------------------------  Stack Using LL  ------------------------------------------------

You need to implement a Stack class using linked list.
The data members should be private.

Implement the following public functions :

1. Constructor -
    Initialises the data member (i.e. head to null).
2. push :
    This function should take one argument of type T and has return type void. This function should insert 
    an element in the stack. Time complexity should be O(1).
3. pop :
    his function takes no input arguments and has return type T. This should removes the last element which is 
    entered and return that element as an answer. Time complexity should be O(1).
4. top :
    This function takes no input arguments and has return type T. This should return the last element which 
    is entered and return that element as an answer. Time complexity should be O(1).
5. size :
    Return the size of stack i.e. count of elements which are present ins stack right now. Time complexity 
    should be O(1).
6. isEmpty :
    Checks if the stack is empty or not. Return true or false.
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class StackUsingLL:

    def __init__(self):
        self.__head = None
        self.__size = 0

    def push(self,data):
        newNode=Node(data)
        newNode.next=self.__head
        self.__head=newNode
        self.__size=self.__size+1

        
    def pop(self):
        if self.isEmpty():
            return 0
        e=self.__head.data
        self.__head=self.__head.next
        self.__size=self.__size-1
        return e
    # Return 0 if stack is empty. Don't display any other message
    def top(self):
        if self.isEmpty():
            return 0
        return self.__head.data
    # Return 0 if stack is empty. Don't display any other message
    def isEmpty(self):
        if self.__size==0:
            return True
        else:
            return False
        
    def getSize(self):
        return self.__size
        
    
s = StackUsingLL()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i+1])
        i+=1
    elif choice == 2:
        ans = s.pop()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        if(s.isEmpty()):
            print('true')
        else:
            print('false')
    i+=1






