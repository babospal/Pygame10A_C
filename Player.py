import pygame
from Settings import GROUND_Y


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        # load images
        self.frog = pygame.transform.scale(
            pygame.image.load("frog.png").convert_alpha(), (100, 100)
        )
        self.frog_jumping = pygame.transform.scale(
            pygame.image.load("frog_jumping.png").convert_alpha(),
            (100, 100),
        )

        # set default image
        self.image: pygame.Surface = self.frog
        self.rect: pygame.Rect = self.image.get_rect()

        self.rect.x = 120
        self.rect.bottom = GROUND_Y

        self.vel_y: float = 0.0
        self.gravity: float = 0.8
        self.jump_power: float = -14.0
        self.jump_count: int = 0
        self.max_jumps: int = 2

    def jump(self) -> None:
        if self.jump_count < self.max_jumps:
            self.vel_y = self.jump_power
            self.jump_count += 1

    def update(self) -> None:
        self.vel_y += self.gravity
        self.rect.y += int(self.vel_y)

        # ground check
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0.0
            self.jump_count = 0

        # 👇 IMAGE SWITCHING LOGIC
        if self.rect.bottom < GROUND_Y:
            self.image = self.frog_jumping
        else:
            self.image = self.frog
