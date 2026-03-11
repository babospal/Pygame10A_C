import random
import pygame
from Settings import (WIDTH)
class Coin:

    def __init__(self,speed):

        y = random.randint(240,320)
        self.rect = pygame.Rect(WIDTH,y,20,20)

        self.speed = speed
        self.color = (255,220,0)

    def update(self):

        self.rect.x -= self.speed

    def draw(self,screen):

        pygame.draw.ellipse(screen,self.color,self.rect)
