import pygame
import constants


def button(options):
    smallfont = pygame.font.SysFont('Corbel',35)
    text = smallfont.render(options , True , constants.BLACK)
    return text

def main():
    pygame.init()
    size=[constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("The Worst Game!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                