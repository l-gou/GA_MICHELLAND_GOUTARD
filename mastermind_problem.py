# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving Mastermind example)
"""
from ga_solver import GAProblem, Individual
import mastermind as mm
import random

class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""
    #code spécifique pour le problem
    
    def create_chromosome(self):
        """
        Creation of a chromosome, composed of 4 random colors
        takes no argument
        returns a chromosome
        """
        chromosome = mm.generate_random_secret(size=4)  #combinations of 4 random colors are generated
        return chromosome #return chromosome
    
    def create_fitness(self, chromosome):
        """
        Creation of a fitness, using the function 'rate_guess' imported from mastermind.py
        takes a chromosome as an argument
        returns a fitness 
        """
        fitness = match.rate_guess(chromosome) #calculation of the fitness of the chromosome generated above
        return fitness #return a fitness value
    
    def reproduction(self, population, parent_a_index, parent_b_index):
        """
        Reproduction step :
        takes a population and two integers as arguments
        returns a chromosome
        
        Steps are : 
            - Take a crossing point at random
            - Take parent 1’s chromosome up to this crossing point
            - Take parent 2’s chromosome after the crossing point till its end
            - Concatenate both parts to produce the new chromosome
        """
        x_point = random.randrange(0,4) #random int between 0 and 3 (included)
        new_chrom = population[parent_a_index].chromosome[0:x_point] + population[parent_b_index].chromosome[x_point:] #the new chromosome is composed of the beginning of the parent A's chromosome and the end of the parent B's chromosome
        return new_chrom #return a chromosome
        
    def mutation(self, population, Index):
        """
        Mutation step :
        takes a population and an integer as arguments
        returns a chromosome
        
        Steps are :
             - Pick a random chromosome position
             - Replace that gene with another gene taken at random in the list of all valid genes
        """
        pos = random.randrange(0,4) #random position on which the position will occur
        valid_colors = mm.get_possible_colors() #list of all possible colors
        new_gene = random.choice(valid_colors) #one random color is selected
        new_chrom = population[Index].chromosome[0:pos] + [new_gene] + population[Index].chromosome[pos+1:] #the selected color is added in the gene of the selected position
        return new_chrom #return a chromosome
    
        


if __name__ == '__main__':

    from ga_solver import GASolver

    match = mm.MastermindMatch(secret_size=4) #creation of a MastermindMatch() object
    problem = MastermindProblem() #creation of a MastermindProblem() object
    solver = GASolver(problem) #create a GASolver() object for the problem created above

    solver.reset_population() #call the function "reset_population()"
    solver.evolve_until() #call the function "evolve_until()"

    best = solver.get_best_individual() #call the function "get_best_individual()"
    print(f"Best guess {best.chromosome}") #print the best individual's chromosome
    print(f"Problem solved ? {match.is_correct(best.chromosome)}") #boolean to know the best guess is the correct one
