
import time



def naive_shearch(S,W):
    m = 0
    i = 0
    apears = 0 
    mathces = 0
    counter = 0 
    while m != len(S):
        if W[i] != S[m]:
            m +=1
            mathces += 1
            counter = 0
            i = 0
        elif W[i] == S[m]:
            counter += 1
            i += 1
            m += 1
            mathces += 1
            if counter == len(W):
                i = 0
                apears += 1
                counter = 0
        
    return apears , mathces

def Rabin_Karp(S,W):
    apears = 0
    matches = 0
    hw = hash(W)
    
    for m in range(len(S)-len(W)):
        hS = hash(S[m:m+len(W)])
        matches += 1
        if hw==hS:
            if S[m:m+len(W)] == W:      
                apears += 1

        
    return apears, matches

def hash(word):
    d = 256
    q = 101
    hw = 0
    for i in range(len(word)):
        hw = (hw*d + ord(word[i]))%q
    return hw



def rollin_rabi(S,W):
    apears = 0
    matches = 0
    collision = 0
    h = 1 
    d = 256
    q = 101 
    for i in range(len(W)):
        h = (h*d) % q 
    hw = hash(W)
    hS = hash(S[:len(W)])
    for m in range(len(S)-len(W)):
        matches +=1
        if hS == hw:
            if S[m:m+len(W)] == W:    
                apears +=1
            else:
                collision +=1
        hS = ((d*hS - ord(S[m])*h) + (ord(S[m+len(W)]))) % q
        if hS < 0:
            hS += q

    return apears, matches,collision

def Knuth_Morris_Pratt(S,W):
    m = 0
    i = 0
    nP = 0
    P = []
    table = kmp_table(W)
    matches = 0
    while m < len(S):
        matches +=1
        if W[i] == S[m]:
            P.append(m-i)
            m += 1
            i += 1
            if i == len(W):
                P[nP] = m-i
                nP = nP + 1
                i = table[i]
        else:
            i = table[i]
            if i < 0:
                m += 1
                i += 1
    return nP , matches


def kmp_table(W):
    pos = 1
    cnd = 0
    T = [0 for i in range(len(W)+1)]
    T[0] = -1
    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1 
        cnd += 1
    T[pos] = cnd
    return T





def main():
    with open("lotr.txt",encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()
    W = 'time'
    appers , matches = naive_shearch(S,W)
    print("{0} ; {1}".format(appers,matches))
    t_start = time.perf_counter()
    naive_shearch(S,W)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    appers , matches = Rabin_Karp(S,W)
    print("{0} ; {1}".format(appers,matches))
    t_start = time.perf_counter()
    Rabin_Karp(S,W)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    appers,matches,colision = rollin_rabi(S,W)
    print("{0} ; {1} : {2} ".format(appers,matches,colision))
    t_start = time.perf_counter()
    rollin_rabi(S,W)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    appers,matches = Knuth_Morris_Pratt(S,W)
    print("{0} ; {1}".format(appers,matches))
    t_start = time.perf_counter()
    Knuth_Morris_Pratt(S,W)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
if __name__ =="__main__":
    main()
