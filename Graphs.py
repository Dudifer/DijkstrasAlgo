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
        return 'vertex id: '+ str(self.id)+'\nparent id: ' +str(self.p.id)+'\ncost from start: '+ str(self.c)

class wGraph: 
    def __init__(self, nvertices=7, Eweights=[(1,2,30),(2,3,22),(3,7,14),(6,7,105),(1,6,7),(1,7,68),(1,4,24),(2,4,7),(2,5,20),(3,4,25),(3,5,4),(5,7,11)], directed=False):
        self.Vcon=nvertices+1
        self.numE=len(Eweights)

        self.V=[vertex(id=a) for a in range(1,self.Vcon)]
        self.E=[]
        self.W={}
        self.d=directed
        for e in Eweights:
            self.E.append((e[0],e[1]))
            self.W.update({str((e[0],e[1])): e[2]})
            if not directed: self.W.update({str((e[1],e[0])): e[2]})
    def getGraph(self):
        return self.V, self.E
    
    def copy_vertices(self):
        V=[vertex(id=a) for a in range(1,self.Vcon)]
        return V
    def asAdj(self):
        adj={v.id:[] for v in self.V}
        for e in self.E:
            if self.d: adj[e[0]].append(e[1])
            else:
                adj[e[0]].append(e[1])
                adj[e[1]].append(e[0])
        return adj
    
    def weight(self,f,t):
        return self.W[str((f.id,t.id))]
