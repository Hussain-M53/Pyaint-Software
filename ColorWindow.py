import math
import pygame
from utils import *


class ColorWindow:
    def __init__(self, theme):
        self.theme = theme
        self.text1 = "R"
        self.text2 = "G"
        self.text3 = "B"
        if (self.theme.getMode() == "dark"):
            self.bg_color = DARKGRAY
            self.text_color = BG_COLOR_PALLETE_WINDOW
        else:
            self.bg_color = BG_COLOR_PALLETE_WINDOW
            self.text_color = GRAY
        self.isRGB = True
        self.height = 520
        self.width = 550
        self.color_window_rect = pygame.Rect(
            WIDTH/2-(self.width/2), HEIGHT/2-(self.height/2)-50, self.width, self.height)
        self.color_window_heading_rect = pygame.Rect(
            WIDTH/2-80, self.color_window_rect.x+55, 80, 40)
        # left-hand tools
        self.color_grayscale_rect = pygame.Rect(
            self.color_window_rect.x+10, self.color_window_heading_rect.y+self.color_window_heading_rect.h+5, 260, 130)
        self.color_gradient_rect = pygame.Rect(
            self.color_window_rect.x+10, self.color_grayscale_rect.y+self.color_grayscale_rect.h+10, 260, 130)
        self.custom_gradient_rect = pygame.Rect(
            self.color_window_rect.x+10, self.color_gradient_rect.y+self.color_gradient_rect.h+10, 260, 130)
        # right hand tools
        self.color_mode_rect = pygame.Rect(
            self.color_window_rect.x+self.color_window_rect.w-270, self.color_window_heading_rect.y+self.color_window_heading_rect.h+5, 260, 130)
        self.color_mixer_rect = pygame.Rect(
            self.color_window_rect.x+self.color_window_rect.w-270, self.color_mode_rect.y+self.color_mode_rect.h+10, 260, 130)
        self.custom_color_rect = pygame.Rect(
            self.color_window_rect.x+self.color_window_rect.w-270, self.color_mixer_rect.y+self.color_mixer_rect.h+10, 260, 130)
        self.add_button()

    def get_index(self, name):
        i = 0
        for button in self.buttons:
            if (button.name == name):
                return i
            i += 1
        return -1

    def hsv_to_rgb(h, s, v):
        M = 255*v
        m = M(1-s)
        z = (M-m)(1 - abs(math.fmod(h/60.0, 2)-1))
        if h >= 0 and h < 60:
            R = M
            G = z + m
            B = m
        if h >= 60 and h < 120:
            R = z + m
            G = M
            B = m
        if h >= 120 and h < 180:
            R = m
            G = M
            B = z + m
        if h >= 180 and h < 240:
            R = m
            G = z + m
            B = M
        if h >= 240 and h < 300:
            R = z + m
            G = m
            B = M
        if h >= 300 and h < 360:
            R = M
            G = m
            B = z + m

        return int(R), int(G), int(B)

    def add_button(self):
        self.buttons = []
        self.buttons.append(Button(self.color_window_rect.w+self.color_window_rect.x-25, self.color_window_rect.y +
                            5, 20, 20, image_url="assets/color_window_exit.png", name="Exit_Color_Window"))
        self.buttons.append(Button(self.color_window_heading_rect.x+self.color_window_heading_rect.w/2, self.color_window_heading_rect.y,
                            self.color_window_heading_rect.w, self.color_window_heading_rect.h, text="COLOR PALLETE", text_color=self.text_color, shape="", pallete=True))
    # grayscale mode structure
        self.buttons.append(Button(self.color_grayscale_rect.x+35,
                            self.color_grayscale_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "GRAYSCALE", GRAY, pallete=True))

    # color mode structure
        self.buttons.append(Button(self.color_mode_rect.x+10,
                            self.color_mode_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "MODE", GRAY, pallete=True))
        self.buttons.append(Button(self.color_mode_rect.x+self.color_mode_rect.w-56,
                                   self.color_mode_rect.y+10, 46, 20, image_url="assets/hsv_toggle.png", name="toggle"))
        # input box 1
        self.buttons.append(Button(self.color_mode_rect.x+20, self.color_mode_rect.y+35,
                            60, 20, COLOR_PALLETE_RECT, self.text1, GRAY, name="input_box_rh_text", pallete=True,))
        self.buttons.append(Button(self.color_mode_rect.x+20,
                            self.color_mode_rect.y+55, 60, 20, BG_COLOR_PALLETE_WINDOW, name="input_box_rh", isBorderRadius=True))
        self.buttons.append(Button(self.color_mode_rect.x+20, self.color_mode_rect.y+55,
                                   60, 20, BG_COLOR_PALLETE_WINDOW, text_color=GRAY, name="input_box_rh_input", pallete=True,))
        # input box 2
        self.buttons.append(Button(self.color_mode_rect.x+90, self.color_mode_rect.y+35,
                            60, 20, COLOR_PALLETE_RECT, self.text2, GRAY, name="input_box_gs_text", pallete=True))
        self.buttons.append(Button(self.color_mode_rect.x+90,
                            self.color_mode_rect.y+55, 60, 20, BG_COLOR_PALLETE_WINDOW, name="input_box_gs", isBorderRadius=True))
        self.buttons.append(Button(self.color_mode_rect.x+90, self.color_mode_rect.y+55,
                                   60, 20, BG_COLOR_PALLETE_WINDOW, text_color=GRAY, name="input_box_gs_input", pallete=True))
        # input box 3
        self.buttons.append(Button(self.color_mode_rect.x+160, self.color_mode_rect.y+35, 60,
                            20, COLOR_PALLETE_RECT, self.text3, GRAY, name="input_box_bv_text", pallete=True))
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
    # gradient mode structure
        self.buttons.append(Button(self.color_gradient_rect.x+28,
                            self.color_gradient_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "GRADIENT", GRAY, pallete=True))

    #  mode structure
        self.buttons.append(Button(self.color_mode_rect.x+10,
                            self.color_mixer_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "MIXER", GRAY, pallete=True))

    # mixer mode structure
        self.buttons.append(Button(self.color_mode_rect.x+10,
                            self.color_mixer_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "MIXER", GRAY, pallete=True))

    # gradient pallete
        self.buttons.append(Button(self.custom_gradient_rect.x+70,
                            self.custom_gradient_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "CUSTOM GRADIENTS", GRAY, pallete=True))
        self.buttons.append(Button(self.custom_gradient_rect.x+8, self.custom_gradient_rect.y+50,
                                   28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"custom_gradient_1", isBorder=True))
        for i in range(2, 9):
            self.buttons.append(Button(self.custom_gradient_rect.x+8+(i)+(30*(i-1)), self.custom_gradient_rect.y+50,
                                       28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"custom_gradient_{i}", isBorder=True))
        self.buttons.append(Button(self.custom_gradient_rect.x+8, self.custom_gradient_rect.y+90,
                                   28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"custom_gradient_9", isBorder=True))
        for i in range(10, 17):
            self.buttons.append(Button(self.custom_gradient_rect.x+8+(i-8)+(30*(i-9)), self.custom_gradient_rect.y+90,
                                       28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"custom_gradient_{i}", isBorder=True))

    # color pallete
        self.buttons.append(Button(self.custom_color_rect.x+55,
                            self.custom_color_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "CUSTOM COLORS", GRAY, pallete=True))
        self.buttons.append(Button(self.custom_color_rect.x+8, self.custom_color_rect.y+50,
                                   28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"custom_color_1", isBorder=True))
        for i in range(2, 9):
            self.buttons.append(Button(self.custom_color_rect.x+8+(i)+(30*(i-1)), self.custom_color_rect.y+50,
                                       28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"custom_color_{i}", isBorder=True))

        self.buttons.append(Button(self.custom_color_rect.x+8, self.custom_color_rect.y+90,
                                   28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"custom_color_9", isBorder=True))
        for i in range(10, 17):
            self.buttons.append(Button(self.custom_color_rect.x+8+(i-8)+(30*(i-9)), self.custom_color_rect.y+90,
                                       28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"custom_color_{i}", isBorder=True))

    def draw_buttons(self, win):
        for button in self.buttons:
            button.draw(win)

    def get_row_col_from_pos(pos):
        x, y = pos
        row = y // PIXEL_SIZE
        col = x // PIXEL_SIZE

        if row >= ROWS:
            raise IndexError
        if col >= ROWS:
            raise IndexError
        return row, col

    def preview_color(self):
        rh=0
        gs=0
        bv=0
        if self.buttons[self.get_index("input_box_rh_input")].text:
            rh =int(self.buttons[self.get_index("input_box_rh_input")].text)
        if self.buttons[self.get_index("input_box_gs_input")].text:
            gs = int(self.buttons[self.get_index("input_box_gs_input")].text)
        if self.buttons[self.get_index("input_box_bv_input")].text:
            bv = int(self.buttons[self.get_index("input_box_bv_input")].text)
        if not self.isRGB:
            rh,gs,bv = self.hsv_to_rgb(rh,gs,bv)
        self.buttons[(self.get_index("color_mode_preview_box"))].color = (rh,gs,bv)


    def run(self, win):
        pygame.draw.rect(win, self.bg_color,
                         self.color_window_rect, border_radius=5)
        pygame.draw.rect(win, GRAY, (WIDTH/2-(self.width/2), HEIGHT/2-(self.height/2)-50,
                         self.width, 30), border_top_left_radius=5, border_top_right_radius=4)
        pygame.draw.rect(
            win, COLOR_PALLETE_RECT, self.color_grayscale_rect, border_radius=6)
        pygame.draw.rect(win, COLOR_PALLETE_RECT,
                         self.color_mode_rect, border_radius=6)
        pygame.draw.rect(win, COLOR_PALLETE_RECT,
                         self.color_gradient_rect, border_radius=6)
        pygame.draw.rect(win, COLOR_PALLETE_RECT,
                         self.color_mixer_rect, border_radius=6)
        pygame.draw.rect(win, COLOR_PALLETE_RECT,
                         self.custom_color_rect, border_radius=6)
        pygame.draw.rect(
            win, COLOR_PALLETE_RECT, self.custom_gradient_rect, border_radius=4)
        running = True
        while running:
            pygame.display.update()
            # for loop through the event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # if user closed the program
                    running = False
                # Check for QUIT event
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    for button in self.buttons:
                        if not button.clicked(pos):
                            if (button.name == "input_box_rh_input" or button.name == "input_box_gs_input" or button.name == "input_box_bv_input") and button.input_box_selected:
                                button.input_box_selected = False
                                button.isBorder = False
                            continue
                        if button.name == "Exit_Color_Window":
                            running = False
                        elif button.name == "toggle" and self.isRGB:
                            button.image_url = "assets/rgb_toggle.png"
                            self.isRGB = False
                            for btn in self.buttons:
                                if (btn.name == "input_box_rh_text"):
                                    btn.text = "H"
                                elif (btn.name == "input_box_gs_text"):
                                    btn.text = "S"
                                elif (btn.name == "input_box_bv_text"):
                                    btn.text = "V"

                        elif button.name == "toggle" and not self.isRGB:
                            button.image_url = "assets/hsv_toggle.png"
                            self.isRGB = True
                            for btn in self.buttons:
                                if (btn.name == "input_box_rh_text"):
                                    btn.text = "R"
                                elif (btn.name == "input_box_gs_text"):
                                    btn.text = "G"
                                elif (btn.name == "input_box_bv_text"):
                                    btn.text = "B"
                        elif button.name == "input_box_rh_input" or button.name == "input_box_gs_input" or button.name == "input_box_bv_input":
                            button.isBorder = True
                            button.input_box_selected = True
                        elif button.name == "add_to_custom_colors":
                            print("add to colors")


                if event.type == pygame.KEYDOWN:
                    for button in self.buttons:
                        if ((button.name == "input_box_rh_input" and button.input_box_selected) or (button.name == "input_box_gs_input" and button.input_box_selected) or (button.name == "input_box_bv_input" and button.input_box_selected)):
                            if event.key == pygame.K_BACKSPACE:
                                userInput = button.text
                                userInput = userInput[:-1]
                                button.text = userInput
                            elif (
                                event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9
                            ) and len(button.text) < 3:
                                userInput = button.text
                                userInput += event.unicode
                                if self.isRGB:
                                    if int(userInput) > 255:
                                        userInput = userInput[0:2]
                                else:
                                    if button.name == "input_box_rh_input":
                                        if int(userInput) > 360:
                                            userInput = userInput[0:2]
                                    if (
                                        button.name == "input_box_gs_input"
                                        or button.name == "input_box_bv_input"
                                    ):
                                        if int(userInput) > 100:
                                            userInput = userInput[0:2]
                                button.text = userInput
                                self.preview_color()


            self.draw_buttons(win)
