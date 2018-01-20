# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 12:24:29 2017

@author: Emanuele

Rank selection problem: given a list of n elements, ordered by a parameter (a floating point) in ascending/descending order
 we want to pick up the first element of the list with probability 1/2 (i.e. 2^(-rank)), the second one with probability 1/4,
 the third one with probability 1/8 and so on..

Solution: we pick up the last element of the list, i.e. the one with the lowest probability to be picked up, and we copy it in
 a new list: then we pick the penultimate element, which we know has double the probability of being picked up than the last one,
 and we copy it two times in the new list. We iterate the process for every element doubling every time the number of copies we do.
 Using the list obtained in this way, we randomly pick up an element.
 
Time Complexity: O(2^n), where n is the size of the initial list of elements, this is the time we need to build the new list of elements;
Space Complexity: O(2^n), since we use a list which contains 1 element for the last in the original list, 2 for the penultimate,..,
                  2^(n-1) for the first one. Doing so we have 2^0 + 2^1 + 2^2 + .. + 2^(n-1) ~ 2*(2^(n-1)) = 2^n
"""

import numpy as np

# this function takes as input:
#   population, the population ordered by the fitness of each element
# returns:
#   the new population, whose size should be 2^(2n)
#   a random element of population, picked up with probability 2**(-rank) where rank is the position of the element wrt the fitness in the popoulation (rank goes from 1 to len(population))
def overgrown_rank_selection(population):
    new_population = list();
    for n in range(len(population)):
        for i in range(2**n):
            new_population.append(population[-n]);    
    return new_population, new_population[np.random.randint(0, len(new_population))];

""" Test Part """
population_size = 10;
population = list([[i, -.1*i] for i in range(population_size)]); # create a population by descending fitness (-.1*i)
new_pop, picked_el = overgrown_rank_selection(population);
