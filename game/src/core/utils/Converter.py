from game.src.ui.sprite.Sprite import Sprite

class Converter:

    @staticmethod
    def pixelToIndex(value):
        return value // Sprite.GROUND_TILE_SIZE

    @staticmethod
    def indexToPixel(value):
        return value * Sprite.GROUND_TILE_SIZE