import pygame
from Settings import (WIDTH, HEIGHT)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
class Game:



    def run(self):
        run: bool = True



        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Dino Runner Pro Max")