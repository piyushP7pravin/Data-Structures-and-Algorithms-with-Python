"""
Longest subset zero sum

Given an array consisting of positive and negative integers, find the 
length of the longest subarray whose sum is zero.

NOTE : 
    You have to return the length of longest subarray .

#### Input Format :
    Line 1 : Contains an integer N i.e. size of array
    Line 2 : Contains N elements of the array, separated by spaces

#### Output Format
    Line 1 : Length of longest subarray 

#### Constraints:
    0 <= N <= 10^8

#### Sample Input :
    10 
    95 -97 -387 -435 -5 -70 897 127 23 284
#### Sample Output :
    5
"""


def subsetSum(l):
#Implement Your Code Here
    n=len(l)
    sum=[0]*n
    sum[0]=l[0]
    m={l[0]:0}
    start, end=-1,-2
    if sum[0]==0:
        start, end=0,0
    for i in range(1,n):
        sum[i]=sum[i-1]+l[i]
        if sum[i]==0:
            start, end=0,i
        elif sum[i] in m:
            if i-m[sum[i]]>end-start+1:
                start,end=m[sum[i]]+1,i
        else:
            m[sum[i]]=i
    return start,end

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
#finalLen= subsetSum(l)
#print(finalLen)
start,end=subsetSum(l)
print(end-start+1)

