import random
import pygame
from Settings import WIDTH


class Coin(pygame.sprite.Sprite):
    _image: pygame.Surface
    _rect: pygame.Rect
    _speed: float
    def __init__(self, speed: float) -> None:
        super().__init__()
        self._image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.ellipse(self._image, (255, 220, 0), (0, 0, 20, 20))
        self._rect = self._image.get_rect()
        self._rect.x = WIDTH
        self._rect.y = random.randint(240, 320)

        self._speed = speed

    def update(self) -> None:
        self._rect.x -= int(self._speed)

        if self._rect.right < 0:
            self.kill()
