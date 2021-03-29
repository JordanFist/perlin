#from enum import Enum

class TilesEnum:
    DEEP_WATER_THRESHOLD = 0
    SHALLOW_WATER_THRESHOLD = 0.37
    SAND_THRESHOLD = 0.45
    GRASS_THRESHOLD = 0.5
    #STONE_THRESHOLD = 0.85
    #SNOW_THRESHOLD = 0.95

    DEEP_WATER = 0
    SHALLOW_WATER = 1
    SAND = 2
    GRASS = 3

    @classmethod
    def getID(self, value):
        if value > self.GRASS_THRESHOLD:
            return self.GRASS
        elif value > self.SAND_THRESHOLD:
            return self.SAND
        elif value > self.SHALLOW_WATER_THRESHOLD:
            return self.SHALLOW_WATER
        elif value >= self.DEEP_WATER_THRESHOLD:
            return self.DEEP_WATER

#for tile in Tiles:      
    #print(tile.name, tile.value)