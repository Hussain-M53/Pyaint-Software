import pygame
from utils import *


class ColorPicker:

    # Color Picker
    def pickColor(self,win):
        pos = pygame.mouse.get_pos()
        if pos[0] < 600 and pos[1] < 600:
            color = tuple(
                win.get_at(pos)
            )  # get the color of pixel at mouse position
            drawing_color = (color[0], color[1], color[2])
            return drawing_color   


    def preview_zoomed_color(self, win):
        pos = pygame.mouse.get_pos()
        if pos[0] <600 and pos[1] < 600:
            color = tuple(
                win.get_at(pos)
            )
            color_picker_button = Button(pos[0]+10,pos[1] - 50,50,50,(color[0], color[1], color[2]),shape="ellipse",isBorder=True)
            color_picker_button.draw(win)
