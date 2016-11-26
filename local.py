""" All the global constants for this file. """
import pygame

TILE_SIZE = 50  # Length/width of the tile in pixel units.
TILE_DISTANCE = 5  # Game distance for a tile in meters.

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

BOARD_WIDTH = SCREEN_WIDTH/TILE_SIZE + 1
BOARD_HEIGHT = SCREEN_HEIGHT/TILE_SIZE + 1
print("HEIGHT: {}".format(BOARD_HEIGHT))

# COLORS
WHITE_COLOR = pygame.Color(255, 255, 255)
BLACK_COLOR = pygame.Color(0, 0, 0)
GREEN_COLOR = pygame.Color(0, 255, 0)
RED_COLOR = pygame.Color(255, 0, 0)
sign = lambda x: (x > 0) - (x < 0)  # Get the sign of the variable

FPS = 60  # Frames per second

FONT = pygame.font.SysFont("monospace", 10)