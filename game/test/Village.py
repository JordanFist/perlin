from game.src.core.Map import Map
from game.src.core.Tiles import Tiles
from time import time
from random import sample

class Village:
    def __init__(self):
        self.findVillagePosition()

    def findVillagePosition(self):
        map = Map(1)
        matrix = map.get()
        start = time()
        subMatrix = [
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS],
            [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS]
        ]
        villages = []
        matrixWidth, matrixHeight = len(matrix[0]), len(matrix)
        subMatrixWidth, subMatrixHeight = len(subMatrix[0]), len(subMatrix) 
        visited = {}
        for i in range(matrixHeight - subMatrixHeight + 1):
            for j in range(matrixWidth - subMatrixWidth + 1):
                rightPosition = True
                if (i, j) not in visited:
                    for k in range(subMatrixHeight):
                        for l in range(subMatrixWidth):
                            if subMatrix[k][l] != Tiles.getID(matrix[i + k][j + l]):
                                self.add(visited, (i, j), (i+k, j+l))
                                rightPosition = False
                                break
                        if not rightPosition:
                            break
                    if rightPosition:
                        villages.append((i, j))
                        
        #print(villages)
        print(time() - start)
        #print(sample(villages, 4))
    
    def add(self, visited, start, end): 
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                visited[(i, j)] = False



