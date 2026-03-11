import pygame
import random
from Settings import WIDTH, GROUND_Y

class Obstacle:

    def __init__(self,speed: int):

        size = random.randint(35,55)
        self.rect = pygame.Rect(WIDTH,GROUND_Y-size,size,size)

        self.speed = speed
        self.color = (200,60,60)

    def update(self):

        self.rect.x -= self.speed

    def draw(self,screen: pygame.Surface):

        pygame.draw.rect(screen,self.color,self.rect)