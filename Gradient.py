from utils import *
import pygame

class Gradient:
    def __init__(self,  color_window_rect, color_grayscale_rect):
        self.color_gradient_rect = pygame.Rect(
            color_window_rect.x + color_window_rect.w -540, color_grayscale_rect.y + color_grayscale_rect.h+10 , 260, 130)
        self.buttons = []
        self.rect = []
        self.grad_color = ()
        self.added_to_custom_grad = False
        self.add_buttons()

    def add_buttons(self):
        # input box 1
        self.buttons = []
         # gradient mode structure
        self.buttons.append(Button(self.color_gradient_rect.x+28,
                            self.color_gradient_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "GRADIENT", GRAY, pallete=True))

        self.buttons.append(Button(self.color_gradient_rect.x+140 , self.color_gradient_rect.y + 65,
                                   55, 20, COLOR_PALLETE_RECT, text= "opacity", text_color=GRAY, name="input_box_text",
                                   pallete=True,))
        self.buttons.append(Button(self.color_gradient_rect.x + 200,
                                   self.color_gradient_rect.y + 65, 55, 20, BG_COLOR_PALLETE_WINDOW, name="gradient_input_box",
                                   isBorderRadius=True))
        self.buttons.append(Button(self.color_gradient_rect.x + 200, self.color_gradient_rect.y + 65,
                                   55, 20, BG_COLOR_PALLETE_WINDOW, text_color=GRAY, name="gradient_input_box_input",
                                   pallete=True, ))

        # preview color box
        self.buttons.append(Button(self.color_gradient_rect.x + 160,
                                   self.color_gradient_rect.y + 30, 55, 20, COLOR_PALLETE_RECT, text="preview",text_color=GRAY,
                                   name="gradient_preview",pallete=True))
        self.buttons.append(Button(self.color_gradient_rect.x + 220,
                                   self.color_gradient_rect.y + 23, 35, 35, COLOR_PALLETE_RECT, isBorder=True,
                                   name="gradient_preview_box"))
        # add to custom button
        self.buttons.append(Button(self.color_gradient_rect.x + 135, self.color_gradient_rect.y + 90,
                                   120, 28, BG_COLOR_PALLETE_WINDOW, name="add_to_custom_gradient", isBorderRadius=True))
        self.buttons.append(Button(self.color_gradient_rect.x + 178, self.color_gradient_rect.y + 90,
                                   35, 28, BG_COLOR_PALLETE_WINDOW, "Add To Custom Gradient", GRAY))

        #color_gradient
        self.buttons.append(Button(self.color_gradient_rect.x + 8, self.color_gradient_rect.y + 40,
                                   120, 80, BG_COLOR_PALLETE_WINDOW, name="color_gradient", image_url="assets/color_gradient.png"))


    def draw(self, win):
        pygame.draw.rect(win, COLOR_PALLETE_RECT,
                         self.color_gradient_rect, border_radius=6)
        for button in self.buttons:
            button.draw(win)


    def stretchGradient(self, win, color):
        self.colour_rect = pygame.Surface((2, 2))
        pygame.draw.line(self.colour_rect, WHITE, (0, 0), (0, 1))
        pygame.draw.line(self.colour_rect, color, (1, 0), (1, 1))
        self.colour_rect = pygame.transform.smoothscale(self.colour_rect, (33, self.color_gradient_rect.y - 254))

        win.blit(self.colour_rect,
                 (self.color_gradient_rect.x + 221, self.color_gradient_rect.y+25))

    def stretchCustomGradient(self, win, color, i):
        self.colour_rect = pygame.Surface((2, 2))
        pygame.draw.line(self.colour_rect, WHITE, (0, 0), (0, 1))
        pygame.draw.line(self.colour_rect, color, (1, 0), (1, 1))
        self.colour_rect = pygame.transform.smoothscale(self.colour_rect, (23, self.color_gradient_rect.y - 262))
        self.rect.append(self.colour_rect)
        if i < 8:
            win.blit(self.colour_rect,
                 (self.color_gradient_rect.x + 11 + (i*30)+i, self.color_gradient_rect.y + 182))
        elif i < 15:
            j=0
            win.blit(self.colour_rect,
                     (self.color_gradient_rect.x + 11 + (j * 30) + j, self.color_gradient_rect.y + 218))
            j+=1

    def drawRect(self, win):
        j = 0
        for i in range(len(self.rect)):
            if i < 8:
                win.blit(self.rect[i],
                     (self.color_gradient_rect.x + 11 + (i * 30) + i, self.color_gradient_rect.y + 182))
            elif i < 16:
                win.blit(self.rect[i],
                         (self.color_gradient_rect.x + 11 + (j * 30) + j, self.color_gradient_rect.y + 218))
                j+=1