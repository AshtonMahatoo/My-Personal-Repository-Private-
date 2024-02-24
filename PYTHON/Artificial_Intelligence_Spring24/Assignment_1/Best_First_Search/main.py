from queue import PriorityQueue
from Graph import Graph
from Vertex import Vertex




if __name__ == '__main__':

    graph = Graph()
    vertex = Vertex()

    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_vertex('c')
    graph.add_vertex('d')
    graph.add_vertex('e')
    graph.add_vertex('f')
    

    graph.add_edge('a', 'b', 7)  
    graph.add_edge('a', 'c', 9)
    graph.add_edge('a', 'f', 14)
    graph.add_edge('b', 'c', 10)
    graph.add_edge('b', 'd', 15)
    graph.add_edge('c', 'd', 11)
    graph.add_edge('c', 'f', 2)
    graph.add_edge('d', 'e', 6)
    graph.add_edge('e', 'f', 9)

    # for vertex in graph:
    #     for next_vertex in vertex.get_connections():
    #         vid = vertex.get_id()
    #         wid = next_vertex.get_id()
    #         print ( 'vertex :', vid,'is connected to vertex :', wid,', and weight is :', vertex.get_weight(next_vertex))  

    # for vertex in graph:
    #     print(vertex.get_id(), graph.vert_dict[vertex.get_id()])

print(graph.get_vertices())
print(graph.get_id())
graph = {
    'A': [('B', 4), ('C', 5)],
    'B': [('A', 4), ('C', 2), ('D', 1)],
    'C': [('A', 5), ('B', 2), ('D', 3)],
    'D': [('B', 1), ('C', 3)]
}

start_node = 'A'
goal_node = 'D'  

def best_First_Search(graph, start, goal):
    visited_list = set()
    queue = PriorityQueue()
    queue.put(0,start)

    while not queue.empty():
        current_position = queue.get()
        if current_position == goal:
            return True
        visited_list.add(current_position)
        neighbors = sorted(graph[current_position],key=lambda x:x[1])
        for neighbor, weight in neighbors:
            if neighbor not in visited_list:
                queue.put((weight, neighbor))

    return False





