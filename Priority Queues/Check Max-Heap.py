"""
-------------------------  Check Max-Heap  ---------------------------

Given an array of integers, check whether it represents max-heap or not.
Return true or false.

#### Input Format :
    Line 1 : An integer N i.e. size of the array
    Line 2 : N integers which are elements of the array, separated by spaces

#### Output Format :
    true if it represents max-heap and false if it is not a max-heap

#### Constraints :
    1 <= N <= 10^5
    1 <= Ai <= 10^5

"""

import heapq
def checkMaxHeap(lst):
    heap=lst[::]
    heapq._heapify_max(heap)
    if heap==lst:
        return True
    else:
        return False
    '''
    n=len(lst)
    parentIndex=0
    leftChildIndex=2*parentIndex+1
    rightChildIndex=2*parentIndex+2
    while leftChildIndex<n:
        
        if lst[parentIndex]<lst[leftChildIndex]:
            return False
        if rightChildIndex<n and lst[parentIndex]<lst[rightChildIndex]:
            return False'''
                
    #return True

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
