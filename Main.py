from game.src.ui.Window import Window

from game.src.ui.Menu import Menu

class Main:
    def __init__(self):
        self.SEED = 1

        self.__window = Window()

        Menu(self.__window)



if (__name__ == "__main__"):
    Main()