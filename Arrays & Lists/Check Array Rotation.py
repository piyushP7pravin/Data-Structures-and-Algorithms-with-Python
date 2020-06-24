""" --------------------------- Check Array Rotation ---------------------------

You have been given an integer array/list(ARR) of size N. It has been sorted(in increasing order) and then rotated by some number 'K' in the clockwise direction.
Your task is to write a function that returns the value of 'K', that means, the index from which the array/list has been rotated.

#### Input format :
        The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

        First line of each test case or query contains an integer 'N' representing the size of the array/list.

        Second line contains 'N' single space separated integers representing the elements in the array/list.

#### Output Format :
    For each test case, print the value of 'K' or the index from which which the array/list has been rotated.

    Output for every test case will be printed in a separate line.

#### Constraints :
    1 <= t <= 10^2
    0 <= N <= 10^5
    Time Limit: 1 sec

#### Sample Input:
        2
        5
        3 6 8 9 10
        4
        10 20 30 1
#### Sample Output :
        0
        3

"""

from sys import stdin 

def arrayRotateCheck(arr, n): 
    for i in range(n - 1): 
        if(arr[i] > arr[i + 1]): 
            return (i + 1) 
    return 0 
    
def takeInput() : 
    n = int(stdin.readline().rstrip()) 
    if n == 0: 
        return list(), 0 
    arr = list(map(int, stdin.readline().rstrip().split(" "))) 
    return arr, n 
    
#main 
t = int(stdin.readline().rstrip()) 
while t > 0 : 
    arr, n = takeInput() 
    print(arrayRotateCheck(arr, n)) 
    t -= 1