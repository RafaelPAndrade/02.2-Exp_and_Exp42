#Attempt at function to easily write stuff

import pygame


def words(x, y, color, size, string):
    font = pygame.font.Font(None, size)
    text = font.render(string, 1, color) #color may refer to the constants.py file
    textpos = text.get_rect()
    textpos.centerx = x
    textpos.centery = y
    screen.blit(text, textpos)
    
    return True


