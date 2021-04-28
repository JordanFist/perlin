class Tiles:
    PATCH_RANGE = 100

    # Threshold values
    DEEP_WATER_THRESHOLD = 0
    SHALLOW_WATER_THRESHOLD = 0.37
    SAND_THRESHOLD = 0.45
    GRASS_THRESHOLD = 0.5

    # Tile ID
    DEEP_WATER = 0
    SHALLOW_WATER = 1
    SAND = 2
    GRASS = 3

    # Patch ID
    TOP_EDGE = 1
    LEFT_EDGE = 2
    BOTTOM_EDGE = 3
    RIGHT_EDGE = 4
    TOP_LEFT_CORNER = 5
    BOTTOM_LEFT_CORNER = 6
    BOTTOM_RIGHT_CORNER = 7
    TOP_RIGHT_CORNER = 8
    TOP_LEFT_PATCH = 9
    BOTTOM_LEFT_PATCH = 10
    BOTTOM_RIGHT_PATCH = 11
    TOP_RIGHT_PATCH = 12

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
        
        raise Exception("the function should return an enum")

    @classmethod
    def getPatches(cls, map, row, col):
        middle = cls.getID(map[row][col])
        left = cls.getID(map[row][col - 1]) if col - 1 >= 0 else None
        bottom = cls.getID(map[row + 1][col]) if row + 1 < len(map) else None
        right = cls.getID(map[row][col + 1]) if col + 1 < len(map[0]) else None
        top = cls.getID(map[row - 1][col]) if row - 1 >= 0 else None
        topLeft = cls.getID(map[row - 1][col - 1]) if row - 1 >= 0 and col - 1 >= 0 else None
        bottomLeft = cls.getID(map[row + 1][col - 1]) if row + 1 < len(map) and col - 1 >= 0 else None
        bottomRight = cls.getID(map[row + 1][col + 1]) if row + 1 < len(map) and col + 1 < len(map[0]) else None
        topRight = cls.getID(map[row - 1][col + 1]) if row - 1 >= 0 and col + 1 < len(map[0]) else None

        patches = [middle]

        if middle != cls.GRASS:
            # Handles edges
            if top != None and top > middle: 
                patches.append(top * cls.PATCH_RANGE + cls.TOP_EDGE)
            if left != None and left > middle:
                patches.append(left * cls.PATCH_RANGE + cls.LEFT_EDGE)
            if bottom != None and bottom > middle:
                patches.append(bottom * cls.PATCH_RANGE + cls.BOTTOM_EDGE)
            if right != None and right > middle:
                patches.append(right * cls.PATCH_RANGE + cls.RIGHT_EDGE)

            patches[1:] = sorted(patches[1:]) # Tiles with a bigger enum are on tiles with a lower enum

            # Handles corner patches
            if top != None and top == left and top > middle:
                patches.append(top * cls.PATCH_RANGE + cls.TOP_LEFT_PATCH)
            if left != None and left == bottom and left > middle:
                patches.append(left * cls.PATCH_RANGE + cls.BOTTOM_LEFT_PATCH)
            if bottom != None and bottom == right and bottom > middle:
                patches.append(bottom * cls.PATCH_RANGE + cls.BOTTOM_RIGHT_PATCH)
            if right != None and right == top and right > middle:
                patches.append(right * cls.PATCH_RANGE + cls.TOP_RIGHT_PATCH)

            # Handles corner
            if top != None and left != None and topLeft != None and top < topLeft > left and middle < topLeft:
                patches.append(topLeft * cls.PATCH_RANGE + cls.TOP_LEFT_CORNER)
            if left != None and bottom != None and bottomLeft != None and left < bottomLeft > bottom and middle < bottomLeft:
                patches.append(bottomLeft * cls.PATCH_RANGE + cls.BOTTOM_LEFT_CORNER)
            if bottom != None and right != None and bottomRight != None and bottom < bottomRight > right and middle < bottomRight:
                patches.append(bottomRight * cls.PATCH_RANGE + cls.BOTTOM_RIGHT_CORNER)
            if right != None and top != None and topRight != None and right < topRight > top and middle < topRight:
                patches.append(topRight * cls.PATCH_RANGE + cls.TOP_RIGHT_CORNER)
        
        return patches