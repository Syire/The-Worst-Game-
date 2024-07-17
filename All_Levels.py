import pygame
import Platforms
import constants
import Platforms2

class Level(object):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.background = None
        self.world_shift = 0
        self.level_limit = -1000

    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
    
    def draw(self, screen):
        screen.fill(constants.BLACK)
        screen.blit(self.background,(self.world_shift // 10000,0))
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
 
    def shift_world(self, shift_x):
        self.world_shift += shift_x
        for platform in self.platform_list:
            platform.rect.x += shift_x
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
 
class Level_01(Level):

    def __init__(self, player):
        music()
        Level.__init__(self, player)
        self.level_limit = -6550
        self.background = pygame.image.load("Jungle.png").convert()   
        self.background.set_colorkey(constants.BLACK)
        level = [
                 [Platforms.PLATFORM_PRIN, 200, 600],
                 [Platforms.PLATFORM_PRIN, 450, 500],
                 [Platforms.PLATFORM_PRIN, 1250, 450],
                 [Platforms.PLATFORM_PRIN, 1500, 380],
                 [Platforms.PLATFORM_PRIN, 850, 490],
                 [Platforms.PLATFORM_PRIN, 2250, 520],
                 [Platforms.SQUARE_PLATFORM,2700,  480],
                 [Platforms.SQUARE_PLATFORM,3200,425],
                 [Platforms.PLATFORM_0, 2920,385],
                 [Platforms.PLATFORM_PRIN, 3990,330],
                 [Platforms.PLATFORM_PRIN,4350,360],
                 [Platforms.PLATFORM_PRIN, 4835,335],
                 [Platforms.PLATFORM_PRIN, 5220,360],
                 [Platforms.SQUARE_PLATFORM, 5700,370],
                 [Platforms.PLATFORM_PRIN, 6040,460],
                 [Platforms.PLATFORM_PRIN, 6480,540],
                 [Platforms.PLATFORM_PRIN, 6865, 490],
                 [Platforms.PLATFORM_PRIN,7460,670],
                 ]
        for platform in level:
            block = Platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_M)
        block.rect.x = 1750
        block.rect.y = 280
        block.boundary_left = 1750
        block.boundary_right = 2100
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_M)
        block.rect.x = 3480
        block.rect.y = 400
        block.boundary_left = 3480
        block.boundary_right = 3925
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEB)
        enemy.rect.x = 450
        enemy.rect.y = 490
        enemy.boundary_left = 450
        enemy.boundary_right = 600
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEW)
        enemy.rect.x = 850
        enemy.rect.y = 480
        enemy.boundary_left = 850
        enemy.boundary_right = 1000
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEY)
        enemy.rect.x =1250
        enemy.rect.y = 440
        enemy.boundary_left = 1250
        enemy.boundary_right = 1400
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEG)
        enemy.rect.x =1500
        enemy.rect.y = 370
        enemy.boundary_left = 1500
        enemy.boundary_right = 1650
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEC)
        enemy.rect.x =2250
        enemy.rect.y = 510
        enemy.boundary_left = 2250
        enemy.boundary_right = 2400
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEO)
        enemy.rect.x =3990
        enemy.rect.y = 320
        enemy.boundary_left = 3990
        enemy.boundary_right = 4140
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEO)
        enemy.rect.x =4350
        enemy.rect.y = 350
        enemy.boundary_left = 4350
        enemy.boundary_right = 4500
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEB)
        enemy.rect.x =4835
        enemy.rect.y = 325
        enemy.boundary_left = 4835
        enemy.boundary_right = 4985
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMER)
        enemy.rect.x =5220
        enemy.rect.y = 350
        enemy.boundary_left = 5220
        enemy.boundary_right = 5370
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEY)
        enemy.rect.x =6040
        enemy.rect.y = 450
        enemy.boundary_left = 6040
        enemy.boundary_right = 6190
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEW)
        enemy.rect.x =6480
        enemy.rect.y = 530
        enemy.boundary_left = 6480
        enemy.boundary_right = 6630
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEB)
        enemy.rect.x =6865
        enemy.rect.y = 480
        enemy.boundary_left = 6865
        enemy.boundary_right = 7015
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 

