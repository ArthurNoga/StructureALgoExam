
class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}
        self.num_vertices = 0

    def __str__(self):
        res: str = ""
        for k in self.get_vertices():
            res += str(k) + str(self.neighbors(k)) + "\n"
        return res

    def __iter__(self):
        return iter(self.vertices)

    def add_vertex(self, node):
        if node not in self.vertices:
            self.num_vertices = self.num_vertices + 1
            self.vertices.add(node)

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vertices:
            self.add_vertex(frm)
        if to not in self.vertices:
            self.add_vertex(to)

        self.add_neighbor(frm, to, cost)
        self.add_neighbor(to, frm, cost)

    def add_neighbor(self, frm, to, weight=0):
        if frm not in self.edges:
            self.edges[frm] = {}
        self.edges[frm][to] = weight

    def get_vertices(self):
        return self.vertices

    def neighbors(self, vertex):
        if vertex in self.edges:
            return self.edges[vertex]

    def get_weight(self, frm, to):
        if frm in self.edges and to in self.edges[frm]:
            return self.edges[frm][to]


if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('b', 'e', 7)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    # for v in g:
    #     for w in g.neighbors(v):
    #         print("%s , %s, %3d" % (v, w, g.get_weight(v, w)))
    for v in g:
        print("g.vertices[%s]=%s" % (v, g.neighbors(v)))
