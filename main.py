import pygame
import random

# Variables
from Variables.settings import Settings
from Variables.colors import Colors

# Objects
from snake import Snake
from apple import Apple

pygame.init()
s = Settings()
c = Colors()

snake = Snake()
apple = Apple()

CLOCK = pygame.time.Clock()

def main():
    snake.spawn()
    apple.spawn()

    surface = pygame.display.set_mode((s.SCREEN_WIDTH, s.SCREEN_HEIGHT))

    pygame.display.set_caption(s.WINDOW_TITLE)

    surface.fill(c.BG_COLOR)

    snake.draw(surface, c.SNAKE_COLOR)
    apple.draw(surface, c.APPLE_COLOR)

    pygame.display.flip()

    while s.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                s.running = False

        snake.check_apple(apple, surface, c.SNAKE_COLOR)

        snake.sync_body(surface)
            
        snake.move(surface)

        surface.fill(c.BG_COLOR)

        snake.draw(surface, c.SNAKE_COLOR)
        apple.draw(surface, c.APPLE_COLOR)

        for i in range(0, len(snake.body)):
            snake.body[i].draw(surface, c.SNAKE_COLOR)

        pygame.display.flip()
        CLOCK.tick(s.FPS)

main()