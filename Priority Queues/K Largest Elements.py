"""
-----------------------  K Largest Elements  --------------------------

You are given with an integer k and an array of integers that contain 
numbers in random order. Write a program to find k largest numbers from 
given array. You need to save them in an array and return it.

Time complexity should be O(nlogk) and space complexity should be not more than O(k).
Order of elements in the output is not important.

#### Input Format :
    Line 1 : Size of array (n)
    Line 2 : Array elements (separated by space)
    Line 3 : Integer k

#### Output Format :
    k largest elements

#### Sample Input :
    13
    2 12 9 16 10 5 3 20 25 11 1 8 6 
    4
#### Sample Output :
    12
    16
    20
    25
"""

import heapq
def kLargest(lst, k):
    heap=lst[:k]
    heapq.heapify(heap)
    n=len(lst)
    for i in range(k,n):
        if heap[0]<lst[i]:
            heapq.heapreplace(heap,lst[i])
    return heap

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')
