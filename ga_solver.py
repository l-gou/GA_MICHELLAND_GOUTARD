# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(generic genetic algorithm module)
"""
import random

class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GAProblem:
    """Defines a Genetic algorithm problem to be solved by ga_solver"""
    
    #definition of the different common functions and the arguments they need
    def create_chromosome(self):
        pass
    
    def create_fitness(self, chromosome):
        pass
    
    def reproduction(self, population, parent_a_index, parent_b_index): 
        pass
        
    def mutation(self, population, Index):
        pass


class GASolver:
    def __init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            problem (GAProblem): GAProblem to be solved by this ga_solver
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._problem = problem
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    
    def reset_population(self, pop_size=100):
        """ Initialize the population with pop_size random Individuals """
        for i in range(pop_size): #repeat the loop "pop_size" times
            chromosome = self._problem.create_chromosome() #call the function create_chromosome for the specific problem
            fitness = self._problem.create_fitness(chromosome) #call the function create_fitness for the specific problem
            new_individual = Individual(chromosome, fitness) #create a new individual with the chromosome and the fitness generated above
            self._population.append(new_individual) #add the "new_individual" to the population


    def evolve_for_one_generation(self):
        """ Apply the process for one generation : 
            -	Sort the population (Descending order)
            -	Selection: Remove x% of population (less adapted)
            -   Reproduction: Recreate the same quantity by crossing the 
                surviving ones 
            -	Mutation: For each new Individual, mutate with probability 
                mutation_rate i.e., mutate it if a random value is below   
                mutation_rate
        """
        #le code commun aux différents exos 
        #les fonctions prennent des arguments ici aussi
        
        #Selection :
        self._population.sort(reverse=True) #sort the population by the fitness in descending order 
        del self._population[int(len(self._population)*self._selection_rate):] #deletion of the worst half of the population
        
        
        #Reproduction :
        list_intermediaire = [] #creation of an empty list in order to add the children individuals
        for i in range(len(self._population)) : #this loop allows to create children individuals
            parent_a_index = random.randint(0,len(self._population)-1) #random int between 0 and the length of the population
            parent_b_index = random.randint(0,len(self._population)-1) #random int between 0 and the length of the population
            
            new_chrom = self._problem.reproduction(self._population, parent_a_index, parent_b_index) #the function reproduction() returns a chromosome
            new_individual = Individual(new_chrom, self._problem.create_fitness(new_chrom)) #creation of a new individual with the chromosome created above and the function create_fitness 
            
            list_intermediaire.append(new_individual) #add the individual to the the children individuals' list
            
        self._population += list_intermediaire #the children are added to the population

        #Mutation :
        for Index in range(len(self._population)) :
            number = random.random() #random number between 0.0 and 1.0
            if number < self._mutation_rate : #condition for the mutation to occur  
                new_chrom = self._problem.mutation(self._population,  Index) #call the function mutation() which is specific to each problem, it returns a chromosome
                new_individual = Individual(new_chrom, self._problem.create_fitness(new_chrom)) #creation of a new individual with the chromosome created above and the function create_fitness 
                self._population[Index] = new_individual #the mutated individual replaces the original individual 


    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        for individual in self._population:
            print(individual)

    def get_best_individual(self):
        """ Return the best Individual of the population """
        return max(self._population, key=lambda indiv: indiv.fitness)   

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None):
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        for i in range(max_nb_of_generations):
            self.evolve_for_one_generation()        
            if threshold_fitness and self.get_best_individual().fitness >= threshold_fitness:
                break


