"""
---------------------------------------------------  Construct BST  --------------------------------------------------

Given a sorted integer array A of size n which contains all unique elements. You need to construct a balanced BST from 
this input array. Return the root of constructed BST.

Note : 
    If array size is even, take first mid as root.

#### Input format :
    Line 1 : Integer n (Size of array)
    Line 2 : Array elements (separated by space)
#### Output Format :
    BST elements (in pre order traversal, separated by space)

#### Sample Input :
    7
    1 2 3 4 5 6 7
#### Sample Output :
     
"""

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):

    if not lst: 
        return None
  
    # find middle 
    mid = (len(lst)-1) // 2

    root = BinaryTreeNode(lst[mid]) 

    root.left = constructBST(lst[:mid]) 
    root.right = constructBST(lst[mid+1:]) 

    return root

def preOrder(root):

    if root==None:
        return

    print(root.data, end=' ')
    
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
root=constructBST(lst)
preOrder(root)
