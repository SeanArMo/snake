import pygame
import random
from Variables.settings import Settings

s = Settings()

class Apple:
    def __init__(self):
        self.apple_x = None
        self.apple_y = None

    def spawn(self):
        self.apple_x = random.randrange(0, s.SCREEN_WIDTH, s.SCREEN_WIDTH * s.BLOCK_SIZE)
        self.apple_y = random.randrange(0, s.SCREEN_HEIGHT, s.SCREEN_HEIGHT * s.BLOCK_SIZE)

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, pygame.Rect(self.apple_x, self.apple_y, s.SCREEN_WIDTH*s.BLOCK_SIZE, s.SCREEN_HEIGHT*s.BLOCK_SIZE))