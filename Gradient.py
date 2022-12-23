from utils import *
import pygame

from pygame import math

from utils import *
import pygame


# class Gradient:
#     def _init_(self, win, color_window_rect, color_grayscale_rect):
#         self.buttons = []
#         self.win = win
#         self.add_buttons()
#         self.color_window_rect = color_window_rect
#         self.color_grayscale_rect = color_grayscale_rect
#         self.gradient_surface = pygame.Rect(self.color_window_rect.x + 10,
#                                             self.color_grayscale_rect.y + self.color_grayscale_rect.h + 10, 260, 130)
#         self.add_buttons()
#
#         self.colour_rect = pygame.Surface((2, 2))
#         pygame.draw.line(self.colour_rect, RED, (0, 0), (0, 1))
#         pygame.draw.line(self.colour_rect, BLUE, (1, 0), (1, 1))
#         colour_rect = pygame.transform.smoothscale(self.colour_rect, (
#             WIDTH / 2 - (self.width / 2) + 120, self.color_gradient_rect.y - 100))  # stretch!
#         win.blit(colour_rect,
#                  (WIDTH / 2 - (self.width / 2) + 12, self.color_gradient_rect.y + self.color_gradient_rect.h - 60))


#PURANI HAII
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
    def __init__(self,  color_window_rect, color_grayscale_rect):
        self.color_gradient_rect = pygame.Rect(
            color_window_rect.x + color_window_rect.w -540, color_grayscale_rect.y + color_grayscale_rect.h+10 , 260, 130)
        self.buttons = []
        self.add_buttons()

    def add_buttons(self):
        # input box 1
        self.buttons = []
         # gradient mode structure
        self.buttons.append(Button(self.color_gradient_rect.x+28,
                            self.color_gradient_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "GRADIENT", GRAY, pallete=True))

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

        #color_gradient
        self.buttons.append(Button(self.color_gradient_rect.x + 8, self.color_gradient_rect.y + 40,
                                   120, 80, BG_COLOR_PALLETE_WINDOW, name="color_gradient", image_url="assets/color_gradient.png"))


    def draw(self, win):
        pygame.draw.rect(win, COLOR_PALLETE_RECT,
                         self.color_gradient_rect, border_radius=6)
        for button in self.buttons:
            button.draw(win)

    #
    # def hsv_to_rgb(self, h, s, v):
    #     M = 255 * v
    #     m = M * (1 - s)
    #     z = (M - m) * (1 - abs(math.fmod(h / 60.0, 2) - 1))
    #     if h >= 0 and h < 60:
    #         R = M
    #         G = z + m
    #         B = m
    #     if h >= 60 and h < 120:
    #         R = z + m
    #         G = M
    #         B = m
    #     if h >= 120 and h < 180:
    #         R = m
    #         G = M
    #         B = z + m
    #     if h >= 180 and h < 240:
    #         R = m
    #         G = z + m
    #         B = M
    #     if h >= 240 and h < 300:
    #         R = z + m
    #         G = m
    #         B = M
    #     if h >= 300 and h < 360:
    #         R = M
    #         G = m
    #         B = z + m
    #
    #     return int(R), int(G), int(B)
    #
    # def gradient(self, win):
    #     # define start and end colors directly
    #     color1 = (255, 0, 0)  # red
    #     color2 = (0, 255, 0)  # green
    #
    #     # or use a color picker widget to select the colors
    #     # color1 = (255, 0, 0)  # red
    #     # color2 = (0, 255, 0)  # green
    #
    #     h1, l1, s1 = Gradient.hsv_to_rgb(color1[0] / 255, color1[1] / 255, color1[2] / 255)
    #     h2, l2, s2 = Gradient.hsv_to_rgb(color2[0] / 255, color2[1] / 255, color2[2] / 255)
    #     dh = (h2 - h1) / 100
    #     dl = (l2 - l1) / 100
    #     ds = (s2 - s1) / 100
    #
    #     gradient = []
    #     for i in range(100):
    #         h = h1 + dh * i
    #         l = l1 + dl * i
    #         s = s1 + ds * i
    #         r, g, b = Gradient.hsv_to_rgb(h, l, s)
    #         gradient.append((int(r * 255), int(g * 255), int(b * 255)))
    #
    #     gradient_surface = pygame.Surface((300, 100))
    #     for i in range(100):
    #         y = i
    #         pygame.draw.line(gradient_surface, gradient[i], (0, y), (300, y))
    #     win.blit(gradient_surface, (0, 0))
    #     pygame.display.update()
    #
    # def color(self,win):
    #     spectrum = 255 * 6 / self.color_gradient_rect.w
    #     red = 255
    #     green = 0
    #     blue = 0
    #
    #     colors = []
    #
    #     step = round(spectrum)
    #
    #     for i in range(0, self.color_window_rect):
    #         for j in range(0, 255 * 6 + 1, step):
    #             if j > 0 and j <= 255:
    #                 blue += step
    #             elif j > 255 and j <= 255 * 2:
    #                 red -= step
    #             elif j > 255 * 2 and j <= 255 * 3:
    #                 green += step
    #             elif j > 255 * 3 and j <= 255 * 4:
    #                 blue -= step
    #             elif j > 255 * 4 and j <= 255 * 5:
    #                 red += step
    #             elif j > 255 * 5 and j <= 255 * 6:
    #                 green -= step
    #             colors.append((red, green, blue))
    #             pygame.draw.rect(win, (print(str(colors)), 10, 70), border_radius=6)
    #     print(str(colors))
    #
    # def drawColorSpec(self, win):
    #     pygame.draw.rect(win, COLOR_PALLETE_RECT,
    #                      self.color_gradient_rect, border_radius=6)
    #
    # def drawGrad(self, win):
    #     pygame.draw.rect(win, COLOR_PALLETE_RECT,
    #                      self.color_gradient_rect.x + 40,
    #                      self.color_gradient_rect.y + 90,
    #                      28, 28)