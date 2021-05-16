import pygame
from time import sleep

from src.core.enums.States import States

from src.ui.background.BackgroundImage import BackgroundImage
from src.ui.display.DisplayPause import DisplayPause
from src.ui.utils.Position import Position
from src.ui.widgets.Button import Button
from src.ui.utils.Margin import Margin

class Pause:
    WAITING_TIME = 0.2

    def __init__(self, window, displayGame):
        sleep(self.WAITING_TIME)
        self.__running = States.RUNNING
        self.__window = window
        self.__background = BackgroundImage("resources/backgrounds/pauseBackground.png")

        self.__display = DisplayPause(self.__window, self.__background, displayGame)
        self.__buttons = []
        self.__initWidget()

    def __initWidget(self):
        settingsButton = Button("Settings", self.__settings, Position.CENTER)
        resumeButton = Button("Resume", self.__resume, Position.TOP, Margin(-70, 0, 0, 0), settingsButton)
        backToMenuButton = Button("Back To Menu", self.__backToMenu, Position.BOTTOM, Margin(70, 0, 0, 0), settingsButton)
        self.__buttons = [settingsButton, resumeButton, backToMenuButton]
        self.__display.add(*self.__buttons)

    def __resume(self):
        self.__running = States.BACK

    def __settings(self):
        print("settings")

    def __backToMenu(self):
        self.__running = States.BACK_TO_MENU

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

            if (pygame.key.get_pressed()[pygame.K_ESCAPE]):
                self.__running = States.BACK

            for button in self.__buttons:
                if button.checkHover():
                    self.__display.flip()

            self.__window.clock() 
        
        sleep(self.WAITING_TIME)
        return States.get(self.__window, self.__running)
