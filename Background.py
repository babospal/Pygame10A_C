import pygame
from Settings import HEIGHT, WIDTH


class Background:
    _image: pygame.Surface
    _x1: float
    _x2: float
    _speed: float

    def __init__(self) -> None:
        # load background image
        self._image: pygame.Surface = pygame.image.load("background.png").convert()
        self._image = pygame.transform.scale(self._image, (WIDTH, HEIGHT))

        # scrolling positions
        self._x1: float = 0.0
        self._x2: float = float(WIDTH)

        self._speed: float = 2.0

    def update(self, speed_modifier: float) -> None:
        self._speed = speed_modifier * 0.3

        self._x1 -= self._speed
        self._x2 -= self._speed

        if self._x1 <= -WIDTH:
            self._x1 = self._x2 + WIDTH

        if self._x2 <= -WIDTH:
            self._x2 = self._x1 + WIDTH

    def draw(self, screen: pygame.Surface) -> None:
        # draw the two background copies
        screen.blit(self._image, (int(self._x1), 0))
        screen.blit(self._image, (int(self._x2), 0))
