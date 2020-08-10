"""
-----------------------------  Pair Sum To 0  -------------------------------

Given a random integer array A of size N. Find and print the pair of elements 
in the array which sum to 0.
Array A can contain duplicate elements.
While printing a pair, print the smaller element first.
That is, if a valid pair is (6, -6) print "-6 6". There is no constraint that 
out of 5 pairs which have to be printed in 1st line. You can print pairs in 
any order, just be careful about the order of elements in a pair.

#### Input format :
    Line 1 : Integer N (Array size)
    Line 2 : Array elements (separated by space)

#### Output format :
    Line 1 : Pair 1 elements (separated by space)
    Line 2 : Pair 2 elements (separated by space)
    Line 3 : and so on

#### Constraints :
    0 <= N <= 10^4

#### Sample Input:
    5
    2 1 -2 2 3
#### Sample Output :
    -2 2
    -2 2
"""

def freqMap(l): 
    map = {} 
    for num in l: 
        if num in map: 
            map[num] += 1 
        else: map[num] = 1 
    return map 

def pairSum0(l):
    m = freqMap(l) 
    for num in m: 
        if num>=0 and -num in m: 
            for _ in range(0, m[num]*m[-num]): 
                print(-num, num)
                
n=int(input()) 
l=list(int(i) for i in input().strip().split(' ')) 
pairSum0(l)