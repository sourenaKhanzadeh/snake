import pygame
import random
import res.constants.colors as CC
import res.constants.physics as PS

# ----------------
# CONFIGURATION
# ----------------

screen_w = 500
screen_h = 500


screen = pygame.display.set_mode((screen_w, screen_h))




from res.prefabs.player import Snake
from res.prefabs.food import Food