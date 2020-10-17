'''<--------------------------------------kReverse-------------------------------------------------->

### Given a singly linked list of integers, reverse the nodes of the linked list 'k' at a time and return its modified list.
 'k' is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of 'k,' then left-out nodes, in the end, should be reversed as well.

###Example :
    Given this linked list: 1 -> 2 -> 3 -> 4 -> 5

    For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5

    For k = 3, you should return: 3 -> 2 -> 1 -> 4 -> 5

###Note :
    No need to print the list, it has already been taken care. Only return the new head to the list.

###Input format :
    1.The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

    2.The first line of each test case or query contains the elements of the singly linked list separated by a single space.

    3.The second line of input contains a single integer depicting the value of 'k'.

###Remember/Consider :
    While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element

###Output format :
    For each test case/query, print the elements of the updated singly linked list.
    Output for every test case will be printed in a seperate line.

###Constraints :
    1 <= t <= 10^2
    0 <= M <= 10^5
    Where M is the size of the singly linked list.
    0 <= k <= M

    Time Limit:  1sec
--->Sample Input 1 :
    1
    1 2 3 4 5 6 7 8 9 10 -1
    4
--->Sample Output 1 :
    4 3 2 1 8 7 6 5 10 9

--->Sample Input 2 :
    2
    1 2 3 4 5 -1
    0
    10 20 30 40 -1
    4
--->Sample Output 2 :
    1 2 3 4 5 
    40 30 20 10 
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def kReverse(head, n):
    if n<=1:
        return head
    if head is None:
        return 
    if head.next is None:
        return head
    c=head
    p=None
    i=1
    nex=None
    while c and i<=n:
        nex=c.next
        c.next=p
        p=c
        c=nex
        i+=1
    if nex:
        head.next=kReverse(nex,n)
        
    return p

    
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
import sys
sys.setrecursionlimit(110000000)

# Main
t=int(input())
# Read the link list elements including -1
while t>0:
    arr=list(int(i) for i in input().strip().split(' '))
    # Create a Linked list after removing -1 from list
    l = ll(arr[:-1])
    i=int(input())
    l = kReverse(l,i)
    printll(l)
    t-=1


