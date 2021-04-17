from game.src.core.utils import Pair

class Coordinates(Pair.Pair):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        self._first = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        self._second = value