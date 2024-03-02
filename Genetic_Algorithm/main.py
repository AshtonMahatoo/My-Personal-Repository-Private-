"""
Ashton Mahatoo

CS 3642: Artificial Intelligence 
Section W02 Spring Semester 2024
Fully Online D2L
Instructor Chen Zhao


Assignment 2
Implement Genetic Algorithm (GA) to find the minimal value of f(x) = x! , where 0 ≤ x ≤ 63 and x is an integer.
"""
import math
import random
from random import randrange, randint
import numpy as np
import re
import time


SIZE_OF_POPULATION = 100
PROBILITY_SCORE = 50 
BREAK_POINT = randint(1,100) #creates a random value between 1 and 100



####### GENERATE POPULATION FUNCTION
"""Below is the implementation of a function generate_population(SIZE_OF_POPULATION) that generates a random population size SIZE_OF_POPULATION. 
Each individual in the population should is represented as a binary vector of length 6, and representing integers in
the range of [0,63]. The desired output of generate_population(SIZE_OF_POPULATION) is [[0,0,0,0,0,1], [1,0,1,0,0,0]] """
start_time = time.time()
def generate_population(SIZE_OF_POPULATION): 
    mylist = []

    for i in range(SIZE_OF_POPULATION):
        # This generates the random value between [0,63]
        x = random.randint(1,63) 

        # This formats the random value in a binary vectorof length 6
        y = format(x,'06b') 

        # List that holds our values.
        mylist.append(y) 
    
    # Returns a binary lists of vectores
    return mylist
end_time = time.time()
""" GENERATE POPULATION FUNCTION VARIABLE LIST AND PRINT"""
# Sorted List variable for Generate Population
sorted_var_general_poputlation = sorted(generate_population(SIZE_OF_POPULATION))

# # This will format our binary vector in this "[[0,0,0,0,0,1], [1,0,1,0,0,0]]" form.
# print("Population Size")
# for index in range(len(sorted_var_general_poputlation)):
#     print("[{}],".format(sorted_var_general_poputlation[index]), end ="") 
# print("\n")

######
""" Below we iterate through the binary list using a for loop to isolate each parent binary string to get parents. """
for index in sorted_var_general_poputlation:
    parent_one = sorted_var_general_poputlation[0]
    parent_two = sorted_var_general_poputlation[1]
    parent_three = sorted_var_general_poputlation[2]
    parent_four = sorted_var_general_poputlation[3]
    
######
""" Below we store each length of the binary string in a list variable."""
parent_one = parent_one[0:6]
parent_two = parent_two[0:6]
parent_three = parent_three[0:6]
parent_four = parent_four[0:6] 

#### END




#### BEGIN FITNESS FUNCTION
""" Below is the fitness(v) function were v is a vector. 
It converts the vector from binary array into integer and calculates f(x) = x^2 """
def fitness(sorted_var_general_poputlation):
    
    # 2 Empty List is created
    decimal_list = []
    sqr_list = []
    best = []
    best2 = []
    
    for binary_num in sorted_var_general_poputlation:
        # decimal is converted from binary
        decimal_list.append(int(binary_num, 2))

        # f(x) = x^2 is calculated
        sqr_list.append(int(binary_num, 2) ** 2)
        
        # the two variables will print from low to high
        # sqr_list.sort()
        # decimal_list.sort()

    # Both lists are returned
    return decimal_list, sqr_list

""" VARIABLE LIST FITNESS FUNCTION """
# fitness_decimal, fitness_sqr = fitness(sorted_var_general_poputlation)
# print("From Fitness!! ", fitness_decimal, fitness_sqr)
### END FITNESS FUNCTION




###### BEGIN CROSSOVER FUNCTION
""" Below is our crossover(c1, c2)Function: Generate a random index to perform a single-point crossover. Combine the binary
    vectors at the chosen index. Return the two offspring created through crossover. Suppose two
    solutions are [0,0,0,1,0,1] and [0,0,1,1,1,1], the randomly generated index is 4. """
