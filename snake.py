import pygame
import random
import sys
from Variables.settings import Settings
from Variables.colors import Colors
from apple import Apple
from segment import Segment

s = Settings()
c = Colors()

class Snake:
    def __init__(self):
        self.head_x = None
        self.head_y = None
        self.body = []
        self.score = 0
        self.direction = None
        self.id = "01"

    def spawn(self):
        self.head_x = random.randrange(0, s.SCREEN_WIDTH, s.SCREEN_WIDTH * s.BLOCK_SIZE)
        self.head_y = random.randrange(0, s.SCREEN_HEIGHT, s.SCREEN_HEIGHT * s.BLOCK_SIZE)

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, pygame.Rect(self.head_x, self.head_y, s.SCREEN_WIDTH*s.BLOCK_SIZE, s.SCREEN_HEIGHT*s.BLOCK_SIZE))

    def check_apple(self, apple:Apple, surface, color):
        if self.head_x == apple.apple_x and self.head_y == apple.apple_y:
            apple.spawn()
            self.score += 1
            if len(self.body) == 0:
                for i in range(0, s.GROWTH_VALUE):
                    segment = Segment()
                    segment.link_to_previous(self)
                    segment.sync(self)
                    self.body.append(segment)
                    segment.draw(surface, color)
                    pygame.display.update()
                    self.move(surface)

            else:
                for i in range(0, s.GROWTH_VALUE):
                    segment = Segment()
                    segment.link_to_previous(self)
                    self.body.append(segment)
                    segment.sync(self)
                    segment.draw(surface, color)
                    pygame.display.update()

    def check_collide(self, surface):
        if self.head_x < 0 or self.head_x == s.SCREEN_WIDTH:
            self.death(surface)
        elif self.head_y < 0 or self.head_y == s.SCREEN_HEIGHT:
           self.death(surface)

        body_x = []
        body_y = []

        pairs = []

        head = [self.head_x, self.head_y]

        for i in range(0, len(self.body)):
            body_x.append(self.body[i].x)
            body_y.append(self.body[i].y)

        for i in range(0, len(self.body)):
            pair = [self.body[i].x, self.body[i].y]
            pairs.append(pair)

        if head in pairs:
            self.death(surface)

    def death(self, surface):
        # Text
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render(f"You died with {self.score} points.", True, c.RED, (c.BLACK))
        textRect = text.get_rect()
        textRect.center = (s.SCREEN_WIDTH // 2, s.SCREEN_HEIGHT // 2)
        surface.fill(c.BLACK)
        surface.blit(text, textRect)

        # Update screen
        pygame.display.update()

        end_run = True
        while end_run:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            except pygame.error:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    end_run = False
                pygame.quit()
                sys.exit()


    def move(self, surface):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.direction!= pygame.K_r:
            self.direction = pygame.K_w
            self.head_y -= s.VELOCITY
            self.check_collide(surface)
        elif keys[pygame.K_a] and self.direction != pygame.K_s:
            self.direction = pygame.K_a
            self.head_x -= s.VELOCITY
            self.check_collide(surface)
        elif keys[pygame.K_r] and self.direction != pygame.K_w:
            self.direction = pygame.K_r
            self.head_y += s.VELOCITY
            self.check_collide(surface)
        elif keys[pygame.K_s] and self.direction != pygame.K_a:
            self.direction = pygame.K_s
            self.head_x += s.VELOCITY
            self.check_collide(surface)
        else:
            if self.direction == pygame.K_w and self.direction != pygame.K_r:
                self.direction = pygame.K_w
                self.head_y -= s.VELOCITY
                self.check_collide(surface)
            elif self.direction == pygame.K_a and self.direction != pygame.K_s:
                self.direction = pygame.K_a
                self.head_x -= s.VELOCITY
                self.check_collide(surface)
            elif self.direction == pygame.K_r and self.direction != pygame.K_w:
                self.direction = pygame.K_r
                self.head_y += s.VELOCITY
                self.check_collide(surface)
            elif self.direction == pygame.K_s and self.direction != pygame.K_a:
                self.direction = pygame.K_s
                self.head_x += s.VELOCITY
                self.check_collide(surface)

    def sync_body(self, surface):
        if len(self.body) > 0:
            i = len(self.body) - 1
            while i >= 0:
                self.body[i].sync(self)
                i -= 1