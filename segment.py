import pygame
from Variables.settings import Settings
from Variables.colors import Colors

s = Settings()
c = Colors()

class Segment:
    def __init__(self):
        self.x = None
        self.y = None
        self.previous = None
        self.id = "00"

    def link_to_previous(self, snake):
        if len(snake.body) == 0:
            #self.x = snake.head_x
            #self.y = snake.head_y
            self.previous = snake
            self.id = "01"
        else:
            self.previous = snake.body[-1]
            #self.x = self.previous.x
            #self.y = self.previous.y

    def sync(self, snake):
        if self.id == "01":
            self.x = snake.head_x
            self.y = snake.head_y
        else:
            self.x = self.previous.x 
            self.y = self.previous.y

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, pygame.Rect(self.x, self.y, s.SCREEN_WIDTH*s.BLOCK_SIZE, s.SCREEN_HEIGHT*s.BLOCK_SIZE))