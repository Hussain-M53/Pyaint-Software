import pygame
from utils import *

class ColorMode:
    def __init__(self,color_window_rect,color_window_heading_rect ):
        self.text1 = "R"
        self.text2 = "G"
        self.text3 = "B"
        self.isRGB = True
        self.color_mode_rect = pygame.Rect(
            color_window_rect.x+color_window_rect.w-270, color_window_heading_rect.y+color_window_heading_rect.h+5, 260, 130)
        self.buttons= []
        self.add_buttons()

    def add_buttons(self):
        # color mode structure
        self.buttons.append(Button(self.color_mode_rect.x+10,
                            self.color_mode_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "MODE", GRAY, pallete=True))
        self.buttons.append(Button(self.color_mode_rect.x+self.color_mode_rect.w-56,
                                   self.color_mode_rect.y+10, 46, 20, image_url="assets/hsv_toggle.png", name="toggle"))
        # input box 1
        self.buttons.append(Button(self.color_mode_rect.x+20, self.color_mode_rect.y+35,
                            60, 20, COLOR_PALLETE_RECT, self.text1, RED, name="input_box_rh_text", pallete=True,))
        self.buttons.append(Button(self.color_mode_rect.x+20,
                            self.color_mode_rect.y+55, 60, 20, BG_COLOR_PALLETE_WINDOW, name="input_box_rh", isBorderRadius=True))
        self.buttons.append(Button(self.color_mode_rect.x+20, self.color_mode_rect.y+55,
                                   60, 20, BG_COLOR_PALLETE_WINDOW, text_color=GRAY, name="input_box_rh_input", pallete=True,))
        # input box 2
        self.buttons.append(Button(self.color_mode_rect.x+90, self.color_mode_rect.y+35,
                            60, 20, COLOR_PALLETE_RECT, self.text2, GREEN, name="input_box_gs_text", pallete=True))
        self.buttons.append(Button(self.color_mode_rect.x+90,
                            self.color_mode_rect.y+55, 60, 20, BG_COLOR_PALLETE_WINDOW, name="input_box_gs", isBorderRadius=True))
        self.buttons.append(Button(self.color_mode_rect.x+90, self.color_mode_rect.y+55,
                                   60, 20, BG_COLOR_PALLETE_WINDOW, text_color=GRAY, name="input_box_gs_input", pallete=True))
        # input box 3
        self.buttons.append(Button(self.color_mode_rect.x+160, self.color_mode_rect.y+35, 60,
                            20, COLOR_PALLETE_RECT, self.text3, BLUE, name="input_box_bv_text", pallete=True))
        self.buttons.append(Button(self.color_mode_rect.x+160,
                            self.color_mode_rect.y+55, 60, 20, BG_COLOR_PALLETE_WINDOW, name="input_box_bv", isBorderRadius=True))
        self.buttons.append(Button(self.color_mode_rect.x+160, self.color_mode_rect.y+55, 60,
                                   20, BG_COLOR_PALLETE_WINDOW, text_color=GRAY, name="input_box_bv_input", pallete=True))
        # preview color box
        self.buttons.append(Button(self.color_mode_rect.x+20,
                            self.color_mode_rect.y+80, 40, 40, COLOR_PALLETE_RECT, isBorder=True, name="color_mode_preview_box"))
        # add to custom button
        self.buttons.append(Button(self.color_mode_rect.x+70, self.color_mode_rect.y+85,
                            150, 30, BG_COLOR_PALLETE_WINDOW, name="add_to_custom_colors", isBorderRadius=True))
        self.buttons.append(Button(self.color_mode_rect.x+125, self.color_mode_rect.y+85,
                            40, 30, BG_COLOR_PALLETE_WINDOW, "Add To Custom Colors", GRAY))    


    def draw(self,win):
        pygame.draw.rect(win, COLOR_PALLETE_RECT,
                         self.color_mode_rect, border_radius=6)
        for button in self.buttons:
            button.draw(win)
