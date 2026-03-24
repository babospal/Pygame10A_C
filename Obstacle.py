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

        # Load images
        big_img = pygame.image.load("images/tree_trunk_big.png").convert_alpha()
        small_img = pygame.image.load("images/tree_trunk_small.png").convert_alpha()

        # Choose type
        if random.randint(0, 1) == 0:
            # BIG obstacle
            target_height = 120
            scale = target_height / big_img.get_height()
            new_width = int(big_img.get_width() * scale)
            self.image = pygame.transform.scale(big_img, (new_width, target_height))

        else:
            # SMALL obstacle
            target_height = 70
            scale = target_height / small_img.get_height()
            new_width = int(small_img.get_width() * scale)
            self.image = pygame.transform.scale(small_img, (new_width, target_height))

        # Set rect based on the final image
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.bottom = GROUND_Y  # Align bottom to the ground

    def update(self) -> None:
        self.rect.x -= int(self.speed)

        if self.rect.right < 0:
            self.kill()
