# <Adam Stasiak> <402722>
from typing import List, Dict


def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    v = len(adjmat)
    e = len(adjmat[0])
    dic = {}
    for i in range(v):
        key: List[int] = []
        for j in range(e):
            if adjmat[i][j] != 0:
                val = adjmat[i][j]
                for k in range(val):
                    key.append(j + 1)
                    dic[i + 1] = key
    return dic


def dfs_recursive(G: Dict[int, List[int]], s: int) -> List[int]:
    def recursive(G: Dict[int, List[int]], s: int, visited: List):
        visited.append(s)

        for key in G[s]:
            if key not in visited:
                recursive(G, key, visited)
    visited = []
    recursive(G, s, visited)
    return visited


def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    visited = []
    stack = [s]
    while len(stack) > 0:
        near = stack.pop()
        if near not in visited:
            visited.append(near)
            for v in reversed(G[near]):
                stack.append(v)
    return visited


def is_acyclic(G: Dict[int, List[int]]) -> bool:
    def acyclic(G1: List[int], s: int, visited):
        visited.append(s)
        for near in G1:
            if near in visited:
                return True
            else:
                acyclic(G1, near, visited[:])
    visited = []
    for el in G:
        if acyclic(G[el], el, visited):
            return False
    return True
