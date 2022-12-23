import pygame
from utils import *
class ColorPicker:
    def __init__(self):
        self.picked_color= WHITE

    
    def get_position(self,pos):
        x, y = pos
        row = y # PIXEL_SIZE
        col = x # PIXEL_SIZE
        return row, col

    #Color Picker
    def pickColor(self,grid):
        pos = pygame.mouse.get_pos()
        i, j = self.get_position(pos)
        if i < 40 and j < 40:
            preColor = grid[i][j]
            return preColor


