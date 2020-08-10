"""
----------------------------------  Replace with depth  -----------------------------------

In a given Generic Tree, replace each node with its depth value. You need to just update the 
data of each node, no need to return or print anything.

#### Input format :
    Line 1 : Elements in level order form separated by space (as per done in class). 
        Order is - 
            Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 

#### Sample Input 1 :
    10 3 20 30 40 2 40 50 0 0 0 0 
#### Sample Output 1 : (Level wise, each level in new line)
    0 
    1 1 1 
    2 2
"""

import queue

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

'''def replacewithDepth(tree):

    q=queue.Queue()
    q.put(tree)
    depth=0
    tree.data=depth
    while not(q.empty()):
        curr=q.get()
        if len(curr.children)>0:
            depth=depth+1
        for child in curr.children:
            q.put(child)
            child.data=depth'''

def replacewithDepth(tree,depth):
    
    tree.data=depth
        
    for child in tree.children:
        child.data=depth
        replacewithDepth(child,depth+1)
            
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

def printLevelAtNewLine(tree):
    q = [tree]
    newq = []
    while q:
        parent = q.pop(0)
        print(parent.data, end=' ')
        for child in parent.children:
            newq.append(child)
        if len(q)==0:
            q = newq
            newq = []
            print()  # Move to next Line

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
depth=0
replacewithDepth(tree,depth)
#replacewithDepth(tree)
printLevelAtNewLine(tree)
