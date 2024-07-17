import pygame
import constants
from SpriteCode import Sprite2

SLIMEW=(88,154,25,18)
SLIMEO=(146,154,25,18)
SLIMEB=(204,154,25,18)
SLIMEY=(60,211,25,18)
SLIMEC=(117,211,25,18)
SLIMEG=(174,211,25,18)
SLIMER=(232,211,25,18)

class Platform(pygame.sprite.Sprite):
    def __init__(self, sprite_):
        pygame.sprite.Sprite.__init__(self)
        sprite = Sprite2("Slime_enemy.png")
        self.image = sprite.get_image(sprite_[0],
                                            sprite_[1],
                                            sprite_[2],
                                            sprite_[3])

        self.rect = self.image.get_rect()

class Platf0rm(pygame.sprite.Sprite):
    def __init__(self, sprite_):
        pygame.sprite.Sprite.__init__(self)
        sprite = Sprite2("Slime_enemy.png")
        self.image = sprite.get_image(sprite_[0],
                                            sprite_[1],
                                            sprite_[2],
                                            sprite_[3])

        self.rect = self.image.get_rect()

class MovingPlatform(Platform):
    change_x = 0
    change_y = 0
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
    player = None
    level = None
    def update(self):
        self.rect.x += self.change_x
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right
        self.rect.y += self.change_y
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
