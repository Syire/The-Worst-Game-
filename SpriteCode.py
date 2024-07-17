import pygame
import constants

class Sprite(object):
    sprite = None
    def __init__(self, file_name):
        self.sprite = pygame.image.load(file_name).convert()
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite, (0, 0), (x, y, width, height))
        image.set_colorkey(constants.BLACK)
        return image

class Sprite2(object):
    sprite = None
    def __init__(self, file_name):
        self.sprite = pygame.image.load(file_name).convert()
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite, (0, 0), (x, y, width, height))
        image.set_colorkey(constants.CYAN)
        return image

