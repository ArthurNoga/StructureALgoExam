""" A Python Class
A simple Python graph class, demonstrating the essential
facts and functionalities of graphs.
"""


class Graph(object):

    def __init__(self, graph_dict: dict = None):
        """
        initializes a graph object
        if no dictionary or None is given, an empty dictionary will be used
        :param graph_dict: a graph in the form
        {
            "a": ["d"],
            "b": ["c"],
            "c": ["b", "c", "d", "e"],
            "d": ["a", "c"],
            "e": ["c"],
            "f": []
        }
        """
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dict: dict = graph_dict

    def __str__(self):
        res: str = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def __generate_edges(self):
        """
        a static method generating the edges of the graph "graph"
        edges are represented as sets with one (a loop back to the vertex) or two vertices
        :return:
        """
        edges: list = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def vertices(self) -> list:
        """
        returns the vertices of a graph
        :return:
        """
        return list(self.__graph_dict.keys())

    def edges(self) -> list:
        """
        returns the edges of a graph
        :return:
        """
        return self.__generate_edges()

    def add_vertex(self, vertex: object):
        """
        if the vertex "vertex" is not in self.__graph_dict, a key "vertex" with an empty
        list as a value is added to the dictionary
        otherwise nothing has to be done.
        :param vertex: a vertex to add to the graph
        :return:
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """
        assumes that edge is of type set, tuple or list;
        between two vertices can be multiple edges!
        :param edge: a graph edge
        :return:
        """
        edge: set = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def order(self):
        return len(self.__graph_dict)

    def neighbors(self, vertex: object) -> list:
        """
        the adjacent vertices to a vertex
        :param vertex: origin vertex
        :return: list of vertices
        """
        if vertex in self.__graph_dict:
            return self.__graph_dict[vertex]

    def degree(self):
        """
        degree of the graph (maximal number of vertices)
        :return: the degree
        """
        max_degree: int = 0
        for v in self.__graph_dict.values():
            if len(v) > max_degree:
                max_degree = len(v)
        return max_degree

    def bfs(self, vertex: object) -> dict:
        """
        breath first search
        :param vertex: origin
        :return: the routing table (predecessors)
        """
        L: list = []
        marked: set = set()
        predecessor: dict = {}

        L.append(vertex)
        marked.add(vertex)
        predecessor[vertex] = None

        while len(L) > 0:
            v: object = L.pop(0)
            print(v)
            for u in self.neighbors(v):
                if u not in marked:
                    predecessor[u] = v
                    marked.add(u)
                    L.append(u)
        return predecessor

    def dfs(self, vertex: object) -> dict:
        """
        depth first search
        :param vertex: origin
        :return: the routing table (predecessors)
        """
        L: list = []
        predecessor: dict = {}
        marked: set = set()

        L.append(vertex)
        predecessor[vertex] = None

        while len(L) > 0:
            v: object = L.pop()
            if v not in marked:
                print(v)
                marked.add(v)
                for u in self.neighbors(v):
                    if u not in marked:
                        L.append(u)
                        predecessor[u] = v
        print(predecessor)

    def path_to(self, v: object, predecessor: dict):
        """
        print the path from the source node in predecessor (precedessor -> None)
        to a node v
        :param v: the destination
        :param predecessor: routing table (node -> predecessor)
        :return:
        """
        if v not in predecessor:
            print("no path from s to v")
        elif predecessor[v] is None:
            return print(v)
        else:
            print(v)
            self.path_to(predecessor[v], predecessor)

    def path_to_iter(self, v: object, predecessor):
        """
        print the path from the source node in predecessor (precedessor -> None)
        to a node v
        :param v: the destination
        :param predecessor: routing table (node -> predecessor)
        :return:
        """
        if v not in predecessor:
            print("no path from s to v")
        else:
            while v is not None:
                print(v)
                v = predecessor[v]


def intro(graph: Graph):
    print("Graph")
    print(graph)
    print()

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print()
    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of graph:")
    print(graph.vertices())

    print("Add an edge:")
    graph.add_edge({"a", "z"})

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print()
    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x", "y"})

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("order:", graph.order())
    print("degree:", graph.degree())
    print("neighbors:", graph.neighbors("c"))


def search(graph: Graph):
    print("### parcours en largeur ###")
    pred = graph.bfs("a")
    print()
    print("### chemin a -> e ###")
    graph.path_to("e", pred)
    print()
    print("### chemin a -> e iterative ###")
    graph.path_to_iter("e", pred)
    print()
    print("### parcours en profondeur ###")
    graph.dfs("d")


if __name__ == "__main__":
    # g = {"a": ["b", "c", "d"],
    #      "b": ["a", "d", "e"],
    #      "c": ["a", "d", "e"],
    #      "d": ["a", "b", "c"],
    #      "e": ["b", "c"]
    #      }
    g = {"a": ["b", "d"],
         "b": ["d", "e", "a"],
         "c": ["b", "e"],
         "d": ["a", "e", "f", "b"],
         "e": ["b", "d", "c", "g", "f"],
         "f": ["d", "e", "g"],
         "g": ["e", "f"]
         }

    graph = Graph(g)

    search(graph)