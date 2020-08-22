"""
---------------------------------------  All connected components  -------------------------------------

Given an undirected graph G(V,E), find and print all the connected components of the given graph G.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
You need to take input in main and create a function which should return all the connected components. 
And then print them in the main, not inside function.
Print different components in new line. And each component should be printed in increasing order 
(separated by space). Order of different components doesn't matter.

Input Format :
    Line 1: Two Integers V and E (separated by space)
        Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting that there exists 
        an edge between Vertex 'a' and Vertex 'b'.

Output Format :
    Different components in new line

Constraints :
    2 <= V <= 1000
    1 <= E <= 1000

Sample Input 1:
    4 2
    0 1
    2 3
Sample Output 1:
    0 1 
    2 3 
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
    
    def __helper(self,sv,visited,li):
        visited[sv]=True
        li.append(sv)
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i]>0 and visited[i] is False:
                
                self.__helper(i,visited,li)
        return li
                
    def connectedComponent(self):
        visited=[False for i in range(self.nVertices)]
        final_list=[]
        
        for j in range(self.nVertices):
            if visited[j] is False:
                li=[]
                final_list.append(self.__helper(j,visited,li))
        return final_list
            
#main
ve=[int(ele) for ele in input().split()]
g=Graph(ve[0])
for i in range(ve[1]):
    el=[int(ele) for ele in input().split()]
    g.addEdge(el[0],el[1])
cc=g.connectedComponent()

for i in cc:
    i.sort()
    print(*i)