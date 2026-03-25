import pygame
from Settings import GROUND_Y


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        # load images
        self.frog = pygame.transform.scale(
            pygame.image.load("images/frog.png").convert_alpha(), (100, 100)
        )
        self.frog_jumping = pygame.transform.scale(
            pygame.image.load("images/frog_jumping.png").convert_alpha(),
            (100, 100),
        )

        # set default image
        self.image: pygame.Surface = self.frog
        self.rect: pygame.Rect = self.image.get_rect()

        self.rect.x = 120
        self.rect.bottom = GROUND_Y

        self.rect.inflate_ip(-40, -40)

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
        self.rect.y += int(self._vel_y)

        # ground check
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self._vel_y = 0.0
            self._jump_count = 0

        # image switching
        if self.rect.bottom < GROUND_Y:
            self.image = self.frog_jumping
        else:
            self.image = self.frog
