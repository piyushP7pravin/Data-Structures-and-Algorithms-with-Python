"""
----------------------------------  Longest Consecutive Sequence  -----------------------------

You are given an array of unique integers that contain numbers in random order. Write a program 
to find the longest possible sequence of consecutive numbers using the numbers from given array.
You need to return the output array which contains consecutive elements. Order of elements in 
the output is not important.

Best solution takes O(n) time.

If two sequences are of equal length then return the sequence starting with the number whose 
occurrence is earlier in the array.

#### Input Format :
    Line 1 : Integer n, Size of array
    Line 2 : Array elements (separated by space)

#### Constraints :
    0 <= n <= 10^8

#### Sample Input 1 :
    13
    2 12 9 16 10 5 3 20 25 11 1 8 6 
#### Sample Output 1 :
    8 
    9 
    10 
    11 
    12

#### Sample Input 2 :
    7
    3 7 2 1 9 8 41
#### Sample Output 2 :
    7
    8
    9
    Explanation: Sequence should be of consecutive numbers. Here we have 2 sequences 
    with same length i.e. [1, 2, 3] and [7, 8, 9], but output should be [7, 8, 9] 
    because the starting point of [7, 8, 9] comes first in input array.

#### Sample Input 3 :
    7
    15 24 23 12 19 11 16
#### Sample Output 3 :
    15 
    16
"""

def longestConsecutiveSubsequence(l): 

    m = {l[i]:i for i in range(len(l)-1, -1, -1)} 

    visited = {} 

    start, end = l[0], l[0] 
    startM, endM = start, end 

    for num in l: 
        if num not in visited: 
            visited[num] = True 
            start, end = num, num 

            while start-1 in m: 
                start -= 1 
                visited[start] = True 

            while end+1 in m: 
                end += 1 
                visited[end] = True 

            if (endM-startM+1 < end-start+1) or ((endM-startM+1 == end-start+1) and (m[start] < m[startM])): 
                startM, endM = start, end 
                
    return startM, endM

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
start,end = longestConsecutiveSubsequence(l)
for num in range(start,end+1):
    print(num)