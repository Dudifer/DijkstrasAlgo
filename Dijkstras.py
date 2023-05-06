'''The idea we learned is given a graph and starting vertex, provide the shortest path to all other vertices from s.
In class, we used a Priority Queue that prioritized minimal edge weights. Since I do not know of a priority queue
data structure in Python, I'll just use min and sort as needed.

I'll be using a dictionary as my prepresentation of a weighted, directed graph G. G[vertex] returns a list of 2 element 
tuples, the first element being the adjacent vertex, the second element representing the cost of travel from vertex.'''

class vertex:
    def __init__(self,id=0,parent=0,cost=float('inf')):
        self.id=id
        self.p=parent
        self.c=cost
    def __lt__(self, v):
        if isinstance(v,vertex):
            return self.c<=v.c
        else:
            print("bro ur not comparing w another vertex lol")
            return False
    def __gt__(self, v):
        if isinstance(v,vertex):
            return self.c>v.c
        else:
            print("bro ur not comparing w another vertex lol")
            return False
    def __str__(self):
        return str(self.id)

class wGraph: 
    def __init__(self, nvertices=7, Eweights=[(1,2,30),(2,3,22),(3,7,14),(6,7,105),(1,6,7),(1,7,68),(1,4,24),(2,4,7),(2,5,20),(3,4,25),(3,5,4),(5,7,11)], directed=False):
        self.Vcon=nvertices+1
        self.numE=len(Eweights)

        self.V=[vertex(id=a) for a in range(1,self.Vcon)]
        self.W={{(e[0],e[1]): e[2]} for e in Eweights}
        self.E=list(self.W.keys())
        self.d=directed
        for e in Eweights:
            self.E.append((e[0],e[1]))
            self.W.update({(e[0],e[1]): e[2]})
            if not directed: self.W.update({(e[1],e[0]): e[2]})
    def getGraph(self):
        return self.V, self.E
    
    def copy_vertices(self):
        V=[vertex(id=a) for a in range(1,self.Vcon)]
        return V
    def asAdj(self):
        adj={v:[] for v in self.V}
        for e in self.E:
            if self.d: adj[e[0]].append(e[1])
            else:
                adj[e[0]].append(e[1])
                adj[e[1]].append(e[0])
        return adj
    
    def weight(self,f,t):
        return self.W[f,t]
class Queue():
    def __init__(self, descending=False):
        self.d=descending
        self.q=[]
    def getq(self):
        return self.q
    def enq(self, v):
        self.q.append(v)
        self.q.sort(reverse=self.d)
        return self.q







def Dijkstra(G=wGraph(),sv_index=1):
    V,E=G.getGraph()
    Adj=G.asAdj()
    V[sv_index].c=0
    Q=Queue()
    for v in V:
        Q.enq(v)
    

    

    


    