class Level_02(Level):
    def __init__(self, player):
        music()
        Level.__init__(self, player)
        self.level_limit = -6480
        self.background = pygame.image.load("Jungle.png").convert()   
        self.background.set_colorkey(constants.BLACK)
        level = [[Platforms.SQUARE_PLATFORM, 200, 550],
                 [Platforms.SQUARE_PLATFORM, 500, 410],
                 [Platforms.SQUARE_PLATFORM, 850, 500],
                 [Platforms.SQUARE_PLATFORM, 1120,460],
                 [Platforms.SQUARE_PLATFORM, 1780,370],
                 [Platforms.SQUARE_PLATFORM, 2110,510],
                 [Platforms.SQUARE_PLATFORM, 2470,430],
                 [Platforms.SQUARE_PLATFORM, 2820,540],
                 [Platforms.SQUARE_PLATFORM, 3720,460],
                 [Platforms.PLATFORM_PRIN, 5280,595],
                 [Platforms.PLATFORM_M, 5620, 530],
                 [Platforms.PLATFORM_PRIN, 5950, 485],
                 [Platforms.PLATFORM_PRIN, 6340, 610],
                 [Platforms.SQUARE_PLATFORM, 6710, 575],
                 [Platforms.PLATFORM_M, 6960, 540],
                 [Platforms.PLATFORM_PRIN, 7220, 510],
                 [Platforms.PLATFORM_PRIN, 7380, 510],
                 ]
        for platform in level:
            block = Platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_M)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_M)
        block.rect.x = 3010
        block.rect.y = 410
        block.boundary_left = 3010
        block.boundary_right = 3420
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_M)
        block.rect.x = 4010
        block.rect.y = 530
        block.boundary_left = 4010
        block.boundary_right = 5130
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEY)
        enemy.rect.x =5950
        enemy.rect.y = 475
        enemy.boundary_left = 5950
        enemy.boundary_right = 6100
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMER)
        enemy.rect.x =6340
        enemy.rect.y = 600
        enemy.boundary_left = 6340
        enemy.boundary_right = 6490
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEC)
        enemy.rect.x =7220
        enemy.rect.y = 500
        enemy.boundary_left = 7220
        enemy.boundary_right = 7530
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEO)
        enemy.rect.x =5280
        enemy.rect.y = 585
        enemy.boundary_left = 5280
        enemy.boundary_right = 5430
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 

class Level_03(Level):
    def __init__(self, player):
        music()
        Level.__init__(self, player)
        self.level_limit = -6480
        self.background = pygame.image.load("Jungle.png").convert()   
        self.background.set_colorkey(constants.BLACK)
        level = [[Platforms.SQUARE_PLATFORM, 200, 200],
                 [Platforms.PLATFORM_PRIN, 520, 340],
                 [Platforms.PLATFORM_PRIN, 680, 340],
                 [Platforms.SQUARE_PLATFORM, 910, 290],
                 [Platforms.SQUARE_PLATFORM, 1240, 350],
                 [Platforms.SQUARE_PLATFORM, 1570, 465],
                 [Platforms.SQUARE_PLATFORM, 1950, 610],
                 [Platforms.SQUARE_PLATFORM, 2720, 505],
                 [Platforms.SQUARE_PLATFORM, 2930, 620],
                 [Platforms.PLATFORM_M, 4490, 670],
                 [Platforms.PLATFORM_PRIN,4700, 580],
                 [Platforms.SQUARE_PLATFORM,5065,590],
                 [Platforms.PLATFORM_PRIN, 5315,625],
                 [Platforms.PLATFORM_PRIN, 6510,610],
                 [Platforms.PLATFORM_M, 6780, 570],
                 [Platforms.PLATFORM_M, 6910, 520],
                 [Platforms.PLATFORM_M, 7090, 485],
                 [Platforms.PLATFORM_PRIN, 7280,380],
                 [Platforms.PLATFORM_PRIN,7440,380],
                 ]
        for platform in level:
            block = Platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.SQUARE_PLATFORM)
        block.rect.x = 2120
        block.rect.y = 610
        block.boundary_left = 2120
        block.boundary_right = 2510
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_PRIN)
        block.rect.x = 3320
        block.rect.y = 530
        block.boundary_left = 3240
        block.boundary_right = 3920
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.SQUARE_PLATFORM)
        block.rect.x = 4210
        block.rect.y = 420
        block.boundary_top = 120
        block.boundary_bottom = 850
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_PRIN)
        block.rect.x = 5510
        block.rect.y = 540
        block.boundary_left = 5510
        block.boundary_right = 6320
        block.change_x = 4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEB)
        enemy.rect.x =520
        enemy.rect.y = 330
        enemy.boundary_left = 520
        enemy.boundary_right = 840
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEG)
        enemy.rect.x =4700
        enemy.rect.y = 570
        enemy.boundary_left = 4700
        enemy.boundary_right = 4860
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEO)
        enemy.rect.x =5315
        enemy.rect.y = 615
        enemy.boundary_left =5315
        enemy.boundary_right = 5475
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEB)
        enemy.rect.x = 6510
        enemy.rect.y = 600
        enemy.boundary_left = 6510
        enemy.boundary_right = 6670
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEY)
        enemy.rect.x = 7280
        enemy.rect.y = 370
        enemy.boundary_left = 7280
        enemy.boundary_right = 7600
        enemy.change_x = 4
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy) 

