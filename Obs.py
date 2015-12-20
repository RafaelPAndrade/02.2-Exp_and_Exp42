#coding: latin-1

#Obs
import pygame
from block import Block
import random
import constants



class Obs(Block):
    def __init__(self, x, y, color):
        super(Obs, self).__init__(x, y, constants.ObsSize, constants.ObsSize,color)
        self.change_x = 0
    
    def generate(self):
        self.canon = random.randint(0,8)
        self.rect.y = (self.canon*50) + 17
        self.change_x = random.randint (1,2)
            
    
    def update(self):
        self.rect.x += self.change_x
