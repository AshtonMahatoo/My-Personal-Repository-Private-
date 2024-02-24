

class Node:
    
    def __init__(self, value, neighbors=None): # value = stored data, neighbors = connected vertices
        self.value = value
        if neighbors is None: # This is 
            self.neighbors =[]
        else:
            self.neighbors = neighbors

    
    # Checks if the vertex is connected.
    def have_neighbors(self):
        if len(self.neighbors) == 0:
            return False
        else:
            return True
        
    # Returns the number of connected vertices
    def number_of_neighbors(self):
        return len(self.neighbors)
    
    # Adds new neighbors
    def add_new_neighbors(self,neighbors):
        self.neighbors.append(neighbors)

    def __str__(self):
        return_string = f"{self.value}->"
        if self.have_neighbors():
            for neighbors in self.neighbors:
                return_string += f"{neighbors[0].value} ->"
    
        return_string += "None"
        return return_string

