from Node import*


class Graph:

    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes

    # This will add a new node/vertex to the Graph
    def add_nodes(self,value,neighbors=None):
        self.nodes.append(Node(value,neighbors))


    # Checks for duplecate node values
    def check_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None
    
    def add_edge(self, value1, value2, weight=1):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)
    




























































































































