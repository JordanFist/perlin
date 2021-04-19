class Display:
    def __init__(self, window, background):
        self._window = window
        self._background = background

        self._objectsOnScreen = []
        self._objectsToUpdate = []

    def add(self, *objects):
        for obj in objects:
            self._objectsOnScreen.append(obj)

    def remove(self, *objects):
        for obj in objects:
            self._objectsOnScreen.remove(obj)

    def toUpdate(self, *objects):
        for obj in objects:
            self._objectsToUpdate.append(obj)

    def clean(self):
        self._objectsOnScreen = []