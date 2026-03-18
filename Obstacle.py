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
        self.image: pygame.Surface = pygame.Surface((size, size))
        self.image.fill((200, 60, 60))
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.bottom = GROUND_Y

        self.speed: float = speed

    def update(self) -> None:
        self.rect.x -= int(self.speed)

        if self.rect.right < 0:
            self.kill()
