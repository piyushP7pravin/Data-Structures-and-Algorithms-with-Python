'''<----------------------------Swap two Nodes of LL------------------------------------------>

###You have been given a singly linked list of integers along with two integers, 'i,' and 'j.' Swap the nodes that are present at the 'i-th' and 'j-th' positions.

###Note :
    Remember, the nodes themselves must be swapped and not the datas.
    No need to print the list, it has already been taken care. Only return the new head to the list.

###Input format :
    1.The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

    2.The first line of each test case or query contains the elements of the singly linked list separated by a single space.

    3.The second line of input contains two integer values 'i,' and 'j,' respectively. A single space will separate them.

###Remember/consider :
    While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element

###Output format :
    For each test case/query, print the elements of the updated singly linked list.
    Output for every test case will be printed in a seperate line.
    Constraints :
    1 <= t <= 10^2
    0 <= M <= 10^5
    Where M is the size of the singly linked list.
    0 <= i < M
    0 <= j < M
    Time Limit: 1sec

---->Sample Input 1 :
    1
    3 4 5 2 6 1 9 -1
    3 4
--->Sample Output 1 :
    3 4 5 6 2 1 9 

--->Sample Input 2 :
    2
    10 20 30 40 -1
    1 2
    70 80 90 25 65 85 90 -1
    0 6
--->Sample Output 2 :
    10 30 20 40 
    90 80 90 25 65 85 70 
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head, i, j):
    p=None
    c=head
    
    p1=None    #####p1=None
    c1=None  #####c1=head
    p2=None   ######p2=None
    c2=None  ######c2=head
    count=0
    #m,n=0,0
    while c is not None: 
        if(count==i): 
            p1 = p 
            c1 = c
        elif(count==j): 
            p2 = p
            c2 = c 
        p = c 
        c = c.next 
        count += 1
    
    if(c1==None or c2==None): 
        return 
    if(p1==None): 
        head = c2 
    else: 
        p1.next = c2 
    if(p2==None): 
        head = c1 
    else: 
        p2.next = c1
        
    c = c1.next 
    c1.next = c2.next 
    c2.next = c 
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
    i, j=list(int(i) for i in input().strip().split(' '))
    l = swap_nodes(l, i, j)
    printll(l)
    t-=1
