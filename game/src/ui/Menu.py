import pygame

from game.src.core.GameLoop import GameLoop
from game.src.core.media.music.Music import Music
from game.src.core.enums.States import States

from game.src.ui.background.BackgroundImage import BackgroundImage
from game.src.ui.display.DisplayMenu import DisplayMenu
from game.src.ui.widgets.Button import Button
from game.src.ui.widgets.Text import Text
from game.src.ui.utils.Position import Position
from game.src.ui.utils.Margin import Margin

class Menu:
    def __init__(self, window, seed=None):
        self.__seed = seed
        self.__window = window
        self.__background = BackgroundImage("game/resources/backgrounds/menuBackground.png")
        self.__display = DisplayMenu(self.__window, self.__background)

        self.__running = States.CONTINUE
        self.__buttons = []
        self.__initWidget()
        Music.play("Celestial", -1)

        self.run()

    def __initWidget(self):
        startButton = Button("New Game", self.__newGame, Position.CENTER, Margin(50, 0, 0, 0))
        settingsButton = Button("Settings", self.__settings, Position.BOTTOM, Margin(50, 0, 0, 0), startButton)
        quitButton = Button("Quit", self.__closeWindow, Position.BOTTOM, Margin(50, 0, 0, 0), settingsButton)
        self.__buttons = [startButton, settingsButton, quitButton]
        self.__display.add(*self.__buttons)

    def __loading(self):
        loading = Text("Loading...", Position.BOTTOM, Margin(0, 0, 50, 0))
        self.__display.clean()
        self.__display.add(loading)
        self.__display.flip()

    def __newGame(self):
        Music.stop(fadeOut=True)
        self.__loading()
        gameLoop = GameLoop(self.__window, self.__seed)
        self.__running = gameLoop.run()

    def __settings(self):
        print("settings")

    def __closeWindow(self):
        self.__running = False

    def __resize(self, event):
        self.__window.resize(event.w, event.h)
        self.__display.flip()

    def run(self):
        self.__display.flip()

        while self.__running == States.CONTINUE:
            updated = False
            for event in pygame.event.get():
                self.__running = self.__window.isClosed(event)

                if self.__window.isResized(event):
                    self.__resize(event)

                for button in self.__buttons:
                    button.checkEvent(event)

            for button in self.__buttons:
                if button.checkHover():
                    self.__display.toUpdate(button)
                    updated = True
            
            if updated:
                self.__display.update()

            self.__window.clock() 

        self.__window.close()