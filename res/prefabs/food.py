from res.prefabs.gameobjects import GameObject
from settings import *

class Food(GameObject):

    def __init__(self, x=screen_w // 2, y=screen_h // 2, color=CC.RED, w=0, width=PS.FOOD_SIZE, height=PS.FOOD_SIZE):
        super().__init__(x, y, color, w)
        self._width =width
        self._height = height
        self.generator()

    def move(self):
        super().move()

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), self.w)

    def collision(self, col):
        if self.x -self.width <= col.x <= self.x + self.width \
                and self.y - self.height <= col.y <= self.y + self.height:

            self.generator()
            col.len += 1

    def generator(self):
        self.x = random.randint(self.width, screen_w - self.width)
        self.y = random.randint(self.height, screen_h - self.height)

    @property
    def width(self):return self._width
    @property
    def height(self):return self._height

    @width.setter
    def width(self, value):self._width = value
    @height.setter
    def height(self, value):self._height = value