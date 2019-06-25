from abc import ABC, abstractmethod
from settings import CC, screen_h, screen_w

class GameObject(ABC):

    def __init__(self, x=screen_w//2, y=screen_h//2, color=CC.RED, w=0):
        self._x = x
        self._y = y
        self._color = color
        self._w = w

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def destroy(self):
        pass

    def update(self):
        self.draw()
        self.update()



    @property
    def x(self):return self._x
    @property
    def y(self):return self._y
    @property
    def color(self):return self._color
    @property
    def w(self):return self._w

    @x.setter
    def x(self, value):self._x = value
    @y.setter
    def y(self, value):self._y = value
    @color.setter
    def color(self, value):self._color = value
    @w.setter
    def w(self, value):self._w = value