import pygame
from utils import *


class Grayscale:
    def __init__(self, color_window_rect, color_window_heading_rect):
    
        self.height = 520
        self.width = 550
        self.color_grayscale_rect = pygame.Rect(
            color_window_rect.x+10, color_window_heading_rect.y+color_window_heading_rect.h+5, 260, 150)
        self.slider_pos = self.color_grayscale_rect.y + 45
        self.slider_value = 45  # Initial range of the slider
        self.add_buttons()

    def add_buttons(self):
        # grayscale mode structure
        self.buttons = []
        self.buttons.append(Button(self.color_grayscale_rect.x+35,
                            self.color_grayscale_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "GRAYSCALE", GRAY, pallete=True))
        for i in range(3, 6):
            self.buttons.append(Button(self.color_grayscale_rect.x+320+(3*(i-8))+(28*(i-8)), self.color_grayscale_rect.y+20,
                                       28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"grayscale_{i-2}", isBorder=True))
        for i in range(3, 6):
            self.buttons.append(Button(self.color_grayscale_rect.x+320+(3*(i-8))+(28*(i-8)), self.color_grayscale_rect.y+50,
                                       28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"grayscale_{i+1}", isBorder=True))
        for i in range(3, 6):
            self.buttons.append(Button(self.color_grayscale_rect.x+320+(3*(i-8))+(28*(i-8)), self.color_grayscale_rect.y+80,
                                       28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"grayscale_{i+4}", isBorder=True))
        for i in range(3, 6):
            self.buttons.append(Button(self.color_grayscale_rect.x+320+(3*(i-8))+(28*(i-8)), self.color_grayscale_rect.y+110,
                                       28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"grayscale_{i+7}", isBorder=True))

        self.buttons.append(Button(self.slider_value,
                         self.slider_pos, 10, 50,BLACK,isBorderRadius= True))
    def draw(self,win):
        pygame.draw.rect(
            win, COLOR_PALLETE_RECT, self.color_grayscale_rect, border_radius=6)
        self.colour_rect = pygame.Surface((2, 2))
        pygame.draw.line(self.colour_rect, WHITE, (0, 0), (0, 1))
        pygame.draw.line(self.colour_rect, BLACK, (1, 0), (1, 1))
        self.colour_rect = pygame.transform.smoothscale(self.colour_rect, (WIDTH / 2 - (
            self.width / 2) + 120, self.color_grayscale_rect.y - 100))  # stretch!
        win.blit(self.colour_rect,
                 (WIDTH / 2 - (self.width / 2) + 12, self.color_grayscale_rect.y  + 60))
        for button in self.buttons:
            button.draw(win)

    def init_slider(self, win):
        self.draw(win)

       
