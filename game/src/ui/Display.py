import pygame
from game.src.ui.Sprite import Sprite

class Display:
    DISPLAY_OFFSET = 2

    def __init__(self):

        self.DEEP_WATER_THRESHOLD = 0.37
        self.SHALLOW_WATER_THRESHOLD = 0.45
        self.GRASS_THRESHOLD = 0.5
        self.STONE_THRESHOLD = 0.85
        self.SNOW_THRESHOLD = 0.95

    def update(self, view, screen, playerOffSet):
        xOff = playerOffSet[0]
        yOff = playerOffSet[1]
        for row in range(len(view)):
            for col in range(len(view[0])):
                if view[row][col] > self.SNOW_THRESHOLD:
                    pygame.draw.rect(screen, "white", pygame.Rect((col - self.DISPLAY_OFFSET) * Sprite.GROUND_TILE_SIZE - xOff, (row - self.DISPLAY_OFFSET) * Sprite.GROUND_TILE_SIZE - yOff, Sprite.GROUND_TILE_SIZE, Sprite.GROUND_TILE_SIZE))
                elif view[row][col] > self.STONE_THRESHOLD:
                    pygame.draw.rect(screen, "grey", pygame.Rect((col - self.DISPLAY_OFFSET) * Sprite.GROUND_TILE_SIZE - xOff, (row - self.DISPLAY_OFFSET) * Sprite.GROUND_TILE_SIZE - yOff, Sprite.GROUND_TILE_SIZE, Sprite.GROUND_TILE_SIZE))
                elif view[row][col] > self.GRASS_THRESHOLD:
                    pygame.draw.rect(screen, "lightgreen", pygame.Rect((col - self.DISPLAY_OFFSET) * Sprite.GROUND_TILE_SIZE - xOff, (row - self.DISPLAY_OFFSET) * Sprite.GROUND_TILE_SIZE - yOff, Sprite.GROUND_TILE_SIZE, Sprite.GROUND_TILE_SIZE))
                elif view[row][col] > self.SHALLOW_WATER_THRESHOLD:
                    pygame.draw.rect(screen, "yellow", pygame.Rect((col - self.DISPLAY_OFFSET) * Sprite.GROUND_TILE_SIZE - xOff, (row - self.DISPLAY_OFFSET) * Sprite.GROUND_TILE_SIZE - yOff, Sprite.GROUND_TILE_SIZE, Sprite.GROUND_TILE_SIZE))
                elif view[row][col] > self.DEEP_WATER_THRESHOLD:
                    pygame.draw.rect(screen, "blue", pygame.Rect((col - self.DISPLAY_OFFSET) * Sprite.GROUND_TILE_SIZE - xOff, (row - self.DISPLAY_OFFSET) * Sprite.GROUND_TILE_SIZE - yOff, Sprite.GROUND_TILE_SIZE, Sprite.GROUND_TILE_SIZE))
                else:
                    pygame.draw.rect(screen, "darkblue", pygame.Rect((col - self.DISPLAY_OFFSET) * Sprite.GROUND_TILE_SIZE - xOff, (row - self.DISPLAY_OFFSET) * Sprite.GROUND_TILE_SIZE - yOff, Sprite.GROUND_TILE_SIZE, Sprite.GROUND_TILE_SIZE))
