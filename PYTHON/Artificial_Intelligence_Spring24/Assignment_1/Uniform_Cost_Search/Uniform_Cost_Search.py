
class Node:
    def __init__(self,value,neighbors=None):
        self.value = value
        self.heuristic_value = int
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors
        self.parent = None

    def __gt__(self, other):
        if isinstance(other,Node):
            if self.heuristic_value > other.heuristic_value:
                return True
            if self.heuristic_value < other.heuristic_value:
                return False
            return self.value > other.value
        



class Graph:
    def __init__(self,nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes

    def add_node(self,value,neighbors=None):
        self.nodes.append(Node(value, neighbors))
    
    def find_node(self,value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None
    
    def add_edge(self,value1,value2, weight =1):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)


class UCS:

    def __init__(self,graph,start_position, target):
        self.graph = graph
        self.start = graph.find_node(start_position)
        self.target = graph.find_node(target)
        self.opened = []
        self.closed = []
        self.number_of_steps = 0

    def calculate_distance(self,parent,child):
        for neighbor in parent.neighbors:
            if neighbor[0] == child:
                distance = parent.heuristic_value + neighbor[1]
                if distance < child.heuristic_value:
                    child.parent = parent
                    return distance
                return child.heuristic_value
    

    def search(self):
        self.start.heuristic_value = 0
        self.opened.append(self.start)

        while True:
            self.number_of_steps += 1

            if self.opened_is_empty():
                print(f"No Solution Found after{self.number_of_steps}steps!!!")
                break
            selected_node = self.remove_from_opened()

            if selected_node == self.target:
                path = self.calculate_path(selected_node)
                return path, self.number_of_steps
            
            new_nodes = selected_node.extend_node()

            if len(new_nodes) > 0:
                for new_nodes in new_nodes:
                    new_nodes.heuristic_value = self.calculate_distance(selected_node, new_nodes)
                    if new_nodes not in self.closed and new_nodes not in self.opened:
                        self.insert_to_list("open", new_nodes)
                    elif new_nodes in self.opened and new_nodes.parent != selected_node:
                        old_node = self.get_old_node(new_nodes.value)
                        if new_nodes.heuristic_value < old_node.heuristic_value:
                            new_nodes.parent = selected_node
                            self.insert_to_opened(new_nodes)

  
graph = Graph()
graph.add_node(Node('v1'))
graph.add_node(Node('v2'))
graph.add_node(Node('v3'))
graph.add_node(Node('v4'))
graph.add_node(Node('v5'))
graph.add_node(Node('v6'))        

graph.add_edge('v1','v2',9)
graph.add_edge('v1','v3',4)
graph.add_edge('v2','v3',2)
graph.add_edge('v2','v4',7)
graph.add_edge('v2','v5',3)
graph.add_edge('v3','v4',1)
graph.add_edge('v3','v5',6)
graph.add_edge('v4','v5',4)
graph.add_edge('v4','v6',8)
graph.add_edge('v5','v6',2)        


alg = UCS(graph, "v1","v6")
path, path_length = alg.search()
print("-> ".join(path))
print(f"Length of the path: {path_length}")


        


