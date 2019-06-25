from res.prefabs.gameobjects import GameObject
from settings import *

class Food(GameObject):

    def __init__(self, x=screen_w // 2, y=screen_h // 2, color=CC.RED, w=0, width=10, height=10):
        super().__init__(x, y, color, w)
        self._width =width
        self._height = height
        self.x = random.randint(self.width, screen_w - self.width)
        self.y = random.randint(self.height, screen_h - self.height)


    def move(self):
        pass

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), self.w)

    def collision(self, col):
        # print(col.x, self.x)
        if self.x in range(col.x, col.x+col.width) and self.y in range(col.y, col.y+col.height):

            self.x = random.randint(self.width, screen_w - self.width)
            self.y = random.randint(self.height, screen_h - self.height)
            col.width += self.width

    @property
    def width(self):return self._width
    @property
    def height(self):return self._height

    @width.setter
    def width(self, value):self._width = value
    @height.setter
    def height(self, value):self._height = value