from game.src.ui.Sprite import Sprite

class SpriteStore:
    MAIN_CHARACTER = 0

    def __init__(self):
        self.__PATH = "game/resources/"
        self.__NUMBER_OF_SPRITES = {
            "grounds": 4,
            "players": 1
        }
        self.__store = {
            "grounds": [],
            "players": [],
        }
        self.load()
    
    def load(self):
        for folder in self.__store.keys():
            for i in range(self.__NUMBER_OF_SPRITES[folder]):
                sprite = Sprite(self.__PATH + folder + "/" + str(i) + ".png")
                self.__store[folder].append(sprite)

    def get(self, spriteType, spriteNumber):
        return self.__store[spriteType][spriteNumber]

    def getPlayer(self):
        return self.__store["players"][self.MAIN_CHARACTER]

            
                    




        



        
