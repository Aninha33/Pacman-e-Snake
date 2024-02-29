# -------------------------------------------------------------------------------------------------
# # importing all required objects
# -------------------------------------------------------------------------------------------------
from SnakeGame import *
from GeneticAlgorithm import *

import matplotlib.pyplot as plt
# -------------------------------------------------------------------------------------------------
# # main function 
# -------------------------------------------------------------------------------------------------

seed = 33

if __name__ == "__main__":

    ag = GeneticAlgorithm(seed)
    bestIndividual, bestFitness, qtyFoods, numberOfGenerations, mean = ag.execute()

   # Encontrar a posição do valor máximo em bestFitness
    index = bestFitness.index(max(bestFitness))

    print("Melhor indivíduo:", bestIndividual[index])
    print("Melhor fitness:", max(bestFitness))
    print("Número total de comidas consumidas:", sum(qtyFoods))
    print("Número de gerações:", numberOfGenerations)

    game = SnakeGame(seed)
    game.moves = bestIndividual[index]
    game.run()
    
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------