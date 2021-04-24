class Sprites:
    NUMBER_OF_ANIMATION_FRAMES = 4

    def __init__(self, sprites):
        self.__INIT_SPRITE = 4

        self.__sprites = sprites

    def get(self, index):
        return self.__sprites[index]

    def init(self):
        return self.__sprites[self.__INIT_SPRITE]

    def idle(self, direction):
        return self.__sprites[direction * self.NUMBER_OF_ANIMATION_FRAMES]