from game.src.ui.Window import Window
from game.src.ui.gui.Menu import Menu

class Main:
    def __init__(self):
        self.__SEED = 1

        self.__window = Window()
        Menu(self.__window, self.__SEED)

if (__name__ == "__main__"):
    Main()