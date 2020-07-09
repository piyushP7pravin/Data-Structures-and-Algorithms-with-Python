"""
--------------------------------------------   Length of LL  ------------------------------------------------

For a given singly linked list of integers, find and return its length. Do it using an iterative method.

#### Input format :
    *The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the 
      test cases follow.
    * First and the only line of each test case or query contains elements of the singly linked list separated 
      by a single space. 
 
    Remember/Consider :
        While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, 
        would never be a list element.

#### Output format :
    For each test case, print the length of the linked list.
    Output for every test case will be printed in a seperate line.

#### Constraints :
    1 <= t <= 10^2
    0 <= N <= 10^5
    Time Limit: 1sec

#### Sample Input 1 :
    1
    3 4 5 2 6 1 9 -1
#### Sample Output 1 :
    7

#### Sample Input 2 :
    2
    10 76 39 -3 2 9 -23 9 -1
    -1
#### Sample Output 2 :
    8
    0
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
len=length(l)
print(len)
