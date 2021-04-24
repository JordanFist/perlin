class Pair:
    def __init__(self, first, second):
        self._first = first
        self._second = second

    def toTuple(self):
        return (int(self._first), int(self._second))

    def __add__(self, pair):
        if (type(pair) == int):
            return type(self)(self._first + pair, self._second + pair)
        return type(self)(self._first + pair._first, self._second + pair._second)

    def __radd__(self, pair):
        if (type(pair) == int):
            return type(self)(self._first + pair, self._second + pair)

    def __sub__(self, pair):
        return type(self)(self._first - pair._first, self._second - pair._second)

    def __mul__(self, pair):
        if (type(pair) == int):
            return type(self)(self._first * pair, self._second * pair)
        if (type(pair) == float):
            return type(self)(self._first * pair, self._second * pair)
        return type(self)(self._first * pair._first, self._second * pair._second)
    
    def __rmul__(self, pair):
        if (type(pair) == int):
            return type(self)(self._first * pair, self._second * pair)
        if (type(pair) == float):
            return type(self)(self._first * pair, self._second * pair)

    def __floordiv__(self, pair):
        if (type(pair) == int):
            return type(self)(self._first // pair, self._second // pair)
        return type(self)(self._first // pair._first, self._second // pair._second)