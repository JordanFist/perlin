import glob, os

from game.src.ui.sprite.Sprite import Sprite

class SpriteStore:
    MAIN_CHARACTER = 0

    def __init__(self):
        self.__PATH = "game/resources/graphics/"
        self.__store = {}

        self.load()
    
    def load(self):
        folders = [os.path.basename(folder) for folder in glob.glob(self.__PATH + "*")]
        for folder in folders:
            self.__store[folder] = []
            numberOfSprites = len(glob.glob1(self.__PATH + folder, "*.png"))
            for i in range(numberOfSprites):
                sprite = Sprite(self.__PATH + folder + "/" + str(i) + ".png")
                self.__store[folder].append(sprite)

    def get(self, spriteType, spriteNumber):
        return self.__store[spriteType][spriteNumber]

    def getPlayer(self):
        return self.__store["sprites"][self.MAIN_CHARACTER]

            
                    




        



        
