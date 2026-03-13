import pygame
import sys
from Player import Player
from Settings import WIDTH, HEIGHT, FPS


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Dino Runner Pro Max")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock: pygame.time.Clock = pygame.time.Clock()

        self.font: pygame.font.Font = pygame.font.SysFont("Comic Sans MS", 28)
        self.font: pygame.font.Font = pygame.font.SysFont("Comic Sans MS", 60)

        self.running: bool = True
        self.state: str = "START"
        self.player: Player = Player()

        def event(self) -> None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if self.state in ("START", "GAMEOVER"):
                        self.new_game()
                    elif self.state == "PLAYING" and event.key == pygame.K_SPACE:
                        self.player.jump()