def crossover(first=[], second=[]):
    first_Parant = first[0:3]   
    first_Parant2 = first[3:6]
    second_Parant = second[0:3]
    second_Parant2 = second[3:6]
    first_child = first_Parant + second_Parant2
    Second_child = first_Parant2 + second_Parant
    return first_child , Second_child

# first_child, second_child = crossover(parent_one, parent_two)
# print("From Crossover: ", first_child, second_child)
### END CROSOVER





######  BEGIN MUTATE FUNCTION
""" Below is the mutation(c, p_m) function: For each bit in the binary vector, apply mutation with a PROBILITY_SCORE of p_m(Mutation).
    If mutation occurs, flip the bit. Return the mutated binary vector.This will perform mutation on an individual."""
def mutate(individual):

    #print("Individual", individual)
    #print(BREAK_POINT)
    mutated_individual = []
    n = len(individual)
    for i in range(0,n):
        mutated_individual.append(individual[i-1])
    return mutated_individual
######  END MUTATE FUNCTION



#####   BEGIN SELECTION FUNCTION
""" Below in the selection(population) that takes a list of binary vectors population as input. 
To implement Elite selection, we need to rank order the individuals based on their fitness, discard the bottom half, and
double the remaining. Then, return the selected parents for reproduction."""
def selection(population):
    
    # Created 2 lists
    decimal_list = []
    sqr_list = []
    
    # Our two created lists store the two variables from the fitness() function. 
    decimal_list, sqr_list = fitness(population)
    #print("Selection:", decimal_list, sqr_list)
    
    # the top half of our lists are stored in our created variables
    decimal_list = decimal_list[0:len(decimal_list)//2]
    sqr_list = sqr_list[0:len(sqr_list)//2]
    
    # Our created variables are being returned
    return decimal_list, sqr_list

""" VARIABLE LIST SELECTION FUNCTION """
my_variable = sorted(generate_population(SIZE_OF_POPULATION))
decimal_value, sqrt_value = selection(my_variable)
# print("My Variable" ,my_variable)
# print("from selection:" , decimal_value, sqrt_value)
    
#########   END SELECTION FUNCTION


    
#########   BEGIN EVOLUTION FUNCTION
""" Below is the evolution(population) that will performs the GA operations: selection, crossover, and mutation. """
def evolution(population):
    
    Perant1 = []
    Perant2 = []
    top_pop = []
    #Generate Population
    population_size = sorted(generate_population(population))
    top_pop = population_size[0:len(population_size)//2]
    
    
    # Selection Function
    decimal_list, sqr_list = sorted(fitness( population_size))
  
    # Crossover() function.
    first_child, second_child = crossover(parent_one, parent_two)
    print("Children: ", first_child, second_child)
    Perant1.append(decimal_list[:1] )
    Perant2.append(decimal_list[1:2])
    
    
    mutation = mutate(population_size)
    print("mutated child: ", mutation)    
    return population_size, top_pop
######  END EVOLUTION FUNCTION




##### BEGIN CHECK FUNCTION
""" Below is the check(population) function that will iterates through each individual in the population. It uses the fitness function to
evaluate the fitness of each individual. If an individual reaches the optimal fitness (in this case, the
minimum value of f(x) is 0 when x = 0), return True if at least one individual is found to be 0;
otherwise return False."""
def check(population):
    new_list = population.count(0)
    if new_list > 0:
        print("Yes it has")
    else:
        print("NO it does not")

# print("This is from Check Function: ")
# check(decimal_value)

pop,top_population = evolution(SIZE_OF_POPULATION)
print("Population: {}\nTop Population :{}".format (pop,top_population))


# Calculate the elapsed time
elapsed_time_ms = (end_time - start_time) * 1000
# Print the elapsed time
print("Elapsed time:", elapsed_time_ms, "seconds")









