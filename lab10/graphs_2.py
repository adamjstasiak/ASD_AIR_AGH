# <Adam Stasiak> <402722>
from typing import List, Set, Dict, Any, NamedTuple
from queue import Queue


# Pomocnicza definicja podpowiedzi typu reprezentującego etykietę
# wierzchołka (liczba 1..n).
VertexID = int

EdgeID = int

# Pomocnicza definicja podpowiedzi typu reprezentującego listę sąsiedztwa.
AdjList = Dict[VertexID, List[VertexID]]

# Nazwana krotka reprezentująca segment ścieżki.


class TrailSegmentEntry(NamedTuple):
    Start: VertexID
    Stop: VertexID
    Edge: EdgeID
    weight: float


Trail = List[TrailSegmentEntry]

Distance = int


class neighbours(NamedTuple):
    id: int
    distance: int


def neighbors(adjlist: AdjList, star_vertex_id: VertexID, max_distance: Distance) -> Set[VertexID]:
    if star_vertex_id in adjlist.keys():
        visited = set()
        Q = Queue()
        Q.put((star_vertex_id, 0))
        while not Q.empty():
            u = Q.get()
            if u[0] not in adjlist.keys():
                return visited
            for v in adjlist[u[0]]:
                if (v not in visited) and (v != star_vertex_id):
                    if u[1] + 1 <= max_distance:
                        visited.add(v)
                        Q.put((v, u[1]+1))
                    else:
                        return visited
        return visited
    else:
        return set()


def load_multigraph_from_file(filepath: str) -> nx.MultiDiGraph:
    """Stwórz multigraf na podstawie danych o krawędziach wczytanych z pliku.

    :param filepath: względna ścieżka do pliku (wraz z rozszerzeniem)
    :return: multigraf
    """
    G = nx.MultiDiGraph()
    with open(filepath, 'r') as str_graph:
        for l in str_graph:
            l = l.strip()
            if l:
                l = l.replace("\n", "")
                l_array = l.split(' ')
                if l != '':
                    G.add_edge(int(l_array[0]), int(
                        l_array[1]), weight=float(l_array[2]))
    return G


def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:
    """Znajdź najkrótszą ścieżkę w grafie pomiędzy zadanymi wierzchołkami.

    :param g: graf
    :param v_start: wierzchołek początkowy
    :param v_end: wierzchołek końcowy
    :return: najkrótsza ścieżka
    """
    list = nx.dijkstra_path(g, v_start, v_end)

    trail: Trail = []
    for i in range(len(list)-1):
        v_list = []
        atlas_view = g[list[i]][list[i+1]]
        for v in atlas_view:
            v_list.append(atlas_view[v]['weight'])
        v_weight = min(v_list)
        v_index = v_list.index(v_weight)
        trail.append(TrailSegmentEntry(list[i], list[i+1], v_index, v_weight))
    return trail


def trail_to_str(trail: Trail) -> str:
    """Wyznacz reprezentację tekstową ścieżki.

    :param trail: ścieżka
    :return: reprezentacja tekstowa ścieżki
    """
    str_trail = ""
    the_last_one = ""
    value = 0
    for seg in trail:
        str_trail += str(seg[0]) + " -[" + str(seg[2]) + \
            ": " + str(seg[3]) + "]-> "
        the_last_one = str(seg[1])
        value += seg[3]
    str_trail += the_last_one + " (value = " + str(value) + ")"
    return str_trail
