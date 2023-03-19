
import polska

class Node:
    def __init__(self,vertex) -> None:
        self.x = vertex[0]
        self.y = vertex[1]
        self.key = vertex[2]

    def __eq__(self,other) -> bool:
        return self.key == other.key

    def __hash__(self) -> int:
        return hash(self.key)
        

class Edge:
    def __init__(self,vertex1,vertex2,wage) -> None:
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.wage = wage

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


    def insertEdge(self,vertex1,vertex2):
        if vertex1 not in self.list_vertex:
            self.insertVertex(vertex1)
        if vertex2 not in self.list_vertex:
            self.insertVertex(vertex2)    
        index1 = self.getVertexIdx(vertex1)
        index2 = self.getVertexIdx(vertex2)
        self.matrix[index1][index2] = 1
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

    def insertEdge(self,vertex1,vertex2):
        if vertex1 not in self.list_vertex:
            self.insertVertex(vertex1)
        if vertex2 not in self.list_vertex:
            self.insertVertex(vertex2)    
        index1 = self.getVertexIdx(vertex1)
        index2 = self.getVertexIdx(vertex2)
        self.list[index1].append(index2)
        self.graf_size += 1


    def deleteVertex(self,vertex):
        index = self.getVertexIdx(vertex)
        self.list_vertex.remove(vertex)
        self.dict_vertex.pop(vertex)
        for i in range(len(self.list_vertex)):
            self.dict_vertex[self.list_vertex[i]] = i 
        self.list.pop(index)
        for ed in self.list:
            if index in ed:
                ed.remove(index)

      

    def deleteEdge(self,vertex1,vertex2):
        index1 = self.getVertexIdx(vertex1)
        index2 = self.getVertexIdx(vertex2)
        self.list[index1].remove(index2)
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
        return self.list[vertexIdx]
    def edges(self):
        edges = []
        for i in range(len(self.list)):
            for j in self.list[i]:
                    edges.append((self.getVertex(i).key,self.getVertex(j).key))
        return edges

def main():
    # poland = Matrix_graf()  
    # for vertex1, vertex2 in polska.graf:
    #     v1 = Node(polska.slownik[vertex1])
    #     v2 = Node(polska.slownik[vertex2])
    #     poland.insertEdge(v1, v2)
    # poland.deleteEdge(Node(polska.slownik['W']), Node(polska.slownik['E']))
    # poland.deleteEdge(Node(polska.slownik['E']), Node(polska.slownik['W']))
    # poland.deleteVertex(Node(polska.slownik['K']))
    # polska.draw_map(poland.edges())
    
    poland2 = Graf_list()
    for vertex1, vertex2 in polska.graf:
        v1 = Node(polska.slownik[vertex1])
        v2 = Node(polska.slownik[vertex2])
        poland2.insertEdge(v1, v2)
    poland2.deleteEdge(Node(polska.slownik['W']), Node(polska.slownik['E']))
    poland2.deleteEdge(Node(polska.slownik['E']), Node(polska.slownik['W']))
    poland2.deleteVertex(Node(polska.slownik['K']))
    polska.draw_map(poland2.edges())
if __name__ =="__main__":
    main()
