import os, sys, pathlib

class PathManager:
    PATH = os.getcwd()

    @classmethod
    def addPath(cls, relative_path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, str(pathlib.Path(relative_path)))