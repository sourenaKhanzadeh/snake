from settings import *

scene = []

def init():
    scene.append(Snake())
    scene.append(Food())

def collision():
    scene[1].collision(scene[0])

init()

def screen_update():
    # game delay
    pygame.time.delay(PS.DEFAULT_TIME_DELAY)
    # update the screen
    pygame.display.update()
    # bg color
    screen.fill(CC.WHITE)
    # update the scene
    for gameObject in scene:
        gameObject.update()

    # check for collisions
    collision()


clock = pygame.time.Clock()

run = True

while run:
    clock.tick(PS.FPS)
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        run = False

    # update the screen
    screen_update()

pygame.quit()