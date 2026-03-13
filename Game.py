import pygame
from Player import Player
from Settings import WIDTH, HEIGHT, FPS


class Game:
    player = Player()
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Dino Runner Pro Max")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def run(self):
        run: bool = True
        clock: pygame.time.Clock = pygame.time.Clock()

        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.display.flip()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
