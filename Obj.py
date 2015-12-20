#coding: latin-1
#obj

import pygame
from block import Block
import constants


class Obj(Block):
    def __init__(self, x, y, width, height, color):
        super(Obj, self).__init__(x, y, width, height, color)
        self.change_x = 0
        self.change_y = 0
        
        
    def move_up(self):
        self.change_y = -constants.VEL
        self.change_x = constants.NULL
        
        
    def move_down(self):
        self.change_y = constants.VEL
        self.change_x = constants.NULL 
        
        
    def move_left(self):
        self.change_x = -constants.VEL
        self.change_y = constants.NULL        

    def move_right(self):
        self.change_x = constants.VEL
        self.change_y = constants.NULL
    
    def dont_move(self):
        self.change_x = constants.NULL
        self.change_y = constants.NULL
                
    def update (self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
