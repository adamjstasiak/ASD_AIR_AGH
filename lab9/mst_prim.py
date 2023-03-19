from math import inf
import graf_mst

class Node:
    def __init__(self,vertex) -> None:
        self.vertex = vertex

    def __eq__(self,other) -> bool:
        return self.vertex == other.vertex

    def __hash__(self) -> int:
        return hash(self.vertex)
    def __str__(self) -> str:
        return str(self.vertex)

class Edge:
    def __init__(self,vertex1,vertex2,value) -> None:
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.value = value


    def __str__(self):
        return str(self.vertex1)  + '->' + str(self.vertex2) + ':' + str(self.value)

class Graf_list:
    def __init__(self) -> None:
        self.list = []
        self.list_vertex = []
        self.dict_vertex = {}
        self.graf_size = 0

    def insertVertex(self,vertex): 
        self.list_vertex.append(vertex)
        self.dict_vertex[vertex] = len(self.list_vertex)-1
        self.list.append([])

    def insertEdge(self,vertex1,vertex2,value):
        vertex1 = Node(vertex1)
        vertex2 = Node(vertex2)
        if vertex1 not in self.list_vertex:
            self.insertVertex(vertex1)
        if vertex2 not in self.list_vertex:
            self.insertVertex(vertex2)    
        index1 = self.getVertexIdx(vertex1)
        index2 = self.getVertexIdx(vertex2)
        edge = Edge(vertex1, vertex2,value)
        self.list[index1].append(edge)
        self.graf_size += 1
        edge1 = Edge(vertex2, vertex1,value)
        self.list[index2].append(edge1)


    def getVertex(self,vertexIdx):
        for key, index in self.dict_vertex.items():
            if index == vertexIdx:
                return key
    
    def getVertexIdx(self,vertex):
        return self.dict_vertex[vertex]

    def order(self):
        return len(self.list_vertex)
    
    def size(self):
        return self.graf_size

    def neighbours(self,vertexIdx):
        return self.list[vertexIdx]

    def edges(self):
        edges = []
        for i in range(len(self.list)):
            for j in self.list[i]:
                    edges.append((self.getVertex(i).key,self.getVertex(j).key))
        return edges

def MST_prim(graf:Graf_list,index):
    size = graf.order()
    intree = [0 for i in range(size)]
    distance = [inf for i in range(size)]
    parent = [-1 for i in range(size) ]
    mst = Graf_list()
    suma = 0
    for i in graf.dict_vertex.keys():
        mst.insertVertex(Node(i))
    current_vertex = index
    while intree[current_vertex] == 0:
        intree[current_vertex] = 1
        neighbours = graf.neighbours(current_vertex)
        for i in neighbours:
            new_vertex = graf.getVertexIdx(i.vertex2)
            if i.value < distance[new_vertex] and intree[new_vertex] == 0:
                distance[new_vertex] = i.value
                parent[new_vertex] = current_vertex
        mini = inf
        current_vertex = 0
        for v in graf.list_vertex:
            if intree[graf.getVertexIdx(v)] == 0 and distance[graf.getVertexIdx(v)] <mini:
                mini = distance[graf.getVertexIdx(v)]
                current_vertex = graf.getVertexIdx(v)
        if mini != inf:
            suma += mini
            next_vertex = graf.getVertex(current_vertex)
            parent_v = graf.getVertex(parent[current_vertex])
            mst.list[current_vertex].append(Edge(new_vertex,parent_v,mini))
            mst.list[parent[current_vertex]].append(Edge(parent_v,next_vertex,mini))
    return mst,suma



def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for edge in nbrs:
            print(edge.vertex2, edge.value, end=";")
        print()
    print("-------------------")
    
def main():

    test_graf = Graf_list()
    for v1, v2, w in graf_mst.graf:
        test_graf.insertEdge(v1, v2, w)
  
    mst,suma = MST_prim(test_graf,1)
    printGraph(mst)
    print(suma)
if __name__ =="__main__":
    main()