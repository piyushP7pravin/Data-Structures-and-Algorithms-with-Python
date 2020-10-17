'''<----------------------------Bubble Sort (Iterative) LinkedList--------------------------------->

###Given a singly linked list of integers, sort it using 'Bubble Sort.'

###Note :
    No need to print the list, it has already been taken care. Only return the new head to the list.

###Input format :
    1.The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

    2.The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.

###Remember/Consider :
    While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element

###Output format :
    1.For each test case/query, print the elements of the sorted singly linked list.
    2.Output for every test case will be printed in a seperate line.

###Constraints :
    1 <= t <= 10^2
    0 <= M <= 10^5
    Where M is the size of the singly linked list.

    Time Limit: 1sec

--->Sample Input 1 :
    1
    10 9 8 7 6 5 4 3 -1
--->Sample Output 1 :
    3 4 5 6 7 8 9 10 

--->Sample Output 2 :
    2
    -1
    10 -5 9 90 5 67 1 89 -1
--->Sample Output 2 :
    -5 1 5 9 10 67 89 90 
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    count=0
    cur=head
    while cur is not None:
        count+=1
        cur=cur.next
    return count

def bubbleSortLL(head) :
    prev=None
    lent=length(head)
    count=0
    while count<lent:
        prev=None
        cur=head
        while cur.next is not None:
            if cur.data<cur.next.data:
                prev=cur
                cur=cur.next
            else:
                if prev!=None:
                    next1=cur.next
                    prev.next=next1
                    cur.next=next1.next
                    next1.next=cur
                    prev=next1
                else:
                    next1=cur.next
                    cur.next=next1.next
                    next1.next=cur
                    head=next1
                    prev=next1
        count+=1
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
t=int(input())
while t>0:
    # Read the link list elements including -1
    arr=list(int(i) for i in input().strip().split(' '))
    # Create a Linked list after removing -1 from list
    l = ll(arr[:-1])
    l = bubbleSortLL(l)
    printll(l)
    t-=1
