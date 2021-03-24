from game.src.core.GameLoop import GameLoop

class Main:
    def __init__(self):
        self.SEED = 1

        gameLoop = GameLoop(self.SEED)


if (__name__ == "__main__"):
    main = Main()