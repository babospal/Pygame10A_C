import random
import pygame
from Settings import WIDTH


class Coin(pygame.sprite.Sprite):
    def __init__(self, speed: float) -> None:
        super().__init__()
        self.image: pygame.Surface = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, (255, 220, 0), (0, 0, 20, 20))
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(240, 320)

        self.speed: float = speed

    def update(self) -> None:
        self.rect.x -= int(self.speed)

        if self.rect.right < 0:
            self.kill()
