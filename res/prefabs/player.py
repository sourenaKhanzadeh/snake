from res.prefabs.gameobjects import GameObject
from settings import *

class Snake(GameObject):

    def __init__(self, x=screen_w // 2, y=screen_h // 2, color=CC.RED, w=0, width=PS.SNAKE_SIZE, height=PS.SNAKE_SIZE):
        super().__init__(x, y, color, w)
        self._width =width
        self._height = height
        self.direction = 'r'
        self.head = [self.x, self.y]
        self.body = [self.head]
        self.len = PS.LEN_SNAKE
        self.margin = 0


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
            self.body.append([self.x +self.width, self.y])
            self.x += self.width
        elif self.direction == 'd':
            self.body.append([self.x , self.y + self.height])
            self.y += self.height
        elif self.direction == 'l':
            self.body.append([self.x - self.width , self.y])
            self.x -= self.width
        else:
            self.body.append([self.x , self.y - self.height])
            self.y -= self.width

        if len(self.body) > self.len:
            del self.body[0]

    def draw(self):
        skin = pygame.Surface((self.width, self.height))
        skin.fill(self.color)

        for pos in self.body:
            screen.blit(skin, pos)

    @property
    def width(self):return self._width
    @property
    def height(self):return self._height

    @width.setter
    def width(self, value):self._width = value
    @height.setter
    def height(self, value):self._height = value