
import numpy as np

def dynamic_programing(P,T):
    D = np.zeros((len(P),len(T)))
    parent = np.full((len(P),len(T)),'X')
    for i in range(len(P)):
        for j in range(len(T)):
            D[i][0] = i
            D[0][j] = j
    for i in range(len(P)):
        for j in range(len(T)):
            if P[i] != T[j]:
                change = D[i-1][j-1] + 1

            else:
                change = D[i-1][j-1]
                
            delete = D[i-1][j] + 1
            insert = D[i][j-1] + 1
            mins = [change,insert,delete]
            D[i][j]= np.min(mins)
            cost = np.argmin(mins)
            if P[i] == T[j]:
                parent[i][j] ='M'
            elif cost == 0:
                parent[i][j] = 'S'
            elif cost == 1:
                parent[i][j] ='I'
            elif cost == 2:
                parent[i][j] ='D'
    for i in range(1,len(P)):
        for j in range(1,len(T)):
            parent[0, j] = 'I'
            parent[i, 0] = 'D'
    return D[-1][-1]



def recuretion_wariant(P,T,i,j):
    if i == 0:
        return j 
    if j == 0:
        return i 
    if P[i] != T[j]:
        change = recuretion_wariant(P,T,i-1,j-1) + 1
    else:
        change =  0
    insert = recuretion_wariant(P,T,i,j-1) + 1
    delete = recuretion_wariant(P,T,i-1,j) + 1

    lower_bond = min(change,insert,delete)

    return lower_bond
    

def path_of_change(P,T):
    D = np.zeros((len(P),len(T)))
  
    parent = np.full((len(P),len(T)),'X')
 
    for i in range(len(P)):
        for j in range(len(T)):
            D[i][0] = i
            D[0][j] = j
    for i in range(len(P)):
        for j in range(len(T)):
            if P[i] != T[j]:
                change = D[i-1][j-1] + 1

            else:
                change = D[i-1][j-1]
                
            delete = D[i-1][j] + 1
            insert = D[i][j-1] + 1
            mins = [change,insert,delete]
            D[i][j]= np.min(mins)
            cost = np.argmin(mins)

            if P[i] == T[j]:
                parent[i][j] ='M'
            elif cost == 0:
                parent[i][j] = 'S'
            
            elif cost == 1:
                parent[i][j] ='I'
            elif cost == 2:
                parent[i][j] ='D'
    for k in range(1,len(P)):
        for j in range(1,len(T)):
            parent[0, j] = 'I'
            parent[k, 0] = 'D'
    x = len(P) - 1
    y = len(T) - 1
    path = []
    while x > 0:
        path.append(parent[x][y])

        if parent[x][y] == 'D':
            x -= 1 
        elif parent[x][y] == 'I':
            y -= 1
        elif parent[x][y] == 'M' or parent[x][y] == 'S':
            x -= 1
            y -= 1
    return path[::-1]

def matching(P,T):
    D = np.zeros((len(P),len(T)))
    parent = np.full((len(P),len(T)),'X')
    for i in range(len(P)):
        for j in range(len(T)):
            D[i][0] = i
    for i in range(len(P)):
        for j in range(len(T)):
            if P[i] != T[j]:
                change = D[i-1][j-1] + 1

            else:
                change = D[i-1][j-1]
                
            delete = D[i-1][j] + 1
            insert = D[i][j-1] + 1
            mins = [change,insert,delete]
            D[i][j]= np.min(mins)
            cost = np.argmin(mins)

            if P[i] == T[j]:
                parent[i][j] ='M'
            elif cost == 0:
                parent[i][j] = 'S'
            
            elif cost == 1:
                parent[i][j] ='I'
            elif cost == 2:
                parent[i][j] ='D'
    for i in range(1,len(P)):
        for j in range(1,len(T)):
            parent[0, j] = 'X'
            parent[i, 0] = 'D'
    x = len(P) - 1
    index = (np.argmin(D[-1,1:])+1) - (x) + 1
    return index


def longest_sequence(P,T):
    D = np.zeros((len(P),len(T)))
    parent = np.full((len(P),len(T)),'X')
    for i in range(len(P)):
        for j in range(len(T)):
            D[i][0] = i
            D[0][j] = j
    for i in range(1,len(P)):
        for j in range(1,len(T)):
            if P[i] != T[j]:
                change = D[i-1][j-1] + 500

            else:
                change = D[i-1][j-1]
                
            delete = D[i-1][j] + 1
            insert = D[i][j-1] + 1
            mins = [change,insert,delete]
            D[i][j]= np.min(mins)
            cost = np.argmin(mins)
            if P[i] == T[j]:
                parent[i][j] ='M'
            elif cost == 0:
                parent[i][j] = 'S'
            elif cost == 1:
                parent[i][j] ='I'
            elif cost == 2:
                parent[i][j] ='D'

    for i in range(1,len(P)):
        for j in range(1,len(T)):
            parent[0, j] = 'I'
            parent[i, 0] = 'D'
    x = len(P) - 1
    y = len(T) - 1
    path = []
    while x > 0:
        if parent[x][y] == 'D':
            x -= 1 
        elif parent[x][y] == 'I':
            y -= 1
        elif parent[x][y] == 'M' or parent[x][y] == 'S':
            path.append(P[x])
            x -= 1
            y -= 1
    return path[::-1]

def main():
    P = ' kot'
    T = ' kon'
    i = len(P)
    j = len(T)

    print(recuretion_wariant(P,T,i-1,j-1))
    P = ' kot'
    T = ' pies'
    i = len(P)
    j = len(T)
    print(recuretion_wariant(P,T,i-1,j-1))
    P = ' biały autobus'
    T = ' czarny autokar'
    print(dynamic_programing(P,T))
    P = ' thou shalt not'
    T = ' you should not'
    path = path_of_change(P,T)
    string = '"'
    for letter in path:
        string += letter
    string +='"'
    print(string)
    P = ' ban'
    T = ' mokeyssbanana'
    print(matching(P,T))
    P = ' democrat'
    T = ' republican'
    sequence = longest_sequence(P,T)
    string = "'"
    for letter in sequence:
        string += letter
    string += "'"
    print(string)
    T = ' 243517698'
    P = sorted(T)
    sequence = longest_sequence(P,T)
    string = "'"
    for letter in sequence:
        string += letter
    string += "'"
    print(string)
if __name__ =="__main__":
    main()

