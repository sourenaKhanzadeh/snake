from abc import ABC, abstractmethod
from settings import CC, PS, screen_h, screen_w

class GameObject(ABC):

    def __init__(self, x=screen_w//2, y=screen_h//2, color=CC.RED, w=0):
        self._x = x
        self._y = y
        self._color = color
        self._w = w
        self._dx = self._dy = PS.DEFAULT_VELOCITY

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
        self.move()



    @property
    def x(self):return self._x
    @property
    def y(self):return self._y
    @property
    def color(self):return self._color
    @property
    def w(self):return self._w
    @property
    def dx(self):return self._dx
    @property
    def dy(self):return self._dy

    @x.setter
    def x(self, value):self._x = value
    @y.setter
    def y(self, value):self._y = value
    @color.setter
    def color(self, value):self._color = value
    @w.setter
    def w(self, value):self._w = value
    @dx.setter
    def dx(self, value):self._dx = value
    @dy.setter
    def dy(self, value):self._dy = value