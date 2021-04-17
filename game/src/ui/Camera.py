from game.src.ui.Window import Window

class Camera:
    def __init__(self, player, mapSize):
        self.__player = player
        self.__mapSize = mapSize
        self.__hasMoved = False
        self.__camera = None
        self.resetCamera()
    
    """ Returns the camera top left coordinates """
    def get(self):
        playerBarycenter = self.__player.getPosition() + self.__player.getSprite().getSize() // 2
        self.__hasMoved = False

        if (playerBarycenter.x - self.__camera.x < Window.getSize().width // 4):
            self.__camera.x = max(0, playerBarycenter.x - Window.getSize().width // 4)
            self.__hasMoved = True

        if (playerBarycenter.x - self.__camera.x > Window.getSize().width - Window.getSize().width // 4):
            self.__camera.x = min(self.__mapSize.width - Window.getSize().width, playerBarycenter.x - (Window.getSize().width - Window.getSize().width // 4))
            self.__hasMoved = True

        if (playerBarycenter.y - self.__camera.y < Window.getSize().height // 4):
            self.__camera.y = max(0, playerBarycenter.y - Window.getSize().height // 4)
            self.__hasMoved = True

        if (playerBarycenter.y - self.__camera.y > Window.getSize().height - Window.getSize().height // 4):
            self.__camera.y = min(self.__mapSize.height - Window.getSize().height, playerBarycenter.y - (Window.getSize().height - Window.getSize().height // 4))
            self.__hasMoved = True

        return self.__camera

    def hasMoved(self):
        return self.__hasMoved

    def resetCamera(self):
        self.__camera = self.__player.getPosition() + self.__player.getSprite().getSize() // 2 - Window.getSize() // 2
        self.__camera.x = min(self.__mapSize.width - Window.getSize().width, max(0, self.__camera.x))
        self.__camera.y = min(self.__mapSize.height - Window.getSize().height, max(0, self.__camera.y))

    def isOnScreen(self, position):
        if (0 < position.x - self.__camera.x < Window.getSize().width) and 0 < position.y - self.__camera.y < Window.getSize().height:
            return True
        return False