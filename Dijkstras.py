'''The idea we learned is given a graph and starting vertex, provide the shortest path to all other vertices from s.
In class, we used a Priority Queue that prioritized minimal edge weights. Since I do not know of a priority queue
data structure in Python, I'll just use min and sort as needed.

I'll be using a dictionary as my prepresentation of a weighted, directed graph G. G[vertex] returns a list of 2 element 
tuples, the first element being the adjacent vertex, the second element representing the cost of travel from vertex.'''
from Graphs import *
class Queue():
    def __init__(self, descending=True):
        self.d=descending
        self.q=[]
    def getq(self):
        return self.q
    def dq(self):    
        return(self.q.pop())
    def enq(self, v):
        self.q.append(v)
        self.q.sort(reverse=self.d)
        return self.q
    def update(self):
        self.q.sort(reverse=self.d)



def Dijkstra(G=wGraph(),sv_index=1):
    V,E=G.getGraph()
    Adj=G.asAdj()
    V[sv_index].c=0
    Q=Queue()
    for v in V:
        Q.enq(v)
    y=[]
    #q=Q.getq()
    for i in range(len(V)):
        f=Q.dq()
        y.append(f)
        for t in list(set(Adj[f.id])-set(y)):
            cost=G.weight(f,t)
            if f.c+cost<t.c: 
                t.p=f
                t.c=f.c+cost
                Q.update()
    print(V.pop(sv_index))
    for a in V:
        print(a)
Dijkstra()
            
        
    


    

    


    
