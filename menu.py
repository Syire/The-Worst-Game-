import pygame
import Arcade
import constants

def button(options):
    smallfont = pygame.font.SysFont('Corbel',35)
    text = smallfont.render(options , True , constants.BLACK)
    return text

def menu():
    pygame.init()
    size=[constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("The Worst Game!")
    screen.fill((constants.BLACK))
    background = pygame.image.load("Jungle.png").convert()   
    background.set_colorkey(constants.BLACK)
    screen.blit(background,(0,0))
    pygame_icon = pygame.image.load('Icon.png')
    pygame.display.set_icon(pygame_icon)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if constants.SCREEN_WIDTH/2.50 <=mouse[0] <= constants.SCREEN_WIDTH/2+40 and constants.SCREEN_HEIGHT/2+50 <= mouse[1] <= constants.SCREEN_HEIGHT/2+90:
                    pygame.quit()
                if constants.SCREEN_WIDTH/2.50 <= mouse[0] <= constants.SCREEN_WIDTH/2+40 and constants.SCREEN_HEIGHT/2 <= mouse[1] <= constants.SCREEN_HEIGHT/2+40:
                    Arcade.start()
        mouse = pygame.mouse.get_pos()
        if constants.SCREEN_WIDTH/2.50 <= mouse[0] <= constants.SCREEN_WIDTH/2+40 and constants.SCREEN_HEIGHT/2 <= mouse[1] <= constants.SCREEN_HEIGHT/2+40:
            pygame.draw.rect(screen,constants.AQUA,[constants.SCREEN_WIDTH/2.50,constants.SCREEN_HEIGHT/2,140,40])
        else:
            pygame.draw.rect(screen,constants.AN_GREEN,[constants.SCREEN_WIDTH/2.50,constants.SCREEN_HEIGHT/2,140,40])
        if constants.SCREEN_WIDTH/2.50 <=mouse[0] <= constants.SCREEN_WIDTH/2+40 and constants.SCREEN_HEIGHT/2+50 <= mouse[1] <= constants.SCREEN_HEIGHT/2+90:
            pygame.draw.rect(screen,constants.AQUA,[constants.SCREEN_WIDTH/2.50,constants.SCREEN_HEIGHT/2+50,140,40])
        else:
            pygame.draw.rect(screen,constants.AN_GREEN,[constants.SCREEN_WIDTH/2.50,constants.SCREEN_HEIGHT/2+50,140,40])
    
        screen.blit(button('The Worst Game!'),(constants.SCREEN_WIDTH/2.75,constants.SCREEN_HEIGHT/2-100))
        screen.blit(button('Play') , (constants.SCREEN_WIDTH/2.50,constants.SCREEN_HEIGHT/2))
        screen.blit(button('Quit'),(constants.SCREEN_WIDTH/2.50, constants.SCREEN_HEIGHT/2+50))
        pygame.display.update()

menu()