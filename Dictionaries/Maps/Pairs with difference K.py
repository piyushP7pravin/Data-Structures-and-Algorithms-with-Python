"""
-------------------------------  Pairs with difference K  ------------------------------

You are given with an array of integers and an integer K. Write a program to find and 
print all pairs which have difference K.

Take difference as absolute.

Input Format :
    Line 1 : Integer n, Size of array
    Line 2 : Array elements (separated by space)
    Line 3 : K

Output format :
    Print pairs in different lines (pair elements separated by space). In a pair, smaller 
    element should be printed first.
    (Order of different pairs is not important)

Constraints :
    0 <= n <= 10^4

Sample Input 1 :
    4 
    5 1 2 4
    3
Sample Output 1 :
    2 5
    1 4

Sample Input 2 :
    4
    4 4 4 4 
    0
Sample Output 2 :
    4 4
    4 4
    4 4
    4 4
    4 4
    4 4
"""



def printPairDiffK(l, k):

    if k<0:
        k*=-1
    d={}
    for num in l:
        if num+k in d:
            for i in range(d[num+k]):
                print(num,num+k)
        if k!=0 and num-k in d:
            for i in range(d[num-k]):
                print(num-k,num)
        if num in d:
            d[num]+=1
        else:
            d[num]=1


n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
printPairDiffK(l, k)