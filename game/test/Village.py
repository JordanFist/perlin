from game.src.core.Map import Map
from game.src.core.TilesEnum import TilesEnum
from time import time
from random import sample

class Village:
    def __init__(self):
        self.findVillagePosition()

    def findVillagePosition(self):
        map = Map(1)
        start = time()
        matrix = map.get()
        villages = []
        subMatrix = [
            [TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS],
            [TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS],
            [TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS],
            [TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS],
            [TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS],
            [TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS, TilesEnum.GRASS]
        ]
        width, height = len(map.get()[0]), len(map.get()[1])
        for i in range(height):
            for j in range(width):
                if (TilesEnum.getID(matrix[i][j]) == subMatrix[0][0]):
                    rightPosition = True
                    for k in range(len(subMatrix)):
                        for l in range(len(subMatrix[0])):
                            if subMatrix[k][l] != TilesEnum.getID(matrix[i + k][j + l]):
                                rightPosition = False
                                break
                        if not rightPosition:
                            break
                    if rightPosition:
                        villages.append((i, j))
        print(villages)
        print(time() - start)
        print(sample(villages, 4))


