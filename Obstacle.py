import random
import pygame
from Settings import WIDTH, GROUND_Y


class Obstacle:
    _size: int
    _rect: pygame.Rect
    _speed: int
    _color: tuple[int, int, int]

    def __init__(self, speed: int):

        size = random.randint(35, 55)
        self._rect = pygame.Rect(WIDTH, GROUND_Y - size, size, size)

        self._speed = speed
        self._color = (200, 60, 60)

    def update(self):

        self._rect.x -= self._speed

    def draw(self, screen: pygame.Surface):

        pygame.draw.rect(screen, self._color, self._rect)
