"""
Pour la classe Graph du module graph
    a. Implémenter un fonction dfs qui parcourt le graphe en profondeur à partir d'une origine v
        La méthode doit retourner le tableau de routage et de distance dans une tuple

    b. Implémenter la méthode path_to qui donne le chemin entre un
        sommet u et le sommet d'origine v du parcours en largeur
"""
from queue import Queue

from graph import Graph, create_simple_graph

def dfs(graph: Graph, _from: object) -> tuple:
    marked: list = []
    distance: dict = {_from: 0}
    routage: dict = {_from: None}
    return _dfs(graph, _from, marked, distance, routage)



def _dfs(graph: Graph, _from: object, marked: list, distance: list, routage: list) -> tuple:
    marked.append(_from)
    for v in graph.neighbors(_from):
        if v not in marked:
            routage[v] = _from
            distance[v] = distance[_from] + graph.get_weight(_from, v)
            _dfs(graph, v, marked, distance, routage)
    return  routage, distance,marked

def path_to(routage: dict, _from: object, _to: object) -> list:
    path: list = []
    if _from in routage and _to in routage and routage[_from] is None:
        cur: object = _to
        while cur is not None:
            path.insert(0,cur)
            cur = routage[cur]
    else:
        return "leChemin n'existe pas"
    return path



if __name__ == "__main__":
	graph: Graph = Graph()

	create_simple_graph(graph)
	print(graph)
	print(graph)
	routage, distance,marked = dfs(graph, 0)
	print(distance)
	print(routage)
	print(path_to(routage, 0,3))
