# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from re import X
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


from util import Stack

def depthFirstSearch(problem):
    
    #Inicializacao
    inicial = problem.getStartState();
    abertos = Stack();
    abertos.push((inicial, [], 0));
    fechados = set();
    
    while abertos != []: 

        #Remova o estado mais a esquerda de ABERTOS, chame-o de X
        X, Y, Z = abertos.pop(); # estado, acao, custo
    
        #Se X for um objetivo, entao retornar SUCESSO
        if  problem.isGoalState(X):
            return Y;

        #Senao
        else:
            
            #Coloque X em FECHADOS
            fechados.add(X);

            #Gere filhos de X
            for successor, action, stepCost in problem.getSuccessors(X):

                #Descarte filhos de X que ja estao em ABERTOS ou FECHADOS
                if successor not in fechados:
                    
                    #Coloque os filhos que restam no final a esquerda de ABERTOS
                    novo_passos = Y + [action]
                    novo_custo = Z + stepCost
                    abertos.push((successor, novo_passos, novo_custo))

    return [];


from util import Queue

def breadthFirstSearch(problem):
    
    #Inicializacao
    inicial = problem.getStartState();
    abertos = Queue();
    abertos.push((inicial, [], 0));
    fechados = set();
    
    while abertos != []: 

        #Remova o estado mais a esquerda de ABERTOS, chame-o de X
        X, Y, Z = abertos.pop(); # estado, acao, custo  
    
        #Se X for um objetivo, entao retornar SUCESSO
        if  problem.isGoalState(X):
            return Y;

        #Senao
        else:
            
            #Coloque X em FECHADOS
            fechados.add(X);

            #Gere filhos de X
            for successor, action, stepCost in problem.getSuccessors(X):

                #Descarte filhos de X que ja estao em ABERTOS ou FECHADOS
                if successor not in fechados:
                    
                    #Coloque os filhos que restam no final a direita de ABERTOS
                    novo_passos = Y + [action]
                    novo_custo = Z + stepCost
                    abertos.push((successor, novo_passos, novo_custo))

    return [];

from util import PriorityQueue

def uniformCostSearch(problem):
    
    #Inicializacao
    inicial = problem.getStartState();
    abertos = PriorityQueue();
    abertos.push((inicial, [], 0),0);
    fechados = set();
    
    while abertos != []: 

        #Remova o estado mais a esquerda de ABERTOS, chame-o de X
        X, Y, Z = abertos.pop();  # estado, acao, custo
    
        #Se X for um objetivo, entao retornar SUCESSO
        if  problem.isGoalState(X):
            return Y;

        #Senao
        else:
            
            #Coloque X em FECHADOS
            fechados.add(X);

            #Gere filhos de X
            for successor, action, stepCost in problem.getSuccessors(X):

                #Descarte filhos de X que ja estao em ABERTOS ou FECHADOS
                if successor not in fechados:
                    
                    #Coloque os filhos que restam no final a direita de ABERTOS
                    novo_passos = Y + [action]
                    novo_custo = Z + stepCost
                    abertos.push((successor, novo_passos, novo_custo),novo_custo)
    
    return [];

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    #Inicializacao
    inicial = problem.getStartState();
    abertos = PriorityQueue();
    abertos.push((inicial, [], 0), heuristic(inicial, problem));
    fechados = set();
    
    while abertos != []: 

        #Remova o estado mais a esquerda de ABERTOS, chame-o de X
        X, Y, Z = abertos.pop(); # estado, acao, custo
    
        #Se X for um objetivo, entao retornar SUCESSO
        if  problem.isGoalState(X):
            return Y;

        #Senao
        else:
            
            #Coloque X em FECHADOS
            fechados.add(X);

            #Gere filhos de X
            for successor, action, stepCost in problem.getSuccessors(X):

                #Descarte filhos de X que ja estao em ABERTOS ou FECHADOS
                if successor not in fechados:
                    
                    #Coloque os filhos que restam no final a direita de ABERTOS
                    novo_passos = Y + [action]
                    novo_custo = Z + stepCost
                    abertos.push((successor, novo_passos, novo_custo), heuristic(successor, problem))

    return [];

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
