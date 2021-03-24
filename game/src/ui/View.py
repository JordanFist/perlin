from game.src.ui.Sprite import Sprite
from game.src.ui.Display import Display
class View:
    def __init__(self, windowSize):
        # we add 2 tiles on each side (thus 2 * offset) to prevent from buggy scrolling
        self.viewSize = windowSize[0] // Sprite.GROUND_TILE_SIZE + 2 * Display.DISPLAY_OFFSET, windowSize[1] // Sprite.GROUND_TILE_SIZE + 2 * Display.DISPLAY_OFFSET
        self.__deltaRow = self.viewSize[1] // 2
        self.__deltaCol = self.viewSize[0] // 2 

    def get(self, map, playerIndex):
        playerRow = playerIndex[0]
        playerCol = playerIndex[1]

        topLeftCorner = (playerRow - self.__deltaRow, playerCol - self.__deltaCol)

        return map[topLeftCorner[0] : topLeftCorner[0] + self.viewSize[1], topLeftCorner[1] : topLeftCorner[1] + self.viewSize[0]]

