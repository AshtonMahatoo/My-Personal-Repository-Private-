
"""
This is just a test file!!!


"""
import random

# def generate_population(sizeof_population): 
#     mylist = []

#     for i in range(sizeof_population):
#         x = random.randint(1,63) # This generates the random value between [0,63]
#         y = format(x,'06b') # This formats the random value in a binary vector of length 6
#         mylist.append(y) # List that holds our values.
#     return mylist

# def fitness(binary_list):
    
#     decimal_list = []
#     sqr_list = []
#     for binary_num in binary_list:
#         decimal_list.append(int(binary_num, 2))
#         sqr_list.append(int(binary_num, 2) * 2)
#     #print(decimal_list)

#     return decimal_list , sqr_list


# pop_size = 4

# binary_list = generate_population(pop_size)
# decimal_list , sqr_list =  fitness(binary_list)
# sqr_list.sort(reverse=True)
# decimal_list.sort(reverse=True)


# for index in binary_list:
#     parent_one = binary_list[0]
#     parent_two = binary_list[1]
#     parent_three = binary_list[2]
#     parent_four = binary_list[3]
   
# parent_one = parent_one[0:6]
# parent_two = parent_two[0:6]
# parent_three = parent_three[0:6]
# parent_four = parent_four[0:6] 

# def crossover(first=[], second=[]):
#     first1 = first[0:3]   
#     first2 = first[3:6]
#     second1 = second[0:3]
#     second2 = second[3:6]
#     first1_second2_cross = first1 + second2
#     first2_second1_cross = first2 + second1
#     return first1_second2_cross , first2_second1_cross




     
    

       

# # Example usage:
# individual = []  # Example individual
#mutation_rate = 0.5  # Mutation rate
#print("Original individual:", parent_four)
# mutated_individual = mutate(parent_four, mutation_rate)
# print("Mutated individual:", mutated_individual)
 



# print("Original individual:", individual)
# mutated_individual = mutate(individual, mutation_rate)
# print("Mutated individual:", mutated_individual)


# first, second = crossover(parent_one, parent_two)
# print("Before crossover: {} , {} ".format(parent_one,parent_two))
# print("After crossover: {}, {} ".format(first, second))
# print("Binary representation of parent_one:{}, parent_two:{}, parent_three:{}, parent_four:{}".format(parent_one,parent_two,parent_three,parent_four))
# print("parent_one:{}, parent_two:{}, parent_three:{}, parent_four:{}".format(parent_one, parent_two,parent_three,parent_four))
# print("Decimal list 1 : {} , and Decimal Sqr : {}".format(decimal_list,sqr_list))


def check(population):
    checkc_point = []
    n = len(population)
    for i in range(0,n):
        checkc_point.append(population[i-1])
    return checkc_point