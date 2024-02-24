import queue
import time
import networkx as nx 
import matplotlib.pyplot as plt 

def order_BFS(graph, start_node):
    visited = set() # set for already visited nodes
    priority_queue = queue.Queue()# priority queue, FIFO
    priority_queue.put(start_node)# starting point node
    order = [] # empty list to store the correct order of BFS

    while not priority_queue.empty(): # loop to dertermin nodes to be processed
        vertex = priority_queue.get() # next node to be processed

        if vertex not in visited: # If node is not stored in the already visited list
            order.append(vertex) # Add node to the BFS list
            visited.add(vertex)# Add the present node to the visited node set!!
            
            for node in graph[vertex]:
                if node not in [visited]:
                    priority_queue.put(node)

    return order


def order_DFS(graph, start_node, visited):
    if visited is None:
        visited = set()

    ordered_dfs_list = []
    
    if start_node not in visited:
        ordered_dfs_list.append(start_node)
        visited.add(start_node)

        for node in graph[start_node]:
            if node not in visited:
                ordered_dfs_list.extend(order_DFS(graph, node,visited))

    return ordered_dfs_list

def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(title)
        nx.draw(G,pos, with_lables=True, node_color=['r' if n == node else 'g'for n in G.nodes])
        plt.draw()
        plt.pause(1.5)
    plt.show()
    time.sleep(1.5)



def random_graph(n,m):
    while True:
        G = nx.gnm_random_graph(n,m)
        if nx.is_connected(G):
            return G
        


order_BFS(G,pos)