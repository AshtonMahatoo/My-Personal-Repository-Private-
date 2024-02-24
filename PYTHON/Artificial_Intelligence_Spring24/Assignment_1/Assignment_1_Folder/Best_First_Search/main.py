"""
Ashton Mahatoo
Artificial Intelligence Section W02

This is a demonstration of the Best First Search algorithm. 
The best first search uses a priority queue and is a heuristic search algorithm.
The aim is to reach the goal from the initial state via the shortest path.
"""

from queue import PriorityQueue # This imports the PriorityQueue


"""
best_First_Search algorithm has the following function arguments:

graph:The weighted graph in the form of an adjacency list.
starting_position: starting vertex point of search.
goal_position: goal vertex we want to reach.

"""

def best_First_Search(graph, starting_position, goal_position):
    set_visited = set() # set to keep track of visited nodes 
    queue_not_visited = PriorityQueue()  # priority queue to store unvisited list.

   
    #tuple that will containig the weight=0,starting_position, and an empty path stored in a list.
    queue_not_visited.put((0, starting_position, []))
    
    # We perform the main loop until the priority queue becomes empty, 
    # and store the vertex with the smallest weight from the priority queue.
    while not queue_not_visited.empty():
        weight, current_position, path = queue_not_visited.get()
        
        # Returns if we found goal position.
        if current_position == goal_position:
            return weight, path + [current_position]
        
        # If the current_position is not the goal_position
        # and not visited we store its position in the set_visited list
        # and explor its neighbor_positions.
        if current_position not in set_visited:
            set_visited.add(current_position)

            # For each neighbor_positions of the current_position, 
            # we calculate the total weight to reach that neighbor_positions,
            # and add it to the priority queue and update the path taken.
            for neighbor_positions, new_weight in graph[current_position]:
                if neighbor_positions not in set_visited:
                    queue_not_visited.put((weight + new_weight, neighbor_positions, path + [current_position]))
        
    
    return False  # Return False if goal_position can't be reached

# Example weighted graph represented as an adjacency list
graph = {
    'A': [('B', 7), ('C', 5)],
    'B': [('A', 7), ('D', 8), ('E', 4)],
    'C': [('A', 5), ('F', 2), ('G', 3)],
    'D': [('B', 8), ('H', 7)],
    'E': [('B', 4), ('H', 11)],
    'F': [('C', 2), ('I', 11)],
    'G': [('C', 3), ('I', 9)],
    'H': [('D', 7), ('E', 11)],
    'I': [('F', 11), ('G', 9)],
    'J': [ ('H', 3), ('I', 13)]
}

# for x in graph:
#     for y in graph[x]:
#         print(x,y)
starting_position = 'B'
goal_position = 'H'

weight, path = best_First_Search(graph, starting_position, goal_position)
if path:
    print("Total cost from Statring Position to reach Goal Position:", weight)
    print("Path from Starting Position to Goal Position :", path)
else:
    print("Goal can't be reached")


    

