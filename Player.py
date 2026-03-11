import pygame
from Settings import GROUND_Y

class Player:

    def __init__(self):
        self.rect = pygame.Rect(120, GROUND_Y - 50, 50, 50)
        self.vel_y = 0
        self.gravity = 0.8
        self.jump_power = -14
        self.jump_count = 0
        self.max_jumps = 2

        self.color = (50,200,80)

    def jump(self):
        if self.jump_count < self.max_jumps:
            self.vel_y = self.jump_power
            self.jump_count += 1

    def update(self):

        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0
            self.jump_count = 0

    def draw(self,screen: pygame.Surface):
        pygame.draw.rect(screen,self.color,self.rect)