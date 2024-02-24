"""
2/11/24
This is a demonstration of the Uniform Cost Algorithm using Python. 

"""
# This imports the Heap Queue Algorithm
import heapq 


"""
Uniform Cost Algorithm algorithm has the following function arguments:

graph:The weighted graph in the form of an adjacency list.
starting_position: starting vertex point of search.
goal_position: goal vertex we want to reach.

"""

def uniform_Cost_Search(graph, starting_position, goal_position):
    visited_set = set() # set to keep track of visited nodes 

    #tuple that will containig the weight=0,starting_position, and an empty path stored in a list.
    heapq_not_visited = [(0, starting_position, [])]
    
    # We perform the main loop until the priority queue becomes empty, 
    # and store the vertex with the smallest weight from the priority queue.
    while heapq_not_visited:
        weight, current_position, path = heapq.heappop(heapq_not_visited)
        
        # This If Returns if we found goal position.
        if current_position not in visited_set:
            visited_set.add(current_position)
            path = path + [current_position]
            if current_position == goal_position:
                return weight, path

            # For each neighbor_positions of the current_position, 
            # we calculate the total weight to reach that neighbor_positions,
            # and add it to the priority queue and update the path taken.
            for neighbor_positions, present_weight in graph[current_position]:
                if neighbor_positions not in visited_set:
                    heapq.heappush(heapq_not_visited, (weight + present_weight, neighbor_positions, path))
        
    
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
    'J': [('A', 9), ('H', 3), ('I', 13)]
}

# for x in graph:
#     for y in graph[x]:
#         print(x,y)
starting_position = 'C'
goal_position = 'I'

weight, path = uniform_Cost_Search(graph, starting_position, goal_position)
if path:
    print("Total cost from Statring Position to reach Goal Position:", weight)
    print("Path from Starting Position to Goal Position :", path)
else:
    print("Goal can't be reached")