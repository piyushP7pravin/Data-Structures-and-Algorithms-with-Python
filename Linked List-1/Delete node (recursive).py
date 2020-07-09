"""
-----------------------------------------  Delete node (recursive)  ---------------------------------------

Given a linked list and a position i, delete the node of ith position from Linked List recursively.
If position i is greater than length of LL, then you should return the same LL without any change.
Indexing starts from 0. You don't need to print the elements, just delete the node and return the head of 
updated LL.

#### Input format :
    Line 1 : Linked list elements (separated by space and terminated by -1)
    Line 2 : Integer i (position)

#### Output format :
    Updated LL elements (separated by space)

#### Sample Input 1 :
    3 4 5 2 6 1 9 -1
    3
#### Sample Output 1 :
    3 4 5 6 1 9

#### Sample Input 2 :
    3 4 5 2 6 1 9 -1
    0
#### Sample Output 2 :
    4 5 2 6 1 9
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteRec(head, i):
    if i<0:
        return head
    if head is None:
        return None
    if i==0:
        head=head.next
        return head
    
    smallHead=deleteRec(head.next,i-1)
    head.next=smallHead
    return head

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = deleteRec(l, i)
printll(l)
