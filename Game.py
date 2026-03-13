import pygame
import sys
import random
from Player import Player
from Obstacle import Obstacle
from Coin import Coin
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

        self.score: int = 0
        self.coin_score: int = 0
        self.speed: float = 6.0
        self.obstacle_timer: int = 0
        self.coin_timer: int = 0

        self.all_sprites: pygame.sprite.Group[pygame.sprite.Sprite] = (
            pygame.sprite.Group()
        )
        self.obstacles: pygame.sprite.Group[Obstacle] = pygame.sprite.Group()
        self.coins: pygame.sprite.Group[Coin] = pygame.sprite.Group()

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

        def update(self) -> None:
            if self.state != "PLAYING":
                return

            self.speed = 6.0 + (self.score // 500)
            self.score += 1

            self.obstacle_timer += 1
            if self.obstacle_timer > random.randint(70, 120):
                obs: Obstacle = Obstacle(self.speed)
                self.obstacles.add(obs)
                self.all_sprites.add(obs)
                self.obstacle_timer = 0

            self.coin_timer += 1
            if self.coin_timer > random.randint(120, 200):
                coin: Coin = Coin(self.speed)
                self.coins.add(coin)
                self.all_sprites.add(coin)
                self.coin_timer = 0

            self.all_sprites.update()

            if pygame.sprite.spritecollide(self.player, self.obstacles, False):
                self.state = "GAMEOVER"

            if pygame.sprite.spritecollide(self.player, self.coins, True):
                self.coin_score += 1
