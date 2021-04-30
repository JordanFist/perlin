from setuptools import setup

APP = ['game/Perlin.py']
DATA_FILES = [('', ['game', 'game/resources'])]
OPTIONS = {'iconfile':'game/resources/icon/icon.icns',}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
