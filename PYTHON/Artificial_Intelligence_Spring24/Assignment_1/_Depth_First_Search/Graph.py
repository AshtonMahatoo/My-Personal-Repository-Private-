"""
This is a test file for the UCS search
"""

class Graph:
    """
    # This creates the dictionary object 
    """
    def __init__(self,graph_dictionary=None):
        if graph_dictionary is None:
            graph_dictionary = []
        self.graph_dictionary = graph_dictionary
    
    """
    This method gets the vertices of the graph
    """
    def get_Graph_Vertices(self):
        return list(self.graph_dictionary.keys())
    
    """
    This method will display graph edges
    """
    def get_Graph_Edges(self):
        graph_edges = []
        for vertex in self.graph_dictionary:
            for next_vertex in self.graph_dictionary[vertex]:
                if {next_vertex, vertex} not in graph_edges:
                    graph_edges.append({vertex,next_vertex})
        
        return graph_edges
    

    """
    This method will add a vertex to the graph
    """
    def add_Graph_Vertex(self,vertex):
        if vertex not in self.graph_dictionary:
            self.graph_dictionary[vertex] = []

    """
    This method will add anew edge connection
    """
    def add_New_Edge(self, edge_connection):
        edge_connection = set(edge_connection)
        (vertex_connect_1, vertex_connect_2) = tuple(edge_connection)
        if vertex_connect_1 in self.graph_dictionary:
            self.graph_dictionary[vertex_connect_1].append(vertex_connect_2)
        else:
            self.graph_dictionary[vertex_connect_1] = [vertex_connect_2]

    """
    This method will list the edge names
    """
    def display_Edges(self):
        edges_names = []
        for vertex in self.graph_dictionary:
            for next_vertex in self.graph_dictionary[vertex]:
                if [next_vertex, vertex] not in edges_names:
                    edges_names.append({vertex, next_vertex})
        return edges_names


if __name__ == '__main__':       
    graph = {
        "A" :   ["B","C","D"],
        "B" :   ["E","F","G"],
        "C" :   ["H","I","J"],
        "D" :   ["K","L"],
        "E" :   [],
        "F" :   ["M"],
        "G" :   ["N"],
        "H" :   [],
        "I" :   [],
        "J" :   ["O"],
        "K" :   ["P"],
        "L" :   [],
        "M" :   [],
        "N" :   [],
        "O" :   [],
        "P" :   []
    }
    graph_object= Graph(graph)

    """
    set() object to keep track of visited nodes
    """   
    visited_vertex = set()
    """
    This method uses recursion to demonstrate the DFS algorithm
    """
    def depth_First_Search(visited_vertex, graph, vertex):
        if vertex not in visited_vertex:
            print(vertex)
            visited_vertex.add(vertex)
            for neighbour_vertex in graph[vertex]:
                depth_First_Search(visited_vertex, graph, neighbour_vertex)







    # print(graph)
    # print(graph_object.get_Graph_Vertices())
    # print(graph_object.get_Graph_Edges())
    # graph_object.add_Graph_Vertex("Q")
    # print(graph_object.get_Graph_Vertices())

    # graph_object.add_New_Edge({"P","O"})
    # graph_object.add_New_Edge({"M","N"})
    # print(graph_object.display_Edges())

    depth_First_Search(visited_vertex,graph, "A")


