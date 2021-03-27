from game.src.ui.Sprite import Sprite

class SpriteStore:

    def __init__(self):
        self.PATH = "game/resources/"

        self.__NUMBER_OF_SPRITES = {
            "grounds": 4,
            "players": 1
        }
        
        self.store = {
            "grounds": [],
            "players": [],
        }

        self.load()

    
    def load(self):
        for folder in self.store.keys():
            for i in range(self.__NUMBER_OF_SPRITES[folder]):
                sprite = Sprite(self.PATH + folder + "/" + str(i) + ".png")
                self.store[folder].append(sprite)

    def get(self, spriteType, spriteNumber):
        return self.store[spriteType][spriteNumber]

            
                    




        



        
