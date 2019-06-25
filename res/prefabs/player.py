from res.prefabs.gameobjects import GameObject
from settings import *

class Snake(GameObject):

    def __init__(self, x=screen_w // 2, y=screen_h // 2, color=CC.RED, w=0, width=10, height=10):
        super().__init__(x, y, color, w)
        self._width =width
        self._height = height
        self.direction = 'r'


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction = 'r'
        elif keys[pygame.K_DOWN]:
            self.direction = 'd'
        elif keys[pygame.K_UP]:
            self.direction = 'u'
        elif keys[pygame.K_LEFT]:
            self.direction = 'l'

        if self.direction == 'r':
            self.x += self.dx
        elif self.direction == 'd':
            self.y += self.dy
        elif self.direction == 'l':
            self.x -= self.dx
        else:
            self.y -= self.dy

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), self.w)


    @property
    def width(self):return self._width
    @property
    def height(self):return self._height

    @width.setter
    def width(self, value):self._width = value
    @height.setter
    def height(self, value):self._height = value