from game.src.core.GameLoop import GameLoop

class Main:
    def __init__(self):
        self.SEED = None

        gameLoop = GameLoop(self.SEED)


if (__name__ == "__main__"):
    Main()