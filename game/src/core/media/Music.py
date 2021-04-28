import pygame

class Music:
    PATH = "resources/musics/"
    EXTENSION = ".mp3"
    FADE_OUT = 5000
    VOLUME = 0.5

    @classmethod
    def play(cls, name, loop):
        pygame.mixer.music.load(cls.PATH + name + cls.EXTENSION)
        pygame.mixer.music.set_volume(cls.VOLUME)
        pygame.mixer.music.play(loop)

    @classmethod
    def stop(cls, fadeOut=False):
        if fadeOut:
            pygame.mixer.music.fadeout(cls.FADE_OUT)
        else:
            pygame.mixer.music.stop()
    
