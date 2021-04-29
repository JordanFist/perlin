import glob, os

from src.ui.sprite.Sprite import Sprite

"""
The store dictionary contains the keys:
    tiles -> referring to a dict of tile sprites
    player -> referring to a dict of player sprites
"""
class SpriteStore:
    def __init__(self):
        self.__PATH = "resources/graphics/"
        self.__store = {}

        self.__load()
    
    def __load(self):
        folders = [os.path.basename(folder) for folder in glob.glob(self.__PATH + "*")]
        for folder in folders:
            self.__store[folder] = {}
            fileNames = [os.path.splitext(os.path.basename(fileName))[0] for fileName in glob.glob(self.__PATH + folder + "/" + "*")]
            for i in fileNames:
                sprite = Sprite(self.__PATH + folder + "/" + i + ".png")
                self.__store[folder][int(i)] = sprite

    def getTiles(self, id):
        return self.__store["tiles"][id]

    def getPlayer(self):
        return self.__store["player"]

            
                    




        



        
