from utils import *
import pygame


class ColorMixer:
    def __init__(self, color_window_rect, color_mode_rect):
        self.text1 = "Red"
        self.text2 = "Green"
        self.text3 = "Blue"
        self.isRGB = True
        self.color_mixer_rect = pygame.Rect(
            color_window_rect.x+color_window_rect.w-270, color_mode_rect.y+color_mode_rect.h+10, 260, 150)
        self.add_buttons()

    def add_buttons(self):
        # color mode structure
        self.buttons = []
        self.buttons.append(Button(self.color_mixer_rect.x+10,
                            self.color_mixer_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "MIXER", GRAY, pallete=True))
        self.buttons.append(Button(self.color_mixer_rect.x+self.color_mixer_rect.w-56,
                                   self.color_mixer_rect.y+10, 46, 20, image_url="assets/hsv_toggle.png", name="toggle"))
        # color 1 input box 1
        self.buttons.append(Button(self.color_mixer_rect.x+6,
                            self.color_mixer_rect.y+55, 45, 20, COLOR_PALLETE_RECT, "Color 1:", GRAY, pallete=True))
        self.buttons.append(Button(self.color_mixer_rect.x+50, self.color_mixer_rect.y+35,
                            60, 20, COLOR_PALLETE_RECT, self.text1, GRAY, name="input_box_rh_text", pallete=True,))
        self.buttons.append(Button(self.color_mixer_rect.x+50,
                            self.color_mixer_rect.y+55, 60, 20, BG_COLOR_PALLETE_WINDOW, name="input_box1_rh", isBorderRadius=True))
        self.buttons.append(Button(self.color_mixer_rect.x+50, self.color_mixer_rect.y+55,
                                   60, 20, BG_COLOR_PALLETE_WINDOW, text_color=GRAY, name="input_box1_rh_input", pallete=True,))
        # color 1 input box 2
        self.buttons.append(Button(self.color_mixer_rect.x+120, self.color_mixer_rect.y+35,
                            60, 20, COLOR_PALLETE_RECT, self.text2, GRAY, name="input_box_gs_text", pallete=True))
        self.buttons.append(Button(self.color_mixer_rect.x+120,
                            self.color_mixer_rect.y+55, 60, 20, BG_COLOR_PALLETE_WINDOW, name="input_box1_gs", isBorderRadius=True))
        self.buttons.append(Button(self.color_mixer_rect.x+120, self.color_mixer_rect.y+55,
                                   60, 20, BG_COLOR_PALLETE_WINDOW, text_color=GRAY, name="input_box1_gs_input", pallete=True))
        # color 1 input box 3
        self.buttons.append(Button(self.color_mixer_rect.x+190, self.color_mixer_rect.y+35, 60,
                            20, COLOR_PALLETE_RECT, self.text3, GRAY, name="input_box_bv_text", pallete=True))
        self.buttons.append(Button(self.color_mixer_rect.x+190,
                            self.color_mixer_rect.y+55, 60, 20, BG_COLOR_PALLETE_WINDOW, name="input_box1_bv", isBorderRadius=True))
        self.buttons.append(Button(self.color_mixer_rect.x+190, self.color_mixer_rect.y+55, 60,
                                   20, BG_COLOR_PALLETE_WINDOW, text_color=GRAY, name="input_box1_bv_input", pallete=True))
        # color 2 input box 1
        self.buttons.append(Button(self.color_mixer_rect.x+6,
                            self.color_mixer_rect.y+80, 45, 20, COLOR_PALLETE_RECT, "Color 2:", GRAY, pallete=True))

        self.buttons.append(Button(self.color_mixer_rect.x+50,
                            self.color_mixer_rect.y+80, 60, 20, BG_COLOR_PALLETE_WINDOW, name="input_box2_rh", isBorderRadius=True))
        self.buttons.append(Button(self.color_mixer_rect.x+50, self.color_mixer_rect.y+80,
                                   60, 20, BG_COLOR_PALLETE_WINDOW, text_color=GRAY, name="input_box2_rh_input", pallete=True,))
        # color 2 input box 2
        self.buttons.append(Button(self.color_mixer_rect.x+120,
                            self.color_mixer_rect.y+80, 60, 20, BG_COLOR_PALLETE_WINDOW, name="input_box2_gs", isBorderRadius=True))
        self.buttons.append(Button(self.color_mixer_rect.x+120, self.color_mixer_rect.y+80,
                                   60, 20, BG_COLOR_PALLETE_WINDOW, text_color=GRAY, name="input_box2_gs_input", pallete=True))
        # color 2 input box 3
        self.buttons.append(Button(self.color_mixer_rect.x+190,
                            self.color_mixer_rect.y+80, 60, 20, BG_COLOR_PALLETE_WINDOW, name="input_box2_bv", isBorderRadius=True))
        self.buttons.append(Button(self.color_mixer_rect.x+190, self.color_mixer_rect.y+80, 60,
                                   20, BG_COLOR_PALLETE_WINDOW, text_color=GRAY, name="input_box2_bv_input", pallete=True))
        # preview color box
        self.buttons.append(Button(self.color_mixer_rect.x+50,
                                   self.color_mixer_rect.y+105, 40, 40, COLOR_PALLETE_RECT, isBorder=True, name="color_mixer_preview_box"))
        # add to custom button
        self.buttons.append(Button(self.color_mixer_rect.x+100, self.color_mixer_rect.y+110,
                            150, 30, BG_COLOR_PALLETE_WINDOW, name="add_to_custom_colors", isBorderRadius=True))
        self.buttons.append(Button(self.color_mixer_rect.x+155, self.color_mixer_rect.y+110,
                            40, 30, BG_COLOR_PALLETE_WINDOW, "Add To Custom Colors", GRAY))

    def draw(self, win):
        pygame.draw.rect(win, COLOR_PALLETE_RECT,
                         self.color_mixer_rect, border_radius=6)
        for button in self.buttons:
            button.draw(win)

   