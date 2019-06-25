from settings import *


run = True

while run:

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        run = False

    # update the screen
    screen_update()

pygame.quit()