class Level_04(Level):
    def __init__(self, player):
        music()
        Level.__init__(self, player)
        self.level_limit = -6480
        self.background = pygame.image.load("Jungle.png").convert()   
        self.background.set_colorkey(constants.BLACK)
        level = [[Platforms.SQUARE_PLATFORM, 200, 400],
                 [Platforms.SQUARE_PLATFORM,2140, 330],
                 [Platforms.PLATFORM_M, 2410, 400],
                 [Platforms.SQUARE_PLATFORM, 2720, 505],
                 [Platforms.SQUARE_PLATFORM, 2930, 620],
                 [Platforms.PLATFORM_M, 4010,580],
                 [Platforms.PLATFORM_PRIN, 4200,640],
                 [Platforms.PLATFORM_PRIN, 5310,425],
                 [Platforms.PLATFORM_PRIN, 5590,580],
                 [Platforms.PLATFORM_M, 5860, 490],
                 [Platforms.PLATFORM_M, 6020, 560],
                 [Platforms.SQUARE_PLATFORM, 6280, 485],
                 [Platforms.SQUARE_PLATFORM, 7010,510],
                 [Platforms.PLATFORM_PRIN, 7280,580],
                 [Platforms.PLATFORM_PRIN,7440,580],
                 ]
        for platform in level:
            block = Platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_PRIN)
        block.rect.x = 400
        block.rect.y = 510
        block.boundary_left = 380
        block.boundary_right = 1120
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.SQUARE_PLATFORM)
        block.rect.x = 1510
        block.rect.y = 420
        block.boundary_top = 95
        block.boundary_bottom = 690
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_PRIN)
        block.rect.x = 1620
        block.rect.y = 225
        block.boundary_left = 1594
        block.boundary_right = 2020
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_PRIN)
        block.rect.x = 3120
        block.rect.y = 540
        block.boundary_left = 3080
        block.boundary_right = 3820
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.SQUARE_PLATFORM)
        block.rect.x = 4470
        block.rect.y = 410
        block.boundary_top = 230
        block.boundary_bottom = 580
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_PRIN)
        block.rect.x = 4610
        block.rect.y = 310
        block.boundary_left = 4590
        block.boundary_right = 5190
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_PRIN)
        block.rect.x = 6420
        block.rect.y = 430
        block.boundary_left = 6350
        block.boundary_right = 6860
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMER)
        enemy.rect.x =4200
        enemy.rect.y = 630
        enemy.boundary_left = 4200
        enemy.boundary_right = 4360
        enemy.change_x = 3
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEC)
        enemy.rect.x =5310
        enemy.rect.y = 415
        enemy.boundary_left = 5310
        enemy.boundary_right = 5470
        enemy.change_x = 3
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEW)
        enemy.rect.x =5590
        enemy.rect.y = 570
        enemy.boundary_left = 5590
        enemy.boundary_right = 5750
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEY)
        enemy.rect.x =7280
        enemy.rect.y = 570
        enemy.boundary_left = 7280
        enemy.boundary_right = 7600
        enemy.change_x = 3
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)

