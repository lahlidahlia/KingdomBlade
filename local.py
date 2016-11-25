""" All the global constants for this file. """
import pygame
from collections import namedtuple

TILE_SIZE = 50  # Length/width of the tile in pixel units.
TILE_DISTANCE = 5  # Game distance for a tile in meters.
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

# COLORS
WHITE_COLOR = pygame.Color(255, 255, 255)
BLACK_COLOR = pygame.Color(0, 0, 0)
GREEN_COLOR = pygame.Color(0, 255, 0)
RED_COLOR = pygame.Color(255, 0, 0)
sign = lambda x: (x > 0) - (x < 0)  # Get the sign of the variable

FPS = 60  # Frames per second