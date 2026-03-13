import pygame
from Settings import GROUND_Y


class Player(pygame.sprite.Sprite):
    _image: pygame.Surface
    _rect: pygame.Rect
    _vel_y: float
    _gravity: float
    _jump_power: float
    _jump_count: int
    _max_jumps: int
    def __init__(self) -> None:
        super().__init__()
        self._image: pygame.Surface = pygame.Surface((50, 50))
        self._image.fill((50, 200, 80))
        self._rect: pygame.Rect = self._image.get_rect()
        self._rect.x = 120
        self._rect.bottom = GROUND_Y

        self._vel_y: float = 0.0
        self._gravity: float = 0.8
        self._jump_power: float = -14.0
        self._jump_count: int = 0
        self._max_jumps: int = 2

    def jump(self) -> None:
        if self._jump_count < self._max_jumps:
            self._vel_y = self._jump_power
            self._jump_count += 1

    def update(self) -> None:
        self._vel_y += self._gravity
        self._rect.y += int(self._vel_y)

        if self._rect.bottom >= GROUND_Y:
            self._rect.bottom = GROUND_Y
            self._vel_y = 0.0
            self._jump_count = 0