class Level_05(Level):
    def __init__(self, player):
        music()
        Level.__init__(self, player)
        self.level_limit = -6480
        self.background = pygame.image.load("Jungle.png").convert()   
        self.background.set_colorkey(constants.BLACK)
        level = [[Platforms.SQUARE_PLATFORM, 200, 500],
                 [Platforms.PLATFORM_PRIN,3640,480],
                 [Platforms.PLATFORM_PRIN,4990,80],
                 [Platforms.PLATFORM_PRIN, 7280,120],
                 [Platforms.PLATFORM_PRIN,7440,120],
                 ]
        for platform in level:
            block = Platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.SQUARE_PLATFORM)
        block.rect.x = 380
        block.rect.y = 610
        block.boundary_left = 370
        block.boundary_right = 780
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_PRIN)
        block.rect.x = 960
        block.rect.y = 540
        block.boundary_left = 930
        block.boundary_right = 1480
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.SQUARE_PLATFORM)
        block.rect.x = 1710
        block.rect.y = 410
        block.boundary_top = 100
        block.boundary_bottom = 670
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_PRIN)
        block.rect.x = 1830
        block.rect.y = 240
        block.boundary_left = 1790
        block.boundary_right = 2470
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_M)
        block.rect.x = 2610
        block.rect.y = 450
        block.boundary_top = 200
        block.boundary_bottom = 610
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_0)
        block.rect.x = 2820
        block.rect.y = 370
        block.boundary_left = 2770
        block.boundary_right = 3450
        block.change_x = 4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_PRIN)
        block.rect.x = 3980
        block.rect.y = 510
        block.boundary_left = 3840
        block.boundary_right = 4600
        block.change_x = 4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.SQUARE_PLATFORM)
        block.rect.x = 4810
        block.rect.y = 300
        block.boundary_top = 80
        block.boundary_bottom = 740
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.SQUARE_PLATFORM)
        block.rect.x = 5240
        block.rect.y = 180
        block.boundary_left = 5150
        block.boundary_right = 5870
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_M)
        block.rect.x = 6120
        block.rect.y = 300
        block.boundary_top = 230
        block.boundary_bottom = 500
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.SQUARE_PLATFORM)
        block.rect.x = 6340
        block.rect.y = 420
        block.boundary_left = 6250
        block.boundary_right = 6890
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.PLATFORM_PRIN)
        block.rect.x = 7070
        block.rect.y = 300
        block.boundary_top = 0
        block.boundary_bottom = 600
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEY)
        enemy.rect.x =6040
        enemy.rect.y = 450
        enemy.boundary_left = 6040
        enemy.boundary_right = 6190
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEG)
        enemy.rect.x =3640
        enemy.rect.y = 470
        enemy.boundary_left = 3640
        enemy.boundary_right = 3800
        enemy.change_x = 3
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEW)
        enemy.rect.x =4990
        enemy.rect.y = 70
        enemy.boundary_left = 4990
        enemy.boundary_right = 5150
        enemy.change_x = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMEB)
        enemy.rect.x =7280
        enemy.rect.y = 110
        enemy.boundary_left = 7280
        enemy.boundary_right = 7600
        enemy.change_x = 4
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)

