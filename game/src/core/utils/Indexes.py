from src.core.utils import Pair 

class Indexes(Pair.Pair):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.__row = row
        self.__col = col

    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, value):
        self.__row = value
        self._first = value

    @property
    def col(self):
        return self.__col

    @col.setter
    def col(self, value):
        self.__col = value
        self._second = value



    