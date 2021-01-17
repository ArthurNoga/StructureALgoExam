import math
import random
from pprint import pprint
from time import time

from graph import Graph, create_simple_graph, create_random_graph
from pqueue import PriorityQueue


def dijkstra(graph: Graph, source: object) -> tuple:
    """
    calcule les plus courts chemins entre les sommets d'un graphe à partir d'une origine source
    :param graph: le graphe
    :param source: le sommet d'origine
    :return: une tuple avec les distance stockés dans la variable dist
                et le tableau de routage
    """
    dist: dict = {source: 0}  # initialization
    routage: dict = {}  # routing table
    Q: PriorityQueue = PriorityQueue()  # create vertex priority queue Q
    for v in graph.get_vertices():
        if v != source:
            dist[v] = math.inf  # unknown distance from source to v
        routage[v] = None  # predecessor of v
        Q.add(v, priority=dist[v])

    while not Q.is_empty():  # the main loop
        vertex: tuple = Q.pop()  # remove and return best vertex
        u: object = vertex[1]
        for v in graph.neighbors(u):  # only v that are still in Q
            alt = dist[u] + graph.get_weight(u, v)
            if alt < dist[v]:
                dist[v] = alt
                routage[v] = u
                Q.add(v, priority=alt)
    return dist, routage


def roy_warshall(graph: Graph):
    """
    calcule le plus courts chemins entre les sommets du graphe graph
    :param graph: un graphe
    :return: la matrice de distance et de routage
    """
    dist: list = []  # initialization
    routage: list = []  # routing table

    for i in range(graph.num_vertices):
        dist.append([None] * graph.num_vertices)
        routage.append([None] * graph.num_vertices)
        for j in range(graph.num_vertices):
            if i == j:
                dist[i][j] = 0
            elif j in graph.neighbors(i):
                dist[i][j] = graph.get_weight(i, j)
                routage[i][j] = i
            else:
                dist[i][j] = math.inf

    for k in range(graph.num_vertices):
        for i in range(graph.num_vertices):
            for j in range(graph.num_vertices):
                alt_dist = dist[i][k] + dist[k][j]
                if alt_dist < dist[i][j]:
                    dist[i][j] = alt_dist
                    routage[i][j] = k

    return dist, routage


def path_to(routing: dict, source: int, destination: int) -> list:
    """
    calcule le chemin source -> destination
    :param routing: la table de routage
    :param source: sommet source
    :param destination: sommet destination
    :return: le chemin
    """
    if source not in routing or destination not in routing:
        return None
    else:
        path: list = []
        cur: int = destination
        while cur is not None:
            path.insert(0, cur)
            cur = routing[cur]
        return path


def test_dijkstra(graph: Graph):
    print("Dijkstra")
    start: float = time()
    repeat: int = min(30, graph.num_vertices)
    for i in range(repeat):
        dist, rout = dijkstra(graph, i)
        pprint(dist)
        pprint(rout)

        dest: int = random.randint(0, graph.num_vertices - 1)
        path: list = path_to(rout, i, dest)
        print("path", i, "to", dest, ":", path)
        print()
    print(time() - start)


def test_roy_warshall(graph: Graph):
    print("Roy-Warshall")
    start: float = time()
    dist, rout = roy_warshall(graph)
    pprint(dist)
    pprint(rout)
    print(time() - start)


if __name__ == "__main__":
    graph: Graph = Graph()
    complex_graph: bool = False

    if complex_graph:
        number_vertex: int = 1000
        number_edge: int = int((number_vertex * (number_vertex - 1) / 2) / 4)
        create_random_graph(graph, number_vertex, number_edge)
    else:
        create_simple_graph(graph)

    test_dijkstra(graph)
    print()
    test_roy_warshall(graph)
