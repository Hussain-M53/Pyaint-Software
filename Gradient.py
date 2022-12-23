from utils import *
import pygame


# class Gradient:
#     def _init_(self,color_window_rect,color_grayscale_rect):
#         self.buttons= []
#         self.add_buttons()
#         self.color_gradient_rect = pygame.Rect(self.color_window_rect.x+10, self.color_grayscale_rect.y+self.color_grayscale_rect.h+10, 260, 130)
#         self.add_buttons()
#
#     def add_buttons(self):
#         self.buttons.append(
#             Button(self.color_gradient_rect.x + 8 + (3 * (i - 8)) + (28 * (i - 8)), self.color_gradient_rect.y + 90,
#                    28, 28, BG_COLOR_PALLETE_WINDOW, shape="square", name=f"color_gradient_{i}", isBorder=True))
#
#     def gradient(self,win):
#         # define start and end colors directly
#         color1 = (255, 0, 0)  # red
#         color2 = (0, 255, 0)  # green
#
#         # or use a color picker widget to select the colors
#         #color1 = (255, 0, 0)  # red
#         #color2 = (0, 255, 0)  # green
#
#         h1, l1, s1 = self.hsv_to_rgb(color1[0] / 255, color1[1] / 255, color1[2] / 255)
#         h2, l2, s2 = self.hsv_to_rgb(color2[0] / 255, color2[1] / 255, color2[2] / 255)
#         dh = (h2 - h1) / 100
#         dl = (l2 - l1) / 100
#         ds = (s2 - s1) / 100
#
#         gradient = []
#         for i in range(100):
#             h = h1 + dh * i
#             l = l1 + dl * i
#             s = s1 + ds * i
#             r, g, b = pygame.hls_to_rgb(h, l, s)
#             gradient.append((int(r * 255), int(g * 255), int(b * 255)))
#
#         gradient_surface = pygame.Surface((300, 100))
#         for i in range(100):
#             y = i
#             pygame.draw.line(gradient_surface, gradient[i], (0, y), (300, y))
#         win.blit(gradient_surface, (0, 0))

class Gradient:
    def __init__(self,  color_window_rect, color_mode_rect):
        self.color_gradient_rect = pygame.Rect(
            color_window_rect.x + color_window_rect.w -540, color_mode_rect.y + color_mode_rect.h+10 , 260, 130)
        self.buttons = []
        self.add_buttons()

    def add_buttons(self):
        # color 1 input box 1
        self.buttons = []
        self.buttons.append(Button(self.color_gradient_rect.x+140 , self.color_gradient_rect.y + 75,
                                   55, 20, COLOR_PALLETE_RECT, text= "opacity", text_color=GRAY, name="input_box_text",
                                   pallete=True,))
        self.buttons.append(Button(self.color_gradient_rect.x + 200,
                                   self.color_gradient_rect.y + 75, 55, 20, BG_COLOR_PALLETE_WINDOW, name="input_box1_rh",
                                   isBorderRadius=True))
        self.buttons.append(Button(self.color_gradient_rect.x + 200, self.color_gradient_rect.y + 75,
                                   55, 20, BG_COLOR_PALLETE_WINDOW, text_color=GRAY, name="input_gradient_box1_input",
                                   pallete=True, ))

        # preview color box
        self.buttons.append(Button(self.color_gradient_rect.x + 160,
                                   self.color_gradient_rect.y + 40, 55, 20, COLOR_PALLETE_RECT, text="preview",text_color=GRAY,
                                   name="gradient_preview",pallete=True))
        self.buttons.append(Button(self.color_gradient_rect.x + 220,
                                   self.color_gradient_rect.y + 33, 35, 35, COLOR_PALLETE_RECT, isBorder=True,
                                   name="gradient_preview_box"))
        # add to custom button
        self.buttons.append(Button(self.color_gradient_rect.x + 135, self.color_gradient_rect.y + 100,
                                   120, 28, BG_COLOR_PALLETE_WINDOW, name="add_to_custom_colors", isBorderRadius=True))
        self.buttons.append(Button(self.color_gradient_rect.x + 175, self.color_gradient_rect.y + 100,
                                   40, 30, BG_COLOR_PALLETE_WINDOW, "Add To Custom Colors", GRAY))

    def draw(self, win):
        pygame.draw.rect(win, COLOR_PALLETE_RECT,
                         self.color_gradient_rect, border_radius=6)
        for button in self.buttons:
            button.draw(win)