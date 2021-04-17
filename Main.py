from game.src.ui.Window import Window
from game.src.ui.Menu import Menu

from game.src.core.GameLoop import GameLoop

class Main:
    def __init__(self):
        self.__SEED = 1

        self.__window = Window()
        #gameLoop = GameLoop(self.__window, self.__SEED)
        #gameLoop.run()
        Menu(self.__window, self.__SEED)

if (__name__ == "__main__"):
    Main()