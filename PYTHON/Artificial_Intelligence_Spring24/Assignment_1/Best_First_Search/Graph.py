
from Vertex import Vertex


class Graph:
    def __init__(self):
        self.graph_dictionary = {} # Graph object to store graph elements
        self.vertices_total = 0 # total count of vertices

    def __iter__(self):
        return iter(self.graph_dictionary.values())

    def add_vertex(self, node):
        self.vertices_total = self.vertices_total + 1
        new_vertex = Vertex(node)
        self.graph_dictionary[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.graph_dictionary:
            return self.graph_dictionary[n]
        else:
            return None

    def add_edge(self, vertex_begin, vertex_to, weight = 0):
        if vertex_begin not in self.graph_dictionary:
            self.add_vertex(vertex_begin)
        if vertex_to not in self.graph_dictionary:
            self.add_vertex(vertex_to)

        self.graph_dictionary[vertex_begin].add_neighbor(self.graph_dictionary[vertex_to], weight)
        self.graph_dictionary[vertex_to].add_neighbor(self.graph_dictionary[vertex_begin], weight)

    def get_vertices(self):
        return self.graph_dictionary.keys()