from game.src.ui.Window import Window

class Camera:
    def __init__(self, player, mapSize):
        self.__player = player
        self.__mapSize = mapSize
        self.__camera = None
        self.resetCamera()
    
    """ Returns the camera top left coordinates """
    def get(self):
        playerBarycenter = self.__player.getPosition() + self.__player.getSprite().getSize() // 2

        if (playerBarycenter.x - self.__camera.x < Window.getSize().width // 4):
            self.__camera.x = max(0, playerBarycenter.x - Window.getSize().width // 4)

        if (playerBarycenter.x - self.__camera.x > Window.getSize().width - Window.getSize().width // 4):
            self.__camera.x = min(self.__mapSize.width - Window.getSize().width, playerBarycenter.x - (Window.getSize().width - Window.getSize().width // 4))

        if (playerBarycenter.y - self.__camera.y < Window.getSize().height // 4):
            self.__camera.y = max(0, playerBarycenter.y - Window.getSize().height // 4)

        if (playerBarycenter.y - self.__camera.y > Window.getSize().height - Window.getSize().height // 4):
            self.__camera.y = min(self.__mapSize.height - Window.getSize().height, playerBarycenter.y - (Window.getSize().height - Window.getSize().height // 4))

        return self.__camera

    def resetCamera(self):
        self.__camera = self.__player.getPosition() + self.__player.getSprite().getSize() // 2 - Window.getSize() // 2
        self.__camera.x = min(self.__mapSize.width - Window.getSize().width, max(0, self.__camera.x))
        self.__camera.y = min(self.__mapSize.height - Window.getSize().height, max(0, self.__camera.y))

    """
    def get(self): 
        playerBarycenter = self.__player.getPosition() + self.__player.getSprite().getSize() // 2
        self.__camera = playerBarycenter - Window.getSize() // 2

        if (playerBarycenter.x < Window.getSize().width // 2):
            self.__camera.x = 0

        if (playerBarycenter.x > self.__mapSize.width - Window.getSize().width // 2):
            self.__camera.x = self.__mapSize.width - Window.getSize().width

        if (playerBarycenter.y < Window.getSize().height // 2):
            self.__camera.y = 0

        if (playerBarycenter.y > self.__mapSize.height - Window.getSize().height // 2):
            self.__camera.y = self.__mapSize.height - Window.getSize().height

        return self.__camera 
    """