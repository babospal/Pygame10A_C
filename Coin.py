import random
import pygame
from Settings import WIDTH


class Coin:
    _y: int
    _rect: pygame.Rect
    _speed: int
    _color: tuple[int, int, int]

    def __init__(self, speed: int):

        y = random.randint(240, 320)
        self._rect = pygame.Rect(WIDTH, y, 20, 20)

        self._speed = speed
        self._color = (255, 220, 0)

    def update(self):

        self._rect.x -= self._speed

    def draw(self, screen: pygame.Surface):

        pygame.draw.ellipse(screen, self._color, self._rect)
