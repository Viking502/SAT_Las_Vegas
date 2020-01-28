
class Vertice:

    def __init__(self, id):
        self.ident = id
        self.edge = []

    def add_edge(self, v):
        self.edge.append(v)


class Graph:

    def __init__(self, vertice):
        self.vertice = vertice

    def add_vertice(self):
        new_id = len(self.vertice)
        self.vertice.append(Vertice(new_id))

    def add_edge(self, u, v):
        self.vertice[u].add_edge(v)
        self.vertice[v].add_edge(u)


if __name__ == '__main__':

    gp = Graph()
