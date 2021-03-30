from game.src.ui.Sprite import Sprite
from game.src.ui.Display import Display
from game.src.ui.Window import Window

class View:
    def __init__(self):
        # we add 2 tiles on each side (thus 2 * offset) to prevent from buggy scrolling
        self.__viewSize = Window.getWidth() // Sprite.GROUND_TILE_SIZE + 2 * Display.BUFFER, Window.getHeight() // Sprite.GROUND_TILE_SIZE + 2 * Display.BUFFER
        self.__view = []
        self.__deltaRow = self.__viewSize[1] // 2
        self.__deltaCol = self.__viewSize[0] // 2 

    def get(self):
        return self.__view

    def getViewSize(self):
        return self.__viewSize

    def setView(self, map, player):
        playerRow, playerCol = map.getIndex(player.getPosition())
        topLeftCorner = (playerRow - self.__deltaRow, playerCol - self.__deltaCol)
        self.__view = map.get()[topLeftCorner[0] : topLeftCorner[0] + self.__viewSize[1], topLeftCorner[1] : topLeftCorner[1] + self.__viewSize[0]]

    def isInMap(self, map, player, direction):
        nextPosition = player.getNextPosition(direction)
        return  (nextPosition[0] > Window.getWidth() // 2 + Display.BUFFER * Sprite.GROUND_TILE_SIZE) and \
                (nextPosition[0] < map.getSize()[0] - (Window.getWidth() // 2) - Display.BUFFER * Sprite.GROUND_TILE_SIZE) and \
                (nextPosition[1] > Window.getHeight() // 2 + Display.BUFFER * Sprite.GROUND_TILE_SIZE) and \
                (nextPosition[1] < map.getSize()[1] - (Window.getHeight() // 2) - Display.BUFFER * Sprite.GROUND_TILE_SIZE)