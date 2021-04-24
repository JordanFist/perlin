from src.core.GameLoop import GameLoop

from src.ui.Window import Window
from src.ui.Menu import Menu

class Perlin:
    def __init__(self):
        self.__SEED = 1

        self.__window = Window()
        gameLoop = GameLoop(self.__window, self.__SEED)
        gameLoop.run()
        #Menu(self.__window, self.__SEED)

if (__name__ == "__main__"):
    Perlin()