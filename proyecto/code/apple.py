import pygame

from settings import *
from random import choice
from math import sin


class Apple:
    def __init__(self, snake):
        self.pos = pygame.Vector2()
        self.display_surface = pygame.display.get_surface()
        self.snake = snake
        self.set_pos()

        self.surf = pygame.image.load(join('..', 'graphics', 'watermelon.png')).convert_alpha()

    def set_pos(self):
        available_pos = [pygame.Vector2(x, y) for x in range(COLS) for y in range(ROWS) if
                         pygame.Vector2(x, y) not in self.snake.body]
        self.pos = choice(available_pos)

    def draw(self):
        self.scaled_surf = pygame.transform.smoothscale_by(self.surf, 2)
        self.scaled_rect = self.scaled_surf.get_rect(
            center=(self.pos.x * CELL_SIZE + CELL_SIZE / 2, self.pos.y * CELL_SIZE + CELL_SIZE / 2))
        self.display_surface.blit(self.scaled_surf, self.scaled_rect)
