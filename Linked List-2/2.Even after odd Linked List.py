'''<--------------------------Even after Odd LinkedList------------------------------------------>

###For a given singly linked list of integers, arrange the elements such that all the even numbers are placed after the odd numbers. The relative order of the odd and even terms should remain unchanged.

#Note :
No need to print the list, it has already been taken care. Only return the new head to the list.

###Input format:
	1.The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
	2.The first line of each test case or query contains the elements of the singly linked list separated by a single space. 

###Remember/Consider :
	While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element

###Output format:
	1.For each test case/query, print the elements of the updated singly linked list.
	2.Output for every test case will be printed in a seperate line.

###Constraints :
	1 <= t <= 10^2
	0 <= M <= 10^5
	Where M is the size of the singly linked list.

###Time Limit: 1sec

-->Sample Input 1 :
	1
	1 4 5 2 -1
-->Sample Output 1 :
	1 5 4 2 

--->Sample Input 2 :
	2
	1 11 3 6 8 0 9 -1
	10 20 30 40 -1
--->Sample Output 2 :
	1 11 3 9 6 8 0
	10 20 30 40
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrange_LinkedList(head):
    oddhead=None
    oddtail=None
    evenhead=None
    eventail=None
    cur=head
    while cur is not None:
        if ((cur.data)%2==0):
            if evenhead==None:
                evenhead=cur
                eventail=cur
            else:
                eventail.next=cur
                eventail=cur
        else:
            if oddhead==None:
                oddhead=cur
                oddtail=cur
            else:
                oddtail.next=cur
                oddtail=cur
        cur=cur.next
    #incase there is only even elements then oddhead and oddtail both are none.
    if oddhead is None and oddtail is None:
        return evenhead
    #incase linkedlist conatin only odd elemnts.
    elif evenhead is None and eventail is None:
        oddtail.next=evenhead
        return oddhead
    else:
        oddtail.next =None
        eventail.next=None
        oddtail.next=evenhead
        return oddhead

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def takeInput() : 
    head = None 
    tail = None

    datas = list(int(i) for i in input().strip().split(' '))

    i = 0 
    while (i < len(datas)) and (datas[i] != -1) : 
        data = datas[i] 
        newNode = Node(data)

        if head is None : 
            head = newNode 
            tail = newNode 
        else : 
            tail.next = newNode 
            tail = newNode

        i += 1 
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main

t = int(input()) 
while t > 0 : 
    head = takeInput() 
    l = arrange_LinkedList(head)
    printll(l)
    t-=1












