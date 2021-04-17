from game.src.core.pair import Pair 

class Dimensions(Pair.Pair):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        self._first = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        self._second = value



    