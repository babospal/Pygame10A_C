from __future__ import annotations
import sys
import random
import pygame
from Player import Player
from Background import Background
from Coin import Coin
from Obstacle import Obstacle
from Settings import HEIGHT, WIDTH, FPS


class Game:
    pygame.mixer.init()
    _coin_sound = pygame.mixer.Sound('sounds/coin_sound.wav')
    _game_over_sound = pygame.mixer.Sound('sounds/game_over_sound.wav')
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Dino Runner Pro Max")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock: pygame.time.Clock = pygame.time.Clock()

        self.font: pygame.font.Font = pygame.font.SysFont("Comic Sans MS", 28)
        self.big_font: pygame.font.Font = pygame.font.SysFont("Comic Sans MS", 60)

        self.running: bool = True
        self.state: str = "START"

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

        self.player: Player = Player()
        self.background: Background = Background()

    def draw_text(
        self, text: str, font: pygame.font.Font, color: tuple[int, int, int], x: int, y: int
    ) -> None:
        img: pygame.Surface = font.render(text, True, color)
        self.screen.blit(img, (x, y))

    def new_game(self) -> None:
        self.score = 0
        self.coin_score = 0
        self.speed = 6.0
        self.obstacle_timer = 0
        self.coin_timer = 0

        self.all_sprites.empty()
        self.obstacles.empty()
        self.coins.empty()

        self.player = Player()
        self.background = Background()

        self.all_sprites.add(self.player)
        self.state = "PLAYING"

    def events(self) -> None:
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
        self.background.update(self.speed)
        self.score += 1

        # Obstacle spawn
        self.obstacle_timer += 1
        if self.obstacle_timer > random.randint(70, 120):
            obs: Obstacle = Obstacle(self.speed)
            self.obstacles.add(obs)
            self.all_sprites.add(obs)
            self.obstacle_timer = 0

        # Coin spawn
        self.coin_timer += 1
        if self.coin_timer > random.randint(120, 200):
            coin: Coin = Coin(self.speed)
            self.coins.add(coin)
            self.all_sprites.add(coin)
            self.coin_timer = 0

        self.all_sprites.update()

        # Obstacle collision
        if pygame.sprite.spritecollide(self.player, self.obstacles, False):
            self.state = "GAMEOVER"
            self._game_over_sound.play()

        # Coin pickup
        if pygame.sprite.spritecollide(self.player, self.coins, True):
            self.coin_score += 1
            self._coin_sound.play()

    def draw(self) -> None:
        self.screen.fill((20, 20, 30))

        if self.state == "START":
            self.draw_text("Dino Runner Pro Max", self.big_font, (255, 255, 255), 165, 150)
            self.draw_text(
                "Press any key to start!", self.font, (200, 200, 200), 300, 250
            )

        elif self.state == "GAMEOVER":
            self.draw_text("GAME OVER :(", self.big_font, (255, 80, 80), 250, 140)
            self.draw_text(f"Score: {self.score}", self.font, (255, 255, 255), 370, 230)
            self.draw_text(
                "Press any key to restart", self.font, (200, 200, 200), 290, 280
            )

        elif self.state == "PLAYING":
            self.background.draw(self.screen)
            self.all_sprites.draw(self.screen)

            self.draw_text(f"Score: {self.score}", self.font, (255, 255, 255), 20, 20)
            self.draw_text(
                f"Coins: {self.coin_score}", self.font, (255, 255, 0), 20, 50
            )

        pygame.display.update()

    def run(self) -> None:
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
