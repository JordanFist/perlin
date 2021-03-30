class TilesEnum:
    # Threshold values
    DEEP_WATER_THRESHOLD = 0
    SHALLOW_WATER_THRESHOLD = 0.37
    SAND_THRESHOLD = 0.45
    GRASS_THRESHOLD = 0.5

    # ID Tile values
    DEEP_WATER = 0
    SHALLOW_WATER = 1
    SAND = 2
    GRASS = 3

    @classmethod
    def getID(cls, value):
        if value > cls.GRASS_THRESHOLD:
            return cls.GRASS
        elif value > cls.SAND_THRESHOLD:
            return cls.SAND
        elif value > cls.SHALLOW_WATER_THRESHOLD:
            return cls.SHALLOW_WATER
        elif value >= cls.DEEP_WATER_THRESHOLD:
            return cls.DEEP_WATER
