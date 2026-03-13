import random
import pygame
from Settings import WIDTH, GROUND_Y


class Obstacle(pygame.sprite.Sprite):
    _image: pygame.Surface
    _rect: pygame.Rect
    _speed: float
    def __init__(self, speed: float) -> None:
        super().__init__()
        size: int = random.randint(35, 55)
        self._image: pygame.Surface = pygame.Surface((size, size))
        self._image.fill((200, 60, 60))
        self._rect: pygame.Rect = self._image.get_rect()
        self._rect.x = WIDTH
        self._rect.bottom = GROUND_Y

        self._speed: float = speed

    def update(self) -> None:
        self._rect.x -= int(self._speed)

        if self._rect.right < 0:
            self.kill()
