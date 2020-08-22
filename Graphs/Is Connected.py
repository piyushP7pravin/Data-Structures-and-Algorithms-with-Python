"""
-------------------------------------- Is Connected ?  ------------------------------------

Given an undirected graph G(V,E), check if the graph G is connected graph or not.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.

Input Format :
    Line 1: Two Integers V and E (separated by space)
        Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting 
        that there exists an edge between Vertex 'a' and Vertex 'b'.

Output Format :
    "true" or "false"

Constraints :
    2 <= V <= 1000
    1 <= E <= 1000

Sample Input 1:
    4 4
    0 1
    0 3
    1 2
    2 3
Sample Output 1:
    true

Sample Input 2:
    4 3
    0 1
    1 3 
    0 3
Sample Output 2:
    false 
Sample Output 2 Explanation
    The graph is not connected, even though vertices 0,1 and 3 are connected to each other 
    but there isn’t any path from vertices 0,1,3 to vertex 2. 
"""

class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]
        
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
        
    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0
        
    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2]>0 else False
    
    def __str__(self):
        return str(self.adjMatrix)
    
    def __dfsHelper(self,sv,visited):
        visited[sv]=True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i]>0 and visited[i] is False:
                self.__dfsHelper(i,visited)
    def dfs(self):
        visited=[False for i in range(self.nVertices)]
        self.__dfsHelper(0,visited)
        for j in range(self.nVertices):
            if visited[j] is False:
                return False
        else:
            return True
    
    def isConnected(self):
        return self.dfs()
        
#main    
ve=[int(ele) for ele in input().split()]
g=Graph(ve[0])
for i in range(ve[1]):
    el=[int(ele) for ele in input().split()]
    g.addEdge(el[0],el[1])
if g.isConnected():
    print("true")
else:
    print("false")