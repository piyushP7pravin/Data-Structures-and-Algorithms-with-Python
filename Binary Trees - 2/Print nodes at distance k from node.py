"""
-------------------------------------  Print nodes at distance k from node  -----------------------------

Given a binary tree, a node and an integer K, print nodes which are at K distance from the the given node.

#### Input format :
    Line 1 : Elements in level order form (separated by space)
    (If any node does not have left or right child, take -1 in its place)
    Line 2 : Node
    Line 3 : K
#### Output format : 
    Answer nodes in different line

#### Sample Input :
    5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
    3
    1
#### Sample Output :
    9
    6
"""

## Read input as specified in the question.

## Print output as specified in the question.
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right = None

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

def printdown(root, k, d=0):

    if not root:
        return

    if k == d:
        print(root.data)

    printdown(root.left, k, d+1)
    printdown(root.right, k, d+1)
    
def printkDistanceNode(root, target, k): 

    if not root: 
        return -1

    if root.data == target: 
        printdown(root, k) 
        return 0 
      
    dl = printkDistanceNode(root.left, target, k) 
      
    if dl != -1: 
        if dl+1 == k : 
            print(root.data)
        else: 
            printdown(root.right, k-dl-2)  
        return 1 + dl 

    dr = printkDistanceNode(root.right, target, k) 

    if dr != -1: 
        if (dr+1 == k): 
            print(root.data)
        else: 
            printdown(root.left, k-dr-2) 
        return 1 + dr  
        
    return -1
# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
node = int(input())
k = int(input())
printkDistanceNode(root, node, k)    
   