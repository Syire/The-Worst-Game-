import pygame

class life:
    def __init__(self,surface):
        self.display_surface = surface 
        self.health_bar = pygame.image.load('health_bar.png')
        self.health_bar_topleft = (54,39)
        self.bar_max_width = 152
        self.bar_height = 4

    def printLife(self,current,max):
        self.current=current
        self.max=max
        self.display_surface.blit(self.health_bar,(20,10))
        current_health_ratio = self.current / self.max
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(self.health_bar_topleft,(current_bar_width,self.bar_height))
        pygame.draw.rect(self.display_surface,'#dc4949',health_bar_rect)
