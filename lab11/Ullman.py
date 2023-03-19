

import numpy as np
from copy import deepcopy

class Node:
    def __init__(self,vertex) -> None:
        self.vertex = vertex

    def __eq__(self,other) -> bool:
        return self.vertex == other.vertex

    def __hash__(self) -> int:
        return hash(self.vertex)

    def __str__(self) -> str:
        return str(self.vertex)


class Matrix_graf:
    def __init__(self) -> None:
        self.matrix = []
        self.list_vertex = []
        self.dict_vertex = {}
        self.graf_size = 0

    def insertVertex(self,vertex): 
        self.list_vertex.append(vertex)
        self.dict_vertex[vertex] = len(self.list_vertex)-1
        if len(self.matrix) == 0:
            self.matrix.append([0])
        else:
            for i in self.matrix:
                i.append(0)
            self.matrix.append([0 for i in range(len(self.matrix[0]))])    


    def insertEdge(self,vertex1,vertex2,wage):
        if vertex1 not in self.list_vertex:
            self.insertVertex(vertex1)
        if vertex2 not in self.list_vertex:
            self.insertVertex(vertex2)    
        index1 = self.getVertexIdx(vertex1)
        index2 = self.getVertexIdx(vertex2)
        self.matrix[index1][index2] = wage
        self.matrix[index2][index1] = wage
        self.graf_size += 1


    def deleteVertex(self,vertex):
        index = self.getVertexIdx(vertex)
        self.list_vertex.remove(vertex)
        self.dict_vertex.pop(vertex)
        for i in range(len(self.list_vertex)):
            self.dict_vertex[self.list_vertex[i]] = i 
        self.matrix.pop(index)
        for ed in self.matrix:
            ed.pop(index)

      

    def deleteEdge(self,vertex1,vertex2):
        index1 = self.getVertexIdx(vertex1)
        index2 = self.getVertexIdx(vertex2)
        self.matrix[index1][index2] = 0
        self.graf_size -= 1


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
        neighbours = []
        for i in range(len(self.list_vertex)):
            if self.matrix[vertexIdx][i] == 1:
                neighbours.append(i)
        return neighbours
    def edges(self):
        edges = []
        for i in range(len(self.matrix)):
            for j in range(i):
                if self.matrix[i][j] == 1:
                    edges.append((self.getVertex(i).key,self.getVertex(j).key))
        return edges

    def convert_to_numpy(self):
        return np.array(self.matrix)


def create_M(G,P):
    size_G = G.shape
    size_P = P.shape
    M = np.zeros((size_P[0],size_G[1]))
    return M

def prune(G,P,M):
    size_m = M.shape
    indexes =  [] 
    for i in range(size_m[0]):
        for j in range(size_m[1]):
            if M[i][j] == 1:
                indexes.append((i,j))
    changed = True
    while changed:
        changed = False
        for i,j in indexes:
            neighbours_viP = []
            for k in range(len(P[i])):
                if P[i][k] == 1:
                    neighbours_viP.append(k)
            neighbours_vjG = []
            for k in range(len(G[j])):
                if G[j][k] == 1:
                    neighbours_vjG.append(k)
            exist = False
            for x in neighbours_viP:
                for y in neighbours_vjG:
                    if M[x][y] == 1:
                        exist = True
            if exist is False:
                changed = True
                M[i][j] = 0
                indexes.pop(indexes.index((i,j)))

def ullman_1(G,P,M=None,used_columns=[],current_row=0,solutions = 0 ,iteration = 0):
    if M is None:
        M = create_M(G,P)
    size_m = M.shape

    if current_row == size_m[0]:
        if np.array_equal(P,np.dot(M,np.transpose(np.dot(M,G)))):
            return solutions+1,iteration
        else:
            return solutions,iteration
    M_copy = deepcopy(M)
    for j in range(size_m[1]):
        if j not in used_columns:
            for i in range(size_m[1]):
                M_copy[current_row][i] = 0
            M_copy[current_row][j] = 1
            used_columns.append(j)
            solutions,iteration = ullman_1(G,P,M_copy,used_columns,current_row+1,solutions, iteration)
            iteration += 1
            used_columns.pop()
    return solutions,iteration
    
    

def ullman_2(G,P,M0,M=None,used_columns=[],current_row=0,solutions = 0 ,iteration = 0):
    if M is None:
        M = create_M(G,P)
    size_m = M.shape

    if current_row == size_m[0]:
        if np.array_equal(P,np.dot(M,np.transpose(np.dot(M,G)))):
            return solutions+1,iteration
        else:
            return solutions,iteration
    M_copy = deepcopy(M)
    for j in range(size_m[1]):
        if j not in used_columns and M0[current_row][j] == 1:
            for i in range(size_m[1]):
                M_copy[current_row][i] = 0
            M_copy[current_row][j] = 1
            used_columns.append(j)
            solutions ,iteration = ullman_2(G,P,M0,M_copy,used_columns,current_row+1,solutions, iteration)
            used_columns.pop()
            iteration += 1
    return solutions,iteration

def ullman_3(G,P,M0,M=None,used_columns=[],current_row=0,solutions = 0 ,iteration = 0):
    if M is None:
        M = create_M(G,P)
    size_m = M.shape

    if current_row == size_m[0]:
        if np.array_equal(P,np.dot(M,np.transpose(np.dot(M,G)))):
            return solutions+1,iteration
        else:
            return solutions,iteration
    M_copy = deepcopy(M)
    if current_row == size_m[0] - 1:
        prune(G,P,M_copy)
    if current_row >=1:
        for row in M_copy[:current_row]:
            if row.sum() == 0:
                return solutions,iteration
    for j in range(size_m[1]):
        if j not in used_columns and M0[current_row][j] == 1:
            for i in range(size_m[1]):
                M_copy[current_row][i] = 0
            M_copy[current_row][j] = 1
            used_columns.append(j)
            solutions ,iteration = ullman_3(G,P,M0,M_copy,used_columns,current_row+1,solutions, iteration)
            used_columns.pop()
            iteration += 1
    return solutions,iteration

def main():

    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]


    test_graph_G = Matrix_graf()
    for v1,v2,w in graph_G:
        test_graph_G.insertEdge(Node(v1),Node(v2),w)
    

    test_graph_P = Matrix_graf()
    for v1,v2,w in graph_P:
        test_graph_P.insertEdge(Node(v1),Node(v2),w)

    M0 = np.zeros((test_graph_P.order(),test_graph_G.order()))
    for i in range(M0.shape[0]):
        for j in range(M0.shape[1]):
            if len(test_graph_P.neighbours(i)) <= len(test_graph_G.neighbours(j)):
                M0[i][j] = 1


    np_test_graph_G = test_graph_G.convert_to_numpy()
    np_test_graph_P = test_graph_P.convert_to_numpy()
   
    print(ullman_1(np_test_graph_G,np_test_graph_P))
    print(ullman_2(np_test_graph_G,np_test_graph_P,M0))
    print(ullman_3(np_test_graph_G,np_test_graph_P,M0))

if __name__ =="__main__":
    main()
