"""
-------------------------------------  Diameter Of Binary Tree  ----------------------------------------

Given a Binary Tree, find and return the diameter of input binary tree.
Diameter is - largest count of nodes between any two leaf nodes in the binary tree (both the leaf nodes 
are inclusive).

#### Input format :
    Elements in level order form (separated by space)
    (If any node does not have left or right child, take -1 in its place)
#### Output Format :
    diameter

#### Sample Input :
    8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
#### Sample Output :
    7
"""

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''def height(node):
    if node is None: 
        return 0 
    return 1 + max(height(node.left) ,height(node.right)) 
def diameter(root):  
    if root is None: 
        return 0
    lheight = height(root.left) 
    rheight = height(root.right) 
  
    ldiameter = diameter(root.left) 
    rdiameter = diameter(root.right) 
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))
'''
def diameterNDepth(root):

    dia, depth=0,0
    if root==None:
        return dia,depth

    leftDia,leftDepth=diameterNDepth(root.left)
    rightDia,rightDepth=diameterNDepth(root.right)

    depth=1+ max(leftDepth,rightDepth)

    diameterWithRoot=leftDepth + rightDepth+1

    dia=max(leftDia,rightDia,diameterWithRoot)

    return dia,depth

def diameter(root):
    dia,depth=diameterNDepth(root)
    return dia

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
print(diameter(root))
