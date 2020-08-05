"""
------------------------------------------  Min and max  ----------------------------------------------

Given a binary tree, find and return the min and max data value of given binary tree.
Return the output as an object of PairAns class, which is already created.

#### Input format :
    Elements in level order form (separated by space)
    (If any node does not have left or right child, take -1 in its place)
#### Output Format :
    Max and min (separated by space)

#### Sample Input :
    8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
#### Sample Output :
    14 1
"""

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

INT_MIN = -2147483648
INT_MAX = 2147483647

def minMax(root):

    if(root==None):
        return 2147483647,-2147483648

    lmin,lmax=minMax(root.left)
    rmin,rmax=minMax(root.right)

    curmin=min(lmin,rmin)
    curmax=max(lmax,rmax)

    if(root.data<curmin):
        curmin=root.data

    if(root.data>curmax):
        curmax=root.data

    return curmin,curmax 

def buildLevelTree(levelorder):

    index = 0
    length = len(levelorder)

    if length<=0 or levelorder[0]==-1:
        return None
        
    root = BinaryTreeNode(levelorder[index])

    index += 1
    q = queue.Queue()
    q.put(root)

    while not q.empty():

        currentNode = q.get()
        leftChild = levelorder[index]

        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelorder[index]

        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
            
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
minimum, maximum = minMax(root)
print(maximum, minimum)

