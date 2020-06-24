#!/usr/bin/env python
# coding: utf-8

""" ## Push Zeros to end
 You have been given a random integer array/list(ARR) of size N. You have been required to push all the zeros that are present in the array/list to the end of it. Also, make sure to maintain the relative order of the non-zero elements.
 ##### Note:
 1.Change in the input array/list itself. You don't need to return or print the elements.    
 2.You need to do this in one scan of array only. Don't use extra space.
 #### Input format :
 The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.<br>
 
 First line of each test case or query contains an integer 'N' representing the size of the array/list.<br>
 
 Second line contains 'N' single space separated integers representing the elements in the array/list.<br>
 #### Output format :
 For each test case, print the elements of the array/list in the desired order separated by a single space.<br>
 
 Output for every test case will be printed in a separate line.
 
# #### Constraints :
 1 <= t <= 10^2    
 0 <= N <= 10^5    
 Time Limit: 1 sec
 
 #### Sample Input :
 2    
 5    
 0 3 0 2 0    
 4    
 9 0 0 8 2 
 #### Sample Output :
 3 2 0 0 0    
 9 8 2 0 0 

 ### Approach
 Before we discuss the approach for this question let’s see what exactly the question
 requires us to do. It seems that we have to push all the 0s in the array towards the end
 of the array. It can also be looked at as pushing all the non-zero elements in the array
 towards the beginning of the array.   

 So let’s use a two pointer approach to solve this problem. We’ll maintain two pointers,
 ‘current’ and ‘nonZeroPos’. ‘current’ will be used to iterate through the array and
 ‘nonZeroPos’ will be used to decide the next position where the next non zero element
 will go to. Both pointers will be initialised with 0. 

 Now, we’ll iterate through the array. If we encounter a 0, we’ll just increase ‘current’ by 1.
 However, if we encounter a non-zero value, we put that element to ‘nonZeroPos’ and
 bring ‘nonZeroPos’s element to the current index. Basically we’re doing
 swap(arr[current], arr[nonZeroPos]). And after this, we’ll increase both
 ‘current’ and ‘nonZeroPos’ by 1. This will ensure that every non-zero element gets
 pushed towards the front of the array with their order maintained.
""" 

from sys import stdin 
def pushZerosAtEnd(arr, n) : 
    nonZero = 0 
    for i in range(n): 
        if arr[i] != 0 : 
            temp = arr[i] 
            arr[i] = arr[nonZero] 
            arr[nonZero] = temp 
            nonZero += 1 
            
def takeInput() : 
    n = int(stdin.readline().rstrip()) 
    if n == 0: 
        return list(), 0 
    arr = list(map(int, stdin.readline().rstrip().split())) 
    return arr, n 

def printList(arr, n) : 
    for i in range(n) : 
        print(arr[i], end = " ") 
    print() 
    
#main 
t = int(stdin.readline().strip())
while t > 0 : 
    arr, n = takeInput() 
    pushZerosAtEnd(arr, n) 
    printList(arr, n) 
    t -= 1

