from Graph import Graph, bfs
# Main program
if __name__ == "__main__":

    V = 5  # Total vertices
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    g.print_graph()
    print(bfs(g,0))
