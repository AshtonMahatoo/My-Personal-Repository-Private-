"""
Ashton Mahatoo

CS 3642: Artificial Intelligence 
Section W02 Spring Semester 2024
Fully Online D2L
Instructor Chen Zhao


Assignment 2
Implement Genetic Algorithm (GA) to find the minimal value of f(x) = x! , where 0 ≤ x ≤ 63 and x is an integer.
"""

import random
from random import randrange
import math




"""
Below is the implementation of a function generate_population(sizeof_population) that generates a random population size sizeof_population. 
Each individual in the population should is represented as a binary vector of length 6, and representing integers in
the range of [0,63]. The desired output of generate_population(sizeof_population) is [[0,0,0,0,0,1], [1,0,1,0,0,0]]
"""
def generate_population(sizeof_population): 
    mylist = []

    for i in range(sizeof_population):
        # This generates the random value between [0,63]
        x = random.randint(1,63) 

        # This formats the random value in a binary vectorof length 6
        y = format(x,'06b') 

        # List that holds our values.
        mylist.append(y) 

    # Returns a binary lists of vectores
    return mylist



"""
Below is the fitness(v) function were v is a vector. 
It converts the vector from binary array into integer and calculates f(x) = x^2
"""
def fitness(binary_list):
    
    # 2 Empty List is created
    decimal_list = []
    sqr_list = []

    for binary_num in binary_list:
        # decimal is converted from binary
        decimal_list.append(int(binary_num, 2))

        # f(x) = x^2 is calculated
        sqr_list.append(int(binary_num, 2) * 2)

    # Both lists are returned
    return decimal_list , sqr_list



def crossover(c1,c2): None

def mutation(c,p_m): None

def selection(population): None

def evolution(population): None
def crossover(population): None


# Variable that stores population size
sizeof_population = 10


#Variable that stores binary string of population produced by the function
calculate_population = generate_population(sizeof_population)


# This will format our binary vector in this "[[0,0,0,0,0,1], [1,0,1,0,0,0]]" form.
for index in range(len(calculate_population)):
    print("[{}],".format(calculate_population[index]), end ="") 
print("\n")










