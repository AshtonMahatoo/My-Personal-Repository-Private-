"""
Ashton Mahatoo
Artificial Intelligence Section W02
2/24

This is a implementation of the Depth-First Search algorithm.
DFS will search all the vertices of a graph or tree data structure. 
The purpose of the algorithm is to mark each vertex it visited 
while avoiding cycles.
"""

# Gaph with connections
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

"""
set() object to keep track of visited nodes
"""   
visited_vertex = {}
"""
This method uses recursion to demonstrate the DFS algorithm
"""
def depth_First_Search(visited_vertex, graph, vertex):
    if vertex not in visited_vertex:
        print("Position:" ,vertex)
        visited_vertex[vertex] = visited_vertex
        for neighbour_vertex in graph[vertex]:
            depth_First_Search(visited_vertex, graph, neighbour_vertex)



depth_First_Search(visited_vertex,graph, "B")
