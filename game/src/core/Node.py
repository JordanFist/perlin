class Node:
    def __init__(self, patches):
        self.__tileID = patches[0]
        self.__patches = patches
        self.__overTileID = -1
        self.__neighbors = set()
    
    def getTileID(self):
        return self.__tileID

    def getPatches(self):
        return self.__patches

    def getOverTileID(self):
        return self.__overTileID

    def getNeighbors(self):
        return self.__neighbors

    def connect(self, node):
        self.__neighbors.add(node)
        node.__neighbors.add(self)

    def disconnect(self, node):
        self.__neighbors.discard(node)
        node.neighbors.discard(self)