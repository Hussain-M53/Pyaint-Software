import math
import pygame
from utils import *
from ColorMode import ColorMode
from ColorMixer import ColorMixer


class ColorWindow:
    def __init__(self, theme):
        self.theme = theme
        self.custom_color_index = 1
        self.custom_gradient_index = 1
        if (self.theme.getMode() == "dark"):
            self.bg_color = DARKGRAY
            self.text_color = BG_COLOR_PALLETE_WINDOW
        else:
            self.bg_color = BG_COLOR_PALLETE_WINDOW
            self.text_color = GRAY
        self.height = 520
        self.width = 550
        self.color_window_rect = pygame.Rect(
            WIDTH/2-(self.width/2), HEIGHT/2-(self.height/2)-50, self.width, self.height)
        self.color_window_heading_rect = pygame.Rect(
            WIDTH/2-80, self.color_window_rect.x+55, 80, 40)
        # left-hand rects
        self.color_grayscale_rect = pygame.Rect(
            self.color_window_rect.x+10, self.color_window_heading_rect.y+self.color_window_heading_rect.h+5, 260, 150)
        self.color_gradient_rect = pygame.Rect(
            self.color_window_rect.x+10, self.color_grayscale_rect.y+self.color_grayscale_rect.h+10, 260, 130)
        self.custom_gradient_rect = pygame.Rect(
            self.color_window_rect.x+10, self.color_gradient_rect.y+self.color_gradient_rect.h+10, 260, 110)
        # right hand rects
        self.color_mode = ColorMode(
            self.color_window_rect, self.color_window_heading_rect)
        self.color_mixer = ColorMixer(
            self.color_window_rect, self.color_mode.color_mode_rect)
        self.custom_color_rect = pygame.Rect(
            self.color_window_rect.x+self.color_window_rect.w-270, self.color_mixer.color_mixer_rect.y+self.color_mixer.color_mixer_rect.h+10, 260, 110)
        self.add_button()

    def get_index(self, name, btns):
        i = 0
        for button in btns:
            if (button.name == name):
                return i
            i += 1
        return -1

    def hsv_to_rgb(self, h, s, v):
        M = 255*v
        m = M*(1-s)
        z = (M-m) * (1 - abs(math.fmod(h/60.0, 2)-1))
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
        if h >= 300 and h <= 360:
            R = M
            G = m
            B = z + m

        return int(R), int(G), int(B)

    def add_button(self):
        self.buttons = []
        self.custom_colors_buttons = []
        self.custom_gradients_buttons = []
        self.buttons.append(Button(self.color_window_rect.w+self.color_window_rect.x-25, self.color_window_rect.y +
                            5, 20, 20, image_url="assets/color_window_exit.png", name="Exit_Color_Window"))
        self.buttons.append(Button(self.color_window_heading_rect.x+self.color_window_heading_rect.w/2, self.color_window_heading_rect.y,
                            self.color_window_heading_rect.w, self.color_window_heading_rect.h, text="COLOR PALLETE", text_color=self.text_color, shape="", pallete=True))
    # grayscale mode structure
        self.buttons.append(Button(self.color_grayscale_rect.x+35,
                            self.color_grayscale_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "GRAYSCALE", GRAY, pallete=True))

    # gradient mode structure
        self.buttons.append(Button(self.color_gradient_rect.x+28,
                            self.color_gradient_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "GRADIENT", GRAY, pallete=True))

    # gradient pallete
        self.buttons.append(Button(self.custom_gradient_rect.x+70,
                            self.custom_gradient_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "CUSTOM GRADIENTS", GRAY, pallete=True))
        self.custom_gradients_buttons.append(Button(self.custom_gradient_rect.x+8, self.custom_gradient_rect.y+40,
                                                    28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name="custom_gradient_1", isBorder=True))
        for i in range(1, 8):
            self.custom_gradients_buttons.append(Button(self.custom_gradient_rect.x+8+(i*3)+(28*(i)), self.custom_gradient_rect.y+40,
                                                        28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"custom_gradient_{i}", isBorder=True))
        self.custom_gradients_buttons.append(Button(self.custom_gradient_rect.x+8, self.custom_gradient_rect.y+75,
                                                    28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name="custom_gradient_9", isBorder=True))
        for i in range(9, 16):
            self.custom_gradients_buttons.append(Button(self.custom_gradient_rect.x+8+(3*(i-8))+(28*(i-8)), self.custom_gradient_rect.y+75,
                                                        28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"custom_gradient_{i}", isBorder=True))

    # color pallete
        self.buttons.append(Button(self.custom_color_rect.x+55,
                            self.custom_color_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "CUSTOM COLORS", GRAY, pallete=True))
        self.custom_colors_buttons.append(Button(self.custom_color_rect.x+8, self.custom_color_rect.y+40,
                                                 28, 28, AQUA, shape="ellipse", name="custom_color_1", isBorder=True))
        for i in range(1, 8):
            self.custom_colors_buttons.append(Button(self.custom_color_rect.x+8+(i*3)+(28*(i)), self.custom_color_rect.y+40,
                                                     28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"custom_color_{i+1}", isBorder=True))

        self.custom_colors_buttons.append(Button(self.custom_color_rect.x+8, self.custom_color_rect.y+75,
                                                 28, 28, RED, shape="ellipse", name="custom_color_9", isBorder=True))
        for i in range(9, 16):
            self.custom_colors_buttons.append(Button(self.custom_color_rect.x+8+(3*(i-8))+(28*(i-8)), self.custom_color_rect.y+75,
                                                     28, 28, BG_COLOR_PALLETE_WINDOW, shape="ellipse", name=f"custom_color_{i+1}", isBorder=True))

    def draw_buttons(self, win):
        self.color_mode.draw(win)
        self.color_mixer.draw(win)
        for button in self.buttons:
            button.draw(win)
        for button in self.custom_colors_buttons:
            button.draw(win)
        for button in self.custom_gradients_buttons:
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

    def preview_color(self, btns):
        rh = 0
        gs = 0
        bv = 0
        if btns[self.get_index("input_box_rh_input", btns)].text:
            rh = int(btns[self.get_index("input_box_rh_input", btns)].text)
        if btns[self.get_index("input_box_gs_input", btns)].text:
            gs = int(btns[self.get_index("input_box_gs_input", btns)].text)
        if btns[self.get_index("input_box_bv_input", btns)].text:
            bv = int(btns[self.get_index("input_box_bv_input", btns)].text)
        if not self.color_mode.isRGB:
            rh, gs, bv = self.hsv_to_rgb(rh, gs/100, bv/100)
        btns[(self.get_index("color_mode_preview_box", btns))].color = (rh, gs, bv)

    def mix_and_preview(self):
        print("mixing colors")
        color1_rh=0;color1_gs=0;color1_bv=0;color2_rh=0;color2_gs=0;color2_bv=0
        if self.color_mixer.buttons[self.get_index("input_box1_rh_input", self.color_mixer.buttons)].text:
            color1_rh = int(self.color_mixer.buttons[self.get_index(
                "input_box1_rh_input", self.color_mixer.buttons)].text)
        if self.color_mixer.buttons[self.get_index("input_box1_gs_input", self.color_mixer.buttons)].text:
            color1_gs = int(self.color_mixer.buttons[self.get_index(
                "input_box1_gs_input", self.color_mixer.buttons)].text)
        if self.color_mixer.buttons[self.get_index("input_box1_bv_input", self.color_mixer.buttons)].text:
            color1_bv = int(self.color_mixer.buttons[self.get_index(
                "input_box1_bv_input", self.color_mixer.buttons)].text)

        if self.color_mixer.buttons[self.get_index("input_box2_rh_input", self.color_mixer.buttons)].text:
            color2_rh = int(self.color_mixer.buttons[self.get_index(
                "input_box2_rh_input", self.color_mixer.buttons)].text)
        if self.color_mixer.buttons[self.get_index("input_box2_gs_input", self.color_mixer.buttons)].text:
            color2_gs = int(self.color_mixer.buttons[self.get_index(
                "input_box2_gs_input", self.color_mixer.buttons)].text)
        if self.color_mixer.buttons[self.get_index("input_box2_bv_input", self.color_mixer.buttons)].text:
            color2_bv = int(self.color_mixer.buttons[self.get_index(
                "input_box2_bv_input", self.color_mixer.buttons)].text)
        if not self.color_mixer.isRGB:
            color1_rh, color1_gs, color1_bv = self.hsv_to_rgb(
                color1_rh, color1_gs/100, color1_bv/100)
            color2_rh, color2_gs, color2_bv = self.hsv_to_rgb(
                color2_rh, color2_gs/100, color2_bv/100)

        color_rh = (color1_rh + color2_rh)/2
        color_gs = (color1_gs + color2_gs)/2
        color_bv = (color1_bv + color2_bv)/2

        self.color_mixer.buttons[(self.get_index(
            "color_mixer_preview_box", self.color_mixer.buttons))].color = (color_rh, color_gs, color_bv)

    def add_to_custom_gradients(self):
        print("added to custom gradients")

    def add_to_custom_color(self, btns,text):
        print("added to custom colors")
        print(self.custom_color_index)
        if self.custom_color_index > 15:
            print("zero")
            self.custom_color_index = 0
        color = btns[(self.get_index(text, btns))].color
        self.custom_colors_buttons[self.custom_color_index].color = color
        self.custom_color_index += 1

    def reset_mixer_inputs(self):
        self.color_mixer.buttons[self.get_index(
            "input_box1_rh_input", self.color_mixer.buttons)].text = ""
        self.color_mixer.buttons[self.get_index(
            "input_box1_gs_input", self.color_mixer.buttons)].text = ""
        self.color_mixer.buttons[self.get_index(
            "input_box1_bv_input", self.color_mixer.buttons)].text = ""
        self.color_mixer.buttons[self.get_index(
            "input_box2_rh_input", self.color_mixer.buttons)].text = ""
        self.color_mixer.buttons[self.get_index(
            "input_box2_gs_input", self.color_mixer.buttons)].text = ""
        self.color_mixer.buttons[self.get_index(
            "input_box2_bv_input", self.color_mixer.buttons)].text = ""

    def reset_color_mode_inputs(self):
        self.color_mode.buttons[self.get_index(
            "input_box_rh_input", self.color_mode.buttons)].text = ""
        self.color_mode.buttons[self.get_index(
            "input_box_gs_input", self.color_mode.buttons)].text = ""
        self.color_mode.buttons[self.get_index(
            "input_box_bv_input", self.color_mode.buttons)].text = ""

    def set_mode_text(self, buttons,t1,t2,t3):
        for btn in buttons:
            if (btn.name == "input_box_rh_text"):
                btn.text = t1
            elif (btn.name == "input_box_gs_text"):
                btn.text = t2
            elif (btn.name == "input_box_bv_text"):
                btn.text = t3

    def run(self, win):
        pygame.draw.rect(win, self.bg_color,
                         self.color_window_rect, border_radius=5)
        pygame.draw.rect(win, GRAY, (WIDTH/2-(self.width/2), HEIGHT/2-(self.height/2)-50,
                         self.width, 30), border_top_left_radius=5, border_top_right_radius=4)
        pygame.draw.rect(
            win, COLOR_PALLETE_RECT, self.color_grayscale_rect, border_radius=6)
        pygame.draw.rect(win, COLOR_PALLETE_RECT,
                         self.color_gradient_rect, border_radius=6)
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
                            continue
                        if button.name == "Exit_Color_Window":
                            running = False
                    for button in self.color_mode.buttons:
                        if not button.clicked(pos):
                            if (button.name == "input_box_rh_input" or button.name == "input_box_gs_input" or button.name == "input_box_bv_input") and button.input_box_selected:
                                button.input_box_selected = False
                                button.isBorder = False
                            continue
                        elif button.name == "toggle":
                            self.reset_color_mode_inputs()
                            if self.color_mode.isRGB:
                                button.image_url = "assets/rgb_toggle.png"
                                self.color_mode.isRGB = False
                                self.set_mode_text(self.color_mode.buttons,"Hue","Sat","Value")
                            elif not self.color_mode.isRGB:
                                button.image_url = "assets/hsv_toggle.png"
                                self.color_mode.isRGB = True
                                self.set_mode_text(self.color_mode.buttons,"Red","Green","Blue")

                        elif button.name == "input_box_rh_input" or button.name == "input_box_gs_input" or button.name == "input_box_bv_input":
                            button.isBorder = True
                            button.input_box_selected = True
                        elif button.name == "add_to_custom_colors":
                            self.add_to_custom_color(self.color_mode.buttons,"color_mode_preview_box")
                            self.reset_color_mode_inputs()

                    for button in self.color_mixer.buttons:
                        if not button.clicked(pos):
                            if (button.name == "input_box1_rh_input" or button.name == "input_box1_gs_input" or button.name == "input_box1_bv_input" or button.name == "input_box2_rh_input" or button.name == "input_box2_gs_input" or button.name == "input_box2_bv_input") and button.input_box_selected:
                                button.input_box_selected = False
                                button.isBorder = False
                            continue
                        elif button.name == "toggle":
                            self.reset_mixer_inputs()
                            if self.color_mixer.isRGB:
                                button.image_url = "assets/rgb_toggle.png"
                                self.color_mixer.isRGB = False
                                self.set_mode_text(self.color_mixer.buttons,"Hue","Sat","Value")
                            elif not self.color_mixer.isRGB:
                                button.image_url = "assets/hsv_toggle.png"
                                self.color_mixer.isRGB = True
                                self.set_mode_text(self.color_mixer.buttons,"Red","Green","Blue")

                        elif button.name == "input_box1_rh_input" or button.name == "input_box1_gs_input" or button.name == "input_box1_bv_input" or button.name == "input_box2_rh_input" or button.name == "input_box2_gs_input" or button.name == "input_box2_bv_input":
                            button.isBorder = True
                            button.input_box_selected = True
                        elif button.name == "add_to_custom_colors":
                            self.add_to_custom_color(self.color_mixer.buttons,"color_mixer_preview_box")
                            self.reset_mixer_inputs()

                if event.type == pygame.KEYDOWN:
                    for button in self.color_mode.buttons:
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
                                if self.color_mode.isRGB:
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
                                self.preview_color(self.color_mode.buttons)


                    for button in self.color_mixer.buttons:
                        if ((button.name == "input_box1_rh_input" or button.name == "input_box1_gs_input"or button.name == "input_box1_bv_input" or button.name == "input_box2_rh_input" or button.name == "input_box2_gs_input"or button.name == "input_box2_bv_input") and button.input_box_selected):
                            if event.key == pygame.K_BACKSPACE:
                                userInput = button.text
                                userInput = userInput[:-1]
                                button.text = userInput
                            elif (
                                event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9
                            ) and len(button.text) < 3:
                                userInput = button.text
                                userInput += event.unicode
                                if self.color_mixer.isRGB:
                                    if int(userInput) > 255:
                                        userInput = userInput[0:2]
                                else:
                                    if button.name == "input_box1_rh_input" or button.name == "input_box2_rh_input":
                                        if int(userInput) > 360:
                                            userInput = userInput[0:2]
                                    if (
                                        button.name == "input_box1_gs_input"
                                        or button.name == "input_box1_bv_input" or button.name == "input_box2_gs_input"
                                        or button.name == "input_box2_bv_input"
                                    ):
                                        if int(userInput) > 100:
                                            userInput = userInput[0:2]
                                button.text = userInput
                                self.mix_and_preview()
            self.draw_buttons(win)
