import glob, os

from src.ui.sprite.Sprite import Sprite

"""
The store dictionary contains the keys:
    tiles -> referring to an array of tile sprites
    player -> referring to an array of player sprites
"""
class SpriteStore:
    def __init__(self):
        self.__PATH = "resources/graphics/"
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

    def getTiles(self, id):
        return self.__store["tiles"][id]

    def getPlayer(self):
        return self.__store["player"]

            
                    




        



        
