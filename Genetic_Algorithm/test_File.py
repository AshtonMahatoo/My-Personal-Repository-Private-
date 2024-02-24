
"""
This is just a test file!!!


"""
import random

def generate_population(sizeof_population): 
    mylist = []

    for i in range(sizeof_population):
        x = random.randint(1,63) # This generates the random value between [0,63]
        y = format(x,'06b') # This formats the random value in a binary vector of length 6
        mylist.append(y) # List that holds our values.
    return mylist

def fitness(binary_list):
    
    decimal_list = []
    sqr_list = []
    for binary_num in binary_list:
        decimal_list.append(int(binary_num, 2))
        sqr_list.append(int(binary_num, 2) * 2)
    #print(decimal_list)

    return decimal_list , sqr_list


pop_size = 10



binary_list = generate_population(pop_size)

list1 , list2 =  fitness(binary_list)

print("Decimal list 1 : {} , and Decimal Sqr : {}".format(list1,list2))

