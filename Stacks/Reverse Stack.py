"""
---------------------------------------- Reverse Stack -------------------------------------------

Reverse a given Stack with the help of another empty stack. Two stacks will be given. Out of which 
first contains some integers and second one is empty. You need to reverse the first one using second 
stack. Change in the given first stack itself.

Note : 
    You don't need to print or return the stack, just reverse the given stack and it will be printed internally.

#### Input format :
    Line 1 : Size of Stack
    Line 2 : Stack elements (separated by space)

#### Sample Input 1 :
    4 
    1 2 3 4     (4 is at top)
#### Sample Output 1 :
    1 2 3 4    (1 is at top)
"""

def reverseStack(s1,s2):
    if len(s1)<=1:
        return
    while len(s1)!=1:
        ele=s1.pop()
        s2.append(ele)
    lastElement=s1.pop()
    while len(s2)!=0:
        ele=s2.pop()
        s1.append(ele)
    reverseStack(s1,s2)
    s1.append(lastElement)
    
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
s1 = [int(ele) for ele in input().split()]
s2 = []
reverseStack(s1,s2)
while(len(s1) !=0):
    print(s1.pop(),end= ' ')