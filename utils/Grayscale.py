import pygame
from utils import *


class Grayscale:
    def __init__(self, color_window_rect, color_window_heading_rect):
        self.height = 520
        self.width = 550
        self.grayscale_index =1
        self.color_grayscale_rect = pygame.Rect(
            color_window_rect.x+10, color_window_heading_rect.y+color_window_heading_rect.h+5, 260, 150)
        self.slider_pos = self.color_grayscale_rect.y+28
        self.slider_value = self.color_grayscale_rect.x+10  # Initial range of the slider
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
        # preview color box
        self.buttons.append(Button(self.color_grayscale_rect.x+10,
                            self.color_grayscale_rect.y+90, 30, 30, COLOR_PALLETE_RECT, isBorder=True, name="grayscale_mode_preview_box"))
        # add to custom button
        self.buttons.append(Button(self.color_grayscale_rect.x+45, self.color_grayscale_rect.y+90,
                            115, 30, BG_COLOR_PALLETE_WINDOW, name="add_to_grayscale_colors", isBorderRadius=True))
        self.buttons.append(Button(self.color_grayscale_rect.x+85, self.color_grayscale_rect.y+95,
                            35, 20, BG_COLOR_PALLETE_WINDOW, "Add To Grayscale Colors", GRAY))    


        self.buttons.append(Button(self.slider_value, self.slider_pos, 20, 50,
                            DARKGRAY, isBorderRadius=True, name="slider",borderRadius=8))

    def draw(self, win):
        pygame.draw.rect(
            win, COLOR_PALLETE_RECT, self.color_grayscale_rect, border_radius=6)
        self.colour_rect = pygame.Surface((2, 2))
        pygame.draw.line(self.colour_rect, WHITE, (0, 0), (0, 1))
        pygame.draw.line(self.colour_rect, BLACK, (1, 0), (1, 1))
        self.colour_rect = pygame.transform.smoothscale(self.colour_rect,(140,30))  # stretch!
        win.blit(self.colour_rect,
                 (self.color_grayscale_rect.x+10, self.color_grayscale_rect.y+40))
    
        for button in self.buttons:
            button.draw(win)

    def set_slider(self, win):
        pos = pygame.mouse.get_pos()
        color = tuple(
            win.get_at(pos)
        )
        for button in self.buttons:
            if button.name == "slider":
                button.x = pos[0]+2
            if button.name == "grayscale_mode_preview_box":
                button.color = color

    def add_to_grayscale_color(self):
        if self.grayscale_index > 13:
            print("zero")
            self.grayscale_index = 1
        for button in self.buttons:
            if button.name == "grayscale_mode_preview_box":
                color = button.color
        print("added to grayscale colors")
        print(self.grayscale_index)
        self.buttons[self.grayscale_index].color = color
        self.grayscale_index += 1