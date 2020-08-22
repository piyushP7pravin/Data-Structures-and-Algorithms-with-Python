"""
Get Path - BFS

Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), find and print 
the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.

Find the path using BFS and print the shortest path available.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.

Note : 
    Save the input graph in Adjacency Matrix.

Input Format :
    Line 1: Two Integers V and E (separated by space)
        Next E lines : Two integers a and b, denoting that there exists an edge between vertex a 
        and vertex b (separated by space)
    Line (E+2) : Two integers v1 and v2 (separated by space)

Output Format :
    Path from v1 to v2 in reverse order (separated by space)

Constraints :
    2 <= V <= 1000
    1 <= E <= 1000
    0 <= v1, v2 <= V-1

Sample Input 1 :
    4 4
    0 1
    0 3
    1 2
    2 3
    1 3
Sample Output 1 :
    3 0 1
"""

import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def removeEdge(self,v1,v2):
        if self.containEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    
    def containEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    
    def getPath(self,v1,v2):
        visited = [False for i in range(self.nVertices)]
        q = queue.Queue()
        d = {}
        k = None
        
        q.put(v1)
        while not(q.empty()):
            front = q.get()
            visited[front] = True
            for i in range(self.nVertices):
                if visited[i] is False and self.adjMatrix[front][i] > 0:
                    q.put(i)
                    d[i] = front
                    visited[i] = True
                    #print(i)
                    #print(front)
                    if i == v2:                  
                        k = i
                        break
                #if c == 0:
                 #   break
                    #d[k] =front
        if k is None:
            return None
        l = [k]
      #  print(d[k])
        while k is not v1:
            l.append(d[k])
            k = d[k]
       # while k is not v1:
        #    s = d.get(k)
         #   l.append(s)
          #  k = s
        
        return l 
   
#main
V, E = (int(x) for x in input().split()) 
G = Graph(V)
for i in range(E):
    v1,v2 = (int(x) for x in input().split()) 
    G.addEdge(v1,v2)

v1,v2 = (int(x) for x in input().split()) 
s = G.getPath(v1,v2)
if s is None:
    print()
else:
    print(*s)
