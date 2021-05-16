class States:
    QUIT = 0
    RUNNING = 1
    BACK = 2
    BACK_TO_MENU = 3

    @classmethod
    def get(cls, window, running):
        if running == cls.QUIT:
            window.close()
        if running == cls.BACK:
            return cls.RUNNING
        if running == cls.BACK_TO_MENU:
            return cls.BACK