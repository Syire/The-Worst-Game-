import pygame
from P_Player import Player
import P_Player
import All_Levels
import constants
from SpriteCode import Sprite
import SpriteCode
from life import life
from enemies import Enemy
import Platforms2

xRes=True
LOOP=0


def button(options):
    smallfont = pygame.font.SysFont('Corbel',70)
    text = smallfont.render(options , True , constants.BLACK)
    return text

def restart(screen):
    screen.blit(button('Press C to reset!'),(constants.SCREEN_WIDTH/3.75,constants.SCREEN_HEIGHT/2-150))
    pygame.display.update()
    Restart=False
    while not Restart:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    Restart=True
            if event.type == pygame.KEYUP:
                break
            if event.type==pygame.QUIT:
                pygame.quit()
    return Restart



def main():
    pygame.init()
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("The Worst Game!")
    pygame_icon = pygame.image.load('Icon.png')
    pygame.display.set_icon(pygame_icon)
    ADDENEMY = pygame.USEREVENT - 0
    pygame.time.set_timer(ADDENEMY, 900)
    player = Player()
    Life= life(screen)

    levels=[]
    levels.append(All_Levels.Level_01(player))
    levels.append(All_Levels.Level_02(player))
    #levels.append(All_Levels.Level_03(player))
    #levels.append(All_Levels.Level_04(player))
    #levels.append(All_Levels.Level_05(player))
    #levels.append(All_Levels.Level_06(player))

    current_levels = levels[constants.checkpoint]
    #slime_enemy=pygame.sprite.Group(current_levels.enemy_list)

    active_sprite_list = pygame.sprite.Group()
    player.level = current_levels
    enemies = pygame.sprite.Group()
    player.rect.x = 200
    player.rect.y = 100
    active_sprite_list.add(player)
    #active_sprite_list.add(slime_enemy)
    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                done = True 
            elif event.type == ADDENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                active_sprite_list.add(enemies)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_DOWN:
                    player.down()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
        if player.rect.y > 700:
            xRes=False
            break
        if pygame.sprite.spritecollideany(player, enemies):
            constants.cur_life+=-10
            for new_enemy in enemies:
                new_enemy.kill()
        if constants.cur_life<=0:
            xRes=False
            break
        active_sprite_list.update()
        enemies.update()
        #slime_enemy.update()
        current_levels.update()
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_levels.shift_world(-diff)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_levels.shift_world(diff)
        current_position = player.rect.x + current_levels.world_shift
        if current_position < current_levels.level_limit:
            player.rect.x = 120
            if constants.checkpoint < len(levels)-1:
                constants.checkpoint+=1
                current_levels= levels[constants.checkpoint]
                player.level = current_levels
                player.rect.x = 200
                player.rect.y = 100
                constants.cur_life=100
            else:
                constants.checkpoint=constants.first_level
                break
        current_levels.draw(screen)
        for entity in active_sprite_list:
            screen.blit(entity.image, entity.rect)
        Life.printLife(constants.cur_life,constants.max_life)
        clock.tick(60)
        pygame.display.flip()
    xRes=restart(screen)
    pygame.quit()
def start():
    main()
    while LOOP!=-1:
        if xRes==False:
            pygame.quit()
        else:
            constants.cur_life=100
            main()

