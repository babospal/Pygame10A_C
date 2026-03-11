import pygame
from Settings import GROUND_Y


class Player:
    _rect: pygame.Rect
    _vel_y: float
    _gravity: float
    _jump_power: float
    _jump_count: int
    _max_jumps: int
    _color: tuple[int, int, int]

    def __init__(self):
        self._rect = pygame.Rect(120, GROUND_Y - 50, 50, 50)
        self._vel_y = 0
        self._gravity = 0.8
        self._jump_power = -14
        self._jump_count = 0
        self._max_jumps = 2

        self.color = (50, 200, 80)

    def jump(self):
        if self._jump_count < self._max_jumps:
            self._vel_y = self._jump_power
            self._jump_count += 1

    def update(self):

        self._vel_y += self._gravity
        self._rect.y += self._vel_y

        if self._rect.bottom >= GROUND_Y:
            self._rect.bottom = GROUND_Y
            self._vel_y = 0
            self._jump_count = 0

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self._color, self._rect)
