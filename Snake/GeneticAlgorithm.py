# -------------------------------------------------------------------------------------------------
# import required packages/libraries
# -------------------------------------------------------------------------------------------------
from SnakeGame import *
import random
import csv
import math
# -------------------------------------------------------------------------------------------------
# A class for a Genetic Algorithm 
# -------------------------------------------------------------------------------------------------

class GeneticAlgorithm:
    
    # attributes
    population = []
    # number of Generations to execute
    numberOfGenerations = 10
    # stop GA execution is no improvement is observed after some generations
    stopEarlyCriteria = 5
    # population size
    populationSize = 20
    # mutation rate
    mutationRate = 0.05
    # best individual(s) returned after the GA is executed
    bestIndividuals = []
    # best fitness value(s) obtained by the best individuals 
    bestFitness = []


    seed = 0
    score = 0
    tournamentSize = 3
    qtyFoods = []

    # constructor
    def __init__(self, seed):
        random.seed(seed)
        self.seed = seed
        self.population = []
        self.qtyFoods = []

    # generate the initial population
    def generateInitialPopulation(self):

        for _ in range(self.populationSize):
            numMoves = random.randint(10, 500)
            individual = [random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT']) for _ in range(numMoves)]
            self.population.append(individual) 
    
    # fitness function to evaluate an individual
    def fitnessFunction(self, individual):
       
        game = SnakeGame(self.seed)

        game.moves = individual

        score, foods = game.run()
        
        # Incentivos
        length_fitness = len(game.snake_body) * 10
        survival_time_fitness = (game.endTime - game.startTime) * 100

        # Verifica se a distância da fruta diminuiu ou aumentou e atualiza a pontuação
        new_dist = abs(game.snake_position[0] - game.fruit_position[0]) + abs(game.snake_position[1] - game.fruit_position[1])
        if new_dist < game.fruitDistance:
            score += 50
        elif new_dist > game.fruitDistance:
            score -= 50

        # Função de fitness
        score += length_fitness + survival_time_fitness

        # Impedir score negativo
        if score <= 0:
            score = 1

        return score, foods

    # receive an individual and evaluate its fitness
    def evaluateIndividual(self, individual):
        return self.fitnessFunction(individual)
    
    # given a population, selects two parents for crossover
    def selectParents(self, fitness):

        # Selecionar aleatoriamente indivíduos para o torneio
        candidates = random.choices(self.population, k = self.tournamentSize)

        # Avaliar o desempenho fitness dos candidatos
        fitness_values = [fitness[self.population.index(candidate)] for candidate in candidates]

        # Obter os índices dos dois candidatos com o melhor desempenho fitness
        winner_indices = sorted(range(len(fitness_values)), key=lambda k: fitness_values[k], reverse=True)[:2]

        # Retornar os dois vencedores do torneio
        parents = [candidates[i] for i in winner_indices]

        return parents


    # given two parents, generate two children recombining them
    def generateChildren(self, parents):

        parent1, parent2 = parents

        # Garante que o ponto de corte não é o início ou o final do cromossomo
        crossover_point = random.randint(1, len(parent1) - 1)

        # Realiza o crossover
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]

        return child1, child2
    
    # selects an individual and apply a mutation
    def mutationOperator(self, child):

        for i in range(len(child)):
            if random.random() < self.mutationRate:
                child[i] = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

        return child

    # run GA
    def execute(self):

        # Gera a população inicial
        self.generateInitialPopulation()

        # Calcula o fitness para cada individuo e coloca em uma lista para pegar o melhor
        marombeiros = []
        foods = []
        mean = []

        for individual in self.population:
            marombeiros.append(self.fitnessFunction(individual)[0])
            foods.append(self.fitnessFunction(individual)[1])

        # Atribui o melhor fitness, melhor individuo e a quantidade de comida desta geração
        self.bestFitness.append(max(marombeiros))
        self.bestIndividuals.append(max(self.population, key=self.evaluateIndividual))
        self.qtyFoods.append(sum(foods))
        mean.append(sum(marombeiros) / len(marombeiros))

        print("População inicial: ")
        print("Melhor fitness: ", max(marombeiros))
        print("Média dos fitness: ", sum(marombeiros) / len(marombeiros))
        print("Comidas p/ gen: ", sum(foods))
        print("\n")
        print("-"*50)
        print("\n")

        with open('dados.csv', 'w', newline='',encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Geração', 'Melhor Fitness', 'Média Fitness', 'Comidas p/ gen'])

            for generation in range(self.numberOfGenerations):

                newPopulation = []
                foods = []

                for _ in range(self.populationSize // 2):

                    # Cria os pais
                    parents = self.selectParents(marombeiros)

                    # Cria os filhos
                    children = self.generateChildren(parents)

                    # Chance de mutar os filhos
                    for child in children:

                        child = self.mutationOperator(child)
                        newPopulation.append(child)

                # Adiciona a nova população na população
                self.population = newPopulation

                marombeiros = []

                # Calcula o fitness para cada individuo e coloca em uma lista para pegar o melhor
                for individual in self.population:
                    marombeiros.append(self.fitnessFunction(individual)[0])
                    foods.append(self.fitnessFunction(individual)[1])

                # Atribui o melhor fitness, melhor individuo, quantidade de comida e a média de fitness desta geração
                self.bestFitness.append(max(marombeiros))
                self.bestIndividuals.append(max(self.population, key=self.evaluateIndividual))
                self.qtyFoods.append(sum(foods))
                mean.append(sum(marombeiros) / len(marombeiros))

                writer.writerow([generation, int(max(marombeiros)), int(sum(marombeiros) / len(marombeiros)), sum(foods)])

                print("Geração: ", generation)
                print("Melhor fitness: ", max(marombeiros))
                print("Média dos fitness: ", sum(marombeiros) / len(marombeiros))
                print("Comidas p/ gen: ", sum(foods))
                print("\n")
                print("-"*50)
                print("\n")



        return self.bestIndividuals, self.bestFitness, self.qtyFoods, self.numberOfGenerations, mean
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------