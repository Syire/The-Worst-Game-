import pygame
import random
import constants
import Platforms
import Platforms2
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("Bird.png").convert()
        self.image.set_colorkey(constants.WHITE)
        self.rect = self.image.get_rect(
            center=(
                random.randint(constants.SCREEN_HEIGHT+100, constants.SCREEN_HEIGHT + 300),
                random.randint(0,constants.SCREEN_WIDTH),
            )
        )
        self.speed = random.randint(7, 10)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.top < 0:
            self.kill()

