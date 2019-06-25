import pygame
import res.constants.colors as CC

# ----------------
# CONFIGURATION
# ----------------

screen_w = 500
screen_h = 500


screen = pygame.display.set_mode((screen_w, screen_h))



def screen_update():
    # update the screen
    pygame.display.update()
    # bg color
    screen.fill(CC.WHITE)

