'''<--------------------------Delete every N nodes------------------------------------->

###You have been given a singly linked list of integers along with two integers, 'M,' and 'N.' Traverse the linked list such that you retain the 'M' nodes, then delete the next 'N' nodes. Continue the same until the end of the linked list.
To put it in other words, in the given linked list, you need to delete N nodes after every M nodes.

###Note :
    No need to print the list, it has already been taken care. Only return the new head to the list.

###Input format :
    1.The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

    2.The first line of each test case or query contains the elements of the singly linked list separated by a single space.

    3.The second line of input contains two integer values 'M,' and 'N,' respectively. A single space will separate them.

###Remember/Consider :
    While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element

###Output format :
    For each test case/query, print the elements of the updated singly linked list.
    Output for every test case will be printed in a seperate line.

###Constraints :
    1 <= t <= 10^2
    0 <= P <= 10^5
    Where P is the size of the singly linked list.
    0 <= M <= 10^5
    0 <= N <= 10^5 
    Time Limit: 1sec

--->Sample Input 1 :
    1
    1 2 3 4 5 6 7 8 -1
    2 2
--->Sample Output 1 :
    1 2 5 6

--->Sample Input 2 :
    2
    10 20 30 40 50 60 -1
    0 1
    1 2 3 4 5 6 7 8 -1
    2 3
--->Sample Output 2 :
    1 2 6 7
    Explanation of Sample Input 2 :
    For the first query, we delete one node after every zero elements hence removing all the items of the list. Therefore, nothing got printed.

    For the second query, we delete three nodes after every two nodes, resulting in the final list, 1 -> 2 -> 6 -> 7.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skipMdeleteN(head, M, N):
    if M==0:
        return 
    if N==0:
        return head
    cur=head
    c1=0
    c2=0
    while cur is not None:
        cur=head
        tail=None
        c1,c2=0,0
        while cur is not None:
            while c1<M:
                if tail==None:
                    tail=cur
                else:
                    tail.next=cur
                    tail=cur
                cur=cur.next
                if cur is None:
                    break
                c1+=1
                if c1==M:
                    c2=0
            while c2<N:
                if cur==None:
                    break
                cur=cur.next
                c2+=1
                if c2==N:
                    c1=0
        tail.next=None
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
    k=list(int(i) for i in input().strip().split(' '))
    m,n=k[0],k[1]
    l = skipMdeleteN(l, m, n)
    printll(l) 
    t-=1
