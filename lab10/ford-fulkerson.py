
from math import inf

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
    def __init__(self,vertex1,vertex2,capacity,flow=0,isResidual=True) -> None:
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.capacity = capacity
        self.flow = flow
        self.residual = capacity
        self.isResidual = isResidual

    def __str__(self):
        return str(self.vertex1)  + '->' + str(self.vertex2) + ':' + str(self.capacity) + ' ' + str(self.flow) + ' '+ str(self.residual) + ' ' + str(self.isResidual) 

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

    def insertEdge(self,vertex1,vertex2,capacity,flow=0):
        vertex1 = Node(vertex1)
        vertex2 = Node(vertex2)
        if vertex1 not in self.list_vertex:
            self.insertVertex(vertex1)
        if vertex2 not in self.list_vertex:
            self.insertVertex(vertex2)    
        index1 = self.getVertexIdx(vertex1)
        index2 = self.getVertexIdx(vertex2)
        edge = Edge(vertex1, vertex2,capacity,flow,isResidual=False)
        self.list[index1].append(edge)
        self.graf_size += 1
        edge1 = Edge(vertex2, vertex1,capacity,flow,isResidual=True)
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


def BFS(graf:Graf_list,index):
    size = graf.order()
    visited = [0 for i in range(size)]
    parent = [-1 for i in range(size)]
    queue = []
    queue.append(index)
    visited[index] = 1
    while queue != []:
        current_index = queue.pop(0)
        neighbours = graf.neighbours(current_index)
        for i in neighbours:
            new_vertex = graf.getVertexIdx(i.vertex2)
            if visited[new_vertex] != 1 and i.residual > 0 and not i.isResidual:
                visited[new_vertex] = 1
                queue.append(new_vertex)
                parent[new_vertex] = current_index
    return parent

def path_analisys(graf:Graf_list,start_vertex,end_vertex,parent):
    min_flow = inf
    current_index = end_vertex
    if parent[current_index] == -1:
        min_flow = 0
        return min_flow
    while current_index != start_vertex:
        neighbours = graf.neighbours(parent[current_index])
        for i in neighbours:
            new_vertex = graf.getVertexIdx(i.vertex2)
            if new_vertex == current_index:
                if i.residual < min_flow and not i.isResidual:
                    min_flow = i.residual
                current_index = parent[current_index]
    return min_flow

def path_augmentation(graf:Graf_list,start_vertex,end_vertex,parent,min_flow):
    current_index = end_vertex
    if parent[current_index] == -1:
        min_flow = 0
        return min_flow
    while current_index != start_vertex:
        neighbours = graf.neighbours(parent[current_index])
        for i in neighbours:
            new_vertex = graf.getVertexIdx(i.vertex2)
            if new_vertex == current_index:
                if not i.isResidual:
                    i.flow += min_flow
                    i.residual -= min_flow
                    
                elif i.isResidual:
                    i.residual += min_flow
        current_index = parent[current_index]  
    return min_flow  


def Ford_Fulkerson(graf:Graf_list,start_vertex,end_vertex):
    start_vertex_id = graf.getVertexIdx(start_vertex)
    end_vertex_id = graf.getVertexIdx(end_vertex)
    parent = BFS(graf,start_vertex_id)
    min_flow = path_analisys(graf,start_vertex_id,end_vertex_id,parent)
    sum_flow = min_flow
    while min_flow > 0 :
        path_augmentation(graf,start_vertex_id,end_vertex_id,parent,min_flow)
        parent = BFS(graf,start_vertex_id)
        min_flow = path_analisys(graf,start_vertex_id,end_vertex_id,parent)
        sum_flow += min_flow
    return sum_flow


def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for edge in nbrs:
            print(edge.vertex2, edge.capacity,edge.flow,edge.residual,edge.isResidual, end=";")
        print()
    print("-------------------")
        

def main():
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]


    test_graf_0 = Graf_list()
    for v1,v2, c in graf_0:
        test_graf_0.insertEdge(v1,v2,c)

    print(Ford_Fulkerson(test_graf_0,Node('s'),Node('t')))
    printGraph(test_graf_0)
    print()
    test_graf_1 = Graf_list()
    for v1,v2, c in graf_1:
        test_graf_1.insertEdge(v1,v2,c)
    print(Ford_Fulkerson(test_graf_1,Node('s'),Node('t')))    
    printGraph(test_graf_1)
    print()
    test_graf_2 = Graf_list()
    for v1,v2, c in graf_2:
        test_graf_2.insertEdge(v1,v2,c)
    print(Ford_Fulkerson(test_graf_2,Node('s'),Node('t'))) 
    printGraph(test_graf_2)
    print()
    test_graf_3 = Graf_list()
    for v1,v2, c in graf_3:
        test_graf_3.insertEdge(v1,v2,c)
    print(Ford_Fulkerson(test_graf_3,Node('s'),Node('t')))     
    printGraph(test_graf_3)


if __name__ =="__main__":
    main() 