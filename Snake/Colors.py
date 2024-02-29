# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

import pygame
import random

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red   = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue  = pygame.Color(0, 0, 255)

# Função para gerar uma cor aleatória
def corzinhas():
    return pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
