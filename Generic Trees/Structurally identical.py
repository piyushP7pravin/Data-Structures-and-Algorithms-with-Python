"""
--------------------------------- Structurally identical --------------------------------

Given two Generic trees, return true if they are structurally identical 
i.e. they are made of nodes with the same values arranged in the same way.

#### Input format :
    Line 1 : Tree 1 elements in level order form separated by space (as per done in class). 
    Order is - 
        Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
    Line 2 : Tree 2 elements in level order form separated by space (as per done in class). 
    Order is - 
        Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
#### Output format :
    true or false

#### Sample Input 1 :
    10 3 20 30 40 2 40 50 0 0 0 0 
    10 3 20 30 40 2 40 50 0 0 0 0
#### Sample Output 1 :
    true

#### Sample Input 2 :
    10 3 20 30 40 2 40 50 0 0 0 0 
    10 3 2 30 40 2 40 50 0 0 0 0
#### Sample Output 2:
    false
"""

import queue

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def isIdentical(tree1, tree2):

    q1=queue.Queue()
    q2=queue.Queue()
    q1.put(tree1)
    q2.put(tree2)

    while (not(q1.empty() or q2.empty())):
        c1=q1.get()
        c2=q2.get()

        if c1.data!=c2.data:
            return False

        for child in c1.children:
            q1.put(child)

        for child in c2.children:
            q2.put(child)

    return True  
    
    '''if tree1 is None or tree2 is None:
        return False
    if tree1.data!=tree2.data:
        return False
    i,j=0,0
    while i<len(tree1.children) and j<len(tree2.children):
        if tree1.children[i].data!=tree2.children[j].data:
            return False
        i+=1
        j+=1
    return True'''

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr1 = list(int(x) for x in input().strip().split(' '))
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in input().strip().split(' '))
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')


