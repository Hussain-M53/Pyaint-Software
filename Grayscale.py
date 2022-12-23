import pygame
from utils import *


class Grayscale:
    def __init__(self, win, color_grayscale_rect):
        self.win = win
        self.color_grayscale_rect = color_grayscale_rect
        self.slider_pos = 0
        self.slider_value = 0
        self.height = 520
        self.width = 550
        self.colour_rect = pygame.Surface((2, 2))
        pygame.draw.line(self.colour_rect, WHITE, (0, 0), (0, 1))
        pygame.draw.line(self.colour_rect, BLACK, (1, 0), (1, 1))
        colour_rect = pygame.transform.smoothscale(self.colour_rect, (WIDTH / 2 - (self.width / 2) + 120, self.color_grayscale_rect.y - 100))  # stretch!
        win.blit(colour_rect,
                 (WIDTH / 2 - (self.width / 2) + 12, self.color_grayscale_rect.y + self.color_grayscale_rect.h - 60))

    def init_slider(self):

        self.slider_pos = self.color_grayscale_rect.y + 45
        self.slider_value = 40  # Initial range of the slider
        pygame.draw.rect(self.win, BLACK, (self.slider_value, self.slider_pos, 10, 70), border_radius=6)

    def drawSlider(self, x):
        self.slider_value = x-5
        pygame.draw.rect(self.win, BLACK, (self.slider_value, self.slider_pos, 10, 70), border_radius=6)

