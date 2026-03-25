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
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Dino Runner Pro Max")
        self._screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self._clock: pygame.time.Clock = pygame.time.Clock()

        self._font: pygame.font.Font = pygame.font.SysFont("Comic Sans MS", 28)
        self._big_font: pygame.font.Font = pygame.font.SysFont("Comic Sans MS", 60)

        self._running: bool = True
        self._state: str = "START"

        self._score: int = 0
        self._coin_score: int = 0
        self._speed: float = 6.0
        self._obstacle_timer: int = 0
        self._coin_timer: int = 0

        self._all_sprites: pygame.sprite.Group[pygame.sprite.Sprite] = (
            pygame.sprite.Group()
        )
        self._obstacles: pygame.sprite.Group[Obstacle] = pygame.sprite.Group()
        self._coins: pygame.sprite.Group[Coin] = pygame.sprite.Group()

        self._player: Player = Player()
        self._background: Background = Background()

        pygame.mixer.init()
        self._coin_sound = pygame.mixer.Sound('sounds/coin_sound.wav')
        self._game_over_sound = pygame.mixer.Sound('sounds/game_over_sound.wav')

        with open("highscore.txt", "r", encoding="utf-8") as file:
            for hs in file.read().splitlines():
                self.highscore : int = int(hs)

    def draw_text(
        self, text: str, font: pygame.font.Font, color: tuple[int, int, int], x: int, y: int
    ) -> None:
        img: pygame.Surface = font.render(text, True, color)
        self._screen.blit(img, (x, y))

    def new_game(self) -> None:
        self._score = 0
        self._coin_score = 0
        self._speed = 6.0
        self._obstacle_timer = 0
        self._coin_timer = 0

        self._all_sprites.empty()
        self._obstacles.empty()
        self._coins.empty()

        self._player = Player()
        self._background = Background()

        self._all_sprites.add(self._player)
        self._state = "PLAYING"

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if self._state in ("START", "GAMEOVER"):
                    self.new_game()
                elif self._state == "PLAYING" and event.key == pygame.K_SPACE:
                    self._player.jump()

    def update(self) -> None:
        if self._state != "PLAYING":
            return

        self._speed = 6.0 + (self._score // 500)
        self._background.update(self._speed)
        self._score += 1

        # Obstacle spawn
        self._obstacle_timer += 1
        if self._obstacle_timer > random.randint(70, 120):
            obs: Obstacle = Obstacle(self._speed)
            self._obstacles.add(obs)
            self._all_sprites.add(obs)
            self._obstacle_timer = 0

        # Coin spawn
        self._coin_timer += 1
        if self._coin_timer > random.randint(120, 200):
            coin: Coin = Coin(self._speed)
            self._coins.add(coin)
            self._all_sprites.add(coin)
            self._coin_timer = 0

        self._all_sprites.update()

        # Obstacle collision
        if pygame.sprite.spritecollide(self._player, self._obstacles, False):
            self._state = "GAMEOVER"
            self._game_over_sound.play()
            if self._score > self.highscore:
                self.highscore = self._score
                with open("highscore.txt", "w", encoding="utf-8") as file:
                    file.writelines(str(self.highscore))

        # Coin pickup
        if pygame.sprite.spritecollide(self._player, self._coins, True):
            self._coin_score += 1
            self._coin_sound.play()

    def draw(self) -> None:
        self._screen.fill((20, 20, 30))

        if self._state == "START":
            self.draw_text("Dino Runner Pro Max", self._big_font, (255, 255, 255), 165, 150)
            self.draw_text(
                "Press any key to start!", self._font, (200, 200, 200), 300, 250
            )

        elif self._state == "GAMEOVER":
            self.draw_text("GAME OVER :(", self._big_font, (255, 80, 80), 250, 140)
            self.draw_text(f"Score: {self._score}", self._font, (255, 255, 255), 370, 230)
            self.draw_text(f"Highscore: {self.highscore}", self._font, (255, 255, 255), 340, 263)
            self.draw_text(
                "Press any key to restart", self._font, (200, 200, 200), 290, 305
            )

        elif self._state == "PLAYING":
            self._background.draw(self._screen)
            self._all_sprites.draw(self._screen)

            self.draw_text(f"Score: {self._score}", self._font, (255, 255, 255), 20, 20)
            self.draw_text(
                f"Coins: {self._coin_score}", self._font, (255, 255, 0), 20, 50
            )

        pygame.display.update()

    def run(self) -> None:
        while self._running:
            self._clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
