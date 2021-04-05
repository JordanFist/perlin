class Display:
    def __init__(self, window, camera, background, spriteStore):
        self.__window = window
        self.__camera = camera
        self.__background = background
        self.__spriteStore = spriteStore

    def update(self, player):
        cameraPosition = self.__camera.get()
        topLeft = self.__window.getScreen().get_rect(topleft = cameraPosition.toTuple())
        self.__window.getScreen().blit(self.__background.get(), (0, 0), topLeft)

        playerSprite = self.__spriteStore.getPlayer()
        playerSprite.setPosition(player.getPosition() - cameraPosition)
        self.__window.getScreen().blit(playerSprite.get(), playerSprite.getRect())