class Level_06(Level):
    def __init__(self, player):
        music()
        Level.__init__(self, player)
        self.level_limit = -6480
        self.background = pygame.image.load("Jungle.png").convert()   
        self.background.set_colorkey(constants.BLACK)
        level = [[Platforms.SQUARE_PLATFORM, 200,600],
                 [Platforms.SQUARE_PLATFORM, 510, 640],
                 [Platforms.SQUARE_PLATFORM, 780, 560],
                 [Platforms.SQUARE_PLATFORM, 1020, 430],
                 [Platforms.SQUARE_PLATFORM, 1290, 360],
                 [Platforms.SQUARE_PLATFORM, 1630, 475],
                 [Platforms.SQUARE_PLATFORM, 1910, 550],
                 [Platforms.SQUARE_PLATFORM, 2250, 610],
                 [Platforms.SQUARE_PLATFORM, 2630, 530],
                 [Platforms.SQUARE_PLATFORM, 2910, 445],
                 [Platforms.SQUARE_PLATFORM, 3310, 365],
                 [Platforms.SQUARE_PLATFORM, 3600, 300],
                 [Platforms.SQUARE_PLATFORM,3945,250],
                 [Platforms.SQUARE_PLATFORM, 4265,425],
                 [Platforms.SQUARE_PLATFORM, 4530,510],
                 [Platforms.SQUARE_PLATFORM, 4860, 420],
                 [Platforms.SQUARE_PLATFORM, 5120, 375],
                 [Platforms.SQUARE_PLATFORM, 5395, 430],
                 [Platforms.SQUARE_PLATFORM, 5605,460],
                 [Platforms.SQUARE_PLATFORM, 5910,380],
                 [Platforms.SQUARE_PLATFORM, 6930,450],
                 [Platforms.PLATFORM_PRIN, 7280,560],
                 [Platforms.PLATFORM_PRIN,7440,560],
                 ]
        for platform in level:
            block = Platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        block = Platforms.MovingPlatform(Platforms.SQUARE_PLATFORM)
        block.rect.x = 6210
        block.rect.y = 420
        block.boundary_left = 6150
        block.boundary_right = 6760
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        enemy = Platforms2.MovingPlatform(Platforms2.SLIMER)
        enemy.rect.x =7280
        enemy.rect.y = 550
        enemy.boundary_left = 7280
        enemy.boundary_right = 7600
        enemy.change_x = 4
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)

'''class Level_07(Level):
    def __init__(self, player):
        music()
        Level.__init__(self, player)
        self.level_limit = -6480
        self.background = pygame.image.load("fnaf.b.png").convert()   
        self.background.set_colorkey(constants.BLACK)
        level = [[Platforms2.MUSIC_BOX, 200, 550],
                 [Platforms2.PL, 500, 400],
                 [Platforms2.MUSIC_BOX, 820, 470],
                 [Platforms2.MUSIC_BOX, 1030, 560],
                 [Platforms2.PL, 1500, 320],
                 [Platforms2.MUSIC_BOX, 1720, 460],
                 [Platforms2.PL, 2420, 490],
                 [Platforms2.PL, 2710, 570],
                 [Platforms2.MUSIC_BOX, 2930, 620],
                 [Platforms2.PL, 3890, 470],
                 [Platforms2.MUSIC_BOX, 4270, 330],
                 [Platforms2.MUSIC_BOX, 4520, 270],
                 [Platforms2.PL, 4790, 360],
                 [Platforms2.MUSIC_BOX, 5035, 450],
                 [Platforms2.MUSIC_BOX, 6480, 485],
                 [Platforms2.MUSIC_BOX, 6710,520],
                 [Platforms2.MUSIC_BOX, 6995, 470],
                 [Platforms2.PL, 7280,560],
                 [Platforms2.PL,7440,560],
                 ]
        for platform in level:
            block = Platforms2.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        block = Platforms2.MovingPlatform(Platforms2.PL)
        block.rect.x = 1250
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 650
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms2.MovingPlatform(Platforms2.MUSIC_BOX)
        block.rect.x = 1970
        block.rect.y = 370
        block.boundary_left = 1875
        block.boundary_right = 2210
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms2.MovingPlatform(Platforms2.PL)
        block.rect.x = 3130
        block.rect.y = 560
        block.boundary_left = 3060
        block.boundary_right = 3640
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        block = Platforms2.MovingPlatform(Platforms2.PL)
        block.rect.x = 5230
        block.rect.y = 560
        block.boundary_left = 5175
        block.boundary_right = 6270
        block.change_x = 4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)'''

def music():
    pygame.mixer.init()
    pygame.mixer.music.load('Jungle_S.mp3')
    pygame.mixer.music.play(loops=-1)
    