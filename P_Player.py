import pygame
import constants
import life
from Platforms import MovingPlatform
from SpriteCode import Sprite

class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    walking_l = []
    walking_r = []
    direction = "R"
    level=None
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = Sprite("player_2.png")

        image = sprite_sheet.get_image(170,26,30,58)
        self.walking_r.append(image)
        image = sprite_sheet.get_image(170,92,30,58)
        self.walking_r.append(image)
        image = sprite_sheet.get_image(170,154,30,58)
        self.walking_r.append(image)
        image = sprite_sheet.get_image(170,220,30,58)
        self.walking_r.append(image)

        image = sprite_sheet.get_image(236,26,30,58)
        self.walking_l.append(image)
        image = sprite_sheet.get_image(236,92,30,58)
        self.walking_l.append(image)
        image = sprite_sheet.get_image(236,154,30,58)
        self.walking_l.append(image)
        image = sprite_sheet.get_image(236,220,30,58)
        self.walking_l.append(image)

        self.image = self.walking_r[0]
        self.rect = self.image.get_rect()
        

    def update(self):
        self.gravity()
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_r)
            self.image = self.walking_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_l)
            self.image = self.walking_l[frame]
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
            if isinstance(block, MovingPlatform):
               self.rect.x += block.change_x

        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            self.change_y = 0
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
        enemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        for enemy in enemy_hit_list:
            if self.change_x > 0:
                self.rect.right = enemy.rect.left
                constants.cur_life+=-1
            elif self.change_x < 0:
                self.rect.left = enemy.rect.right
                constants.cur_life+=-1
        enemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        for enemy in enemy_hit_list:
            if self.change_y > 0:
                self.rect.bottom = enemy.rect.top
                #live=life.life()
                constants.cur_life+=-1
            self.change_y = 0


    def gravity(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        self.rect.y += 1
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    def go_left(self):
        self.change_x = -7
        self.direction = "L"

    def go_right(self):
        self.change_x = 7
        self.direction = "R"

    def stop(self):
        self.change_x = 0

    def down(self):
        self.change_y = 5
    


        


