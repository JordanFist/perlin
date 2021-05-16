import pygame

from src.core.GameLoop import GameLoop
from src.core.media.Music import Music
from src.core.enums.States import States

from src.ui.background.BackgroundImage import BackgroundImage
from src.ui.display.DisplayMenu import DisplayMenu
from src.ui.widgets.Button import Button
from src.ui.widgets.Text import Text
from src.ui.utils.Position import Position
from src.ui.utils.Margin import Margin

class Menu:
    def __init__(self, window, seed=None):
        self.__seed = seed
        self.__window = window
        self.__background = BackgroundImage("resources/backgrounds/menuBackground.png")
        self.__display = DisplayMenu(self.__window, self.__background)

        self.__running = States.RUNNING
        self.__buttons = []
        self.__initWidget()
        Music.play("Celestial", -1)

        self.run()

    def __initWidget(self):
        startButton = Button("New Game", self.__newGame, Position.CENTER, Margin(50, 0, 0, 0))
        settingsButton = Button("Settings", self.__settings, Position.BOTTOM, Margin(70, 0, 0, 0), startButton)
        quitButton = Button("Quit", self.__window.close, Position.BOTTOM, Margin(70, 0, 0, 0), settingsButton)
        self.__buttons = [startButton, settingsButton, quitButton]
        self.__display.add(*self.__buttons)

    def __loading(self):
        loading = Text("Loading", Position.BOTTOM, Margin(0, 0, 50, 0))
        self.__display.clean()
        self.__display.add(loading)
        self.__display.flip()

    def __newGame(self):
        Music.stop(fadeOut=True)
        self.__loading()
        gameLoop = GameLoop(self.__window, self.__seed)
        self.__running = gameLoop.run()
        self.__display.clean()
        self.__initWidget()
        self.__display.flip()

    def __settings(self):
        print("settings")

    def __resize(self, event):
        self.__window.resize(event.w, event.h)
        for button in self.__buttons:
            button.initRect()
        self.__display.flip()

    def run(self):
        self.__display.flip()

        while self.__running == States.RUNNING:
            for event in pygame.event.get():
                if self.__window.isClosed(event):
                    self.__running = States.QUIT

                if self.__window.isResized(event):
                    self.__resize(event)

                for button in self.__buttons:
                    button.checkEvent(event)

            for button in self.__buttons:
                if button.checkHover():
                    self.__display.flip()

            self.__window.clock() 

        return States.get(self.__window, self.__running)