"""
--------------------------  Min Cost Path Problem  -----------------------------------

Given an integer matrix of size m*n, you need to find out the value of minimum 
cost to reach from the cell (0, 0) to (m-1, n-1).

From a cell (i, j), you can move in three directions : (i+1, j), (i, j+1) and (i+1, j+1).
Cost of a path is defined as the sum of values of each cell through which path passes.

Input Format :
    Line 1 : Two integers, m and n
    Next m lines : n integers of each row (separated by space)

Output Format :
    Minimum cost

Constraints :
    1 <= m, n <= 20

Sample Input 1 :
    3 4
    3 4 1 2
    2 1 8 9
    4 7 8 1
Sample Output 1 :
    13
"""


import sys
def minCost(cost,n,m):
    dp=[[sys.maxsize for j in range(n+1)] for i in range(m+1)]
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i==m-1 and j==n-1:
                dp[i][j]=cost[i][j]
            else:
                ans1=dp[i+1][j]
                ans2=dp[i][j+1]
                ans3=dp[i+1][j+1]
                dp[i][j]=cost[i][j] + min(ans1,ans2,ans3)
    return dp[0][0]

li=[int(ele) for ele in input().split()]
cost=[[int(ele) for ele in input().split()] for j in range(li[0])]
print(minCost(cost,li[1],li[0]))