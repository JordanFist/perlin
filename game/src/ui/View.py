from game.src.ui.Sprite import Sprite
from math import ceil

class View:
    def __init__(self, windowSize):
        self.viewSize = (ceil(windowSize[0] / Sprite.GROUND_TILE_SIZE), ceil(windowSize[1] / Sprite.GROUND_TILE_SIZE))

    def get(self, map, playerIndex):
        row = playerIndex[0]
        col = playerIndex[1]

        deltaRow = self.viewSize[1] // 2 + 1
        deltaCol = self.viewSize[0] // 2 + 1 

        

        #print(row - deltaRow , row + deltaRow, col - deltaCol , col + deltaCol)

        return map[row - deltaRow : row + deltaRow, col - deltaCol : col + deltaCol]

