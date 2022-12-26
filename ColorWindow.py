import math
import pygame
from Gradient import Gradient
from Grayscale import Grayscale
from utils import *
from ColorMode import ColorMode
from ColorMixer import ColorMixer


class ColorWindow:
    def __init__(self, theme):
        self.theme = theme
        self.custom_color_index = 1
        self.custom_gradient_index = -1
        self.stretch = False
        self.color_gradient_image = pygame.image.load(
            "assets/color_gradient.png")
        self.bg_color = BG_COLOR_PALLETE_WINDOW
        self.text_color = GRAY
        self.height = 520
        self.width = 550
        self.color_window_rect = pygame.Rect(
            WIDTH/2-(self.width/2), HEIGHT/2-(self.height/2)-50, self.width, self.height)
        self.color_window_heading_rect = pygame.Rect(
            WIDTH/2-80, self.color_window_rect.x+55, 80, 40)
        # left-hand rects
        self.grayscale = Grayscale(
            self.color_window_rect, self.color_window_heading_rect)
        self.gradient = Gradient(
            self.color_window_rect, self.grayscale.color_grayscale_rect)
        self.custom_gradient_rect = pygame.Rect(
            self.color_window_rect.x+10, self.gradient.color_gradient_rect.y+self.gradient.color_gradient_rect.h+10, 260, 110)
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
            if button.name == name:
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
        self.custom_grayscale_buttons = []
        self.buttons.append(Button(self.color_window_rect.w+self.color_window_rect.x-25, self.color_window_rect.y +
                            5, 20, 20, image_url="assets/color_window_exit.png", name="Exit_Color_Window"))
    # gradient pallete
        self.buttons.append(Button(self.custom_gradient_rect.x+70,
                            self.custom_gradient_rect.y+10, 60, 20, COLOR_PALLETE_RECT, "CUSTOM GRADIENTS", GRAY, pallete=True))

        self.custom_gradients_buttons.append(Button(self.custom_gradient_rect.x+8, self.custom_gradient_rect.y+40,
                                                    28, 28, BG_COLOR_PALLETE_WINDOW, shape="rectangle", name="custom_gradient_1", isBorder=True))
        for i in range(1, 8):
            self.custom_gradients_buttons.append(Button(self.custom_gradient_rect.x+8+(i*3)+(28*(i)), self.custom_gradient_rect.y+40,
                                                        28, 28, BG_COLOR_PALLETE_WINDOW, shape="rectangle", name=f"custom_gradient_{i}", isBorder=True))

        self.custom_gradients_buttons.append(Button(self.custom_gradient_rect.x+8, self.custom_gradient_rect.y+75,
                                                    28, 28, BG_COLOR_PALLETE_WINDOW, shape="rectangle", name="custom_gradient_9", isBorder=True))
        for i in range(9, 16):
            self.custom_gradients_buttons.append(Button(self.custom_gradient_rect.x+8+(3*(i-8))+(28*(i-8)), self.custom_gradient_rect.y+75,
                                                        28, 28, BG_COLOR_PALLETE_WINDOW, shape="rectangle", name=f"custom_gradient_{i}", isBorder=True))

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
        self.gradient.draw(win)
        self.grayscale.draw(win)
        if self.stretch:
            self.gradient.stretchGradient(win, self.gradient.grad_color)
        for button in self.buttons:
            button.draw(win)
        for button in self.custom_colors_buttons:
            button.draw(win)
        for button in self.custom_gradients_buttons:
            button.draw(win)
        for button in self.custom_grayscale_buttons:
            button.draw(win)
        if self.gradient.added_to_custom_grad:
            self.gradient.stretchCustomGradient(win, self.gradient.grad_color, self.custom_gradient_index)
            self.gradient.added_to_custom_grad = False
        self.gradient.drawRect(win)

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
        if not self.color_mode.mode.isRGB:
            rh, gs, bv = self.hsv_to_rgb(rh, gs/100, bv/100)
        btns[(self.get_index("color_mode_preview_box", btns))].color = (rh, gs, bv)

    def mix_and_preview(self):
        print("mixing colors")
        color1_rh = 0
        color1_gs = 0
        color1_bv = 0
        color2_rh = 0
        color2_gs = 0
        color2_bv = 0
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
        if not self.color_mixer.mode.isRGB:
            color1_rh, color1_gs, color1_bv = self.hsv_to_rgb(
                color1_rh, color1_gs/100, color1_bv/100)
            color2_rh, color2_gs, color2_bv = self.hsv_to_rgb(
                color2_rh, color2_gs/100, color2_bv/100)

        color_rh = (color1_rh + color2_rh)/2
        color_gs = (color1_gs + color2_gs)/2
        color_bv = (color1_bv + color2_bv)/2

        self.color_mixer.buttons[(self.get_index(
            "color_mixer_preview_box", self.color_mixer.buttons))].color = (color_rh, color_gs, color_bv)


    def add_to_custom_gradients(self, color):

        if self.custom_gradient_index > 15:
            self.custom_gradient_index = 0

        print("Added to Custom Gradients")
        self.custom_gradient_index += 1

    def add_to_custom_color(self, btns, text):
        if self.custom_color_index > 15:
            self.custom_color_index = 0
        color = btns[(self.get_index(text, btns))].color
        if color == (248, 245, 245):
            return
        print("Added to Custom Colors")
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

    def run(self, win):

        if self.theme.getMode() == "dark":
            self.bg_color = DARKGRAY
        else:
            self.bg_color = BG_COLOR_PALLETE_WINDOW
            
        pygame.draw.rect(win, self.bg_color,
                         self.color_window_rect, border_radius=5)
        pygame.draw.rect(win, GRAY, (WIDTH/2-(self.width/2), HEIGHT/2-(self.height/2)-50,
                         self.width, 30), border_top_left_radius=5, border_top_right_radius=5)
        pygame.draw.rect(win, COLOR_PALLETE_RECT,
                         self.custom_color_rect, border_radius=6)
        pygame.draw.rect(
            win, COLOR_PALLETE_RECT, self.custom_gradient_rect, border_radius=4)

        text_surface = pygame.font.SysFont('Georgia', 30,bold=True).render("Color Palette", 1, RED)
        win.blit(text_surface, (
            self.color_window_heading_rect.x + self.color_window_heading_rect.w / 2 - 50,
            self.color_window_heading_rect.y))

        running = True
        while running:
            pygame.display.update()
            # for loop through the event queue
            for event in pygame.event.get():
                # Check for QUIT event
                if event.type == pygame.QUIT:  # if user closed the program
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the mouse position
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Get the color of the pixel at the mouse position
                    if mouse_x > 43 and mouse_x < 162 and mouse_y > 325 and mouse_y < 405:
                        color = win.get_at((mouse_x, mouse_y))
                        self.gradient.grad_color = color
                        self.stretch = True

                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos[0], event.pos[1]
                    if x > self.grayscale.color_grayscale_rect.x+10 and x < self.grayscale.color_grayscale_rect.x + 140 and y > self.grayscale.color_grayscale_rect.y+40 and y < self.grayscale.color_grayscale_rect.y + 70:
                        self.grayscale.set_slider(win)
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
                            if self.color_mode.mode.isRGB:
                                button.image_url = "assets/rgb_toggle.png"
                                self.color_mode.mode.isRGB = False
                                self.color_mode.mode.set_mode_text(
                                    self.color_mode.buttons, "Hue", "Sat", "Value")
                            else:
                                button.image_url = "assets/hsv_toggle.png"
                                self.color_mode.mode.isRGB = True
                                self.color_mode.mode.set_mode_text(
                                    self.color_mode.buttons, "Red", "Green", "Blue")

                        elif button.name == "input_box_rh_input" or button.name == "input_box_gs_input" or button.name == "input_box_bv_input":
                            button.isBorder = True
                            button.input_box_selected = True
                        elif button.name == "add_to_custom_colors":
                            self.add_to_custom_color(
                                self.color_mode.buttons, "color_mode_preview_box")
                            self.reset_color_mode_inputs()

                    for button in self.gradient.buttons:
                        if not button.clicked(pos):
                            if (button.name == "gradient_input_box_input") and button.input_box_selected:
                                button.input_box_selected = False
                                button.isBorder = False
                            continue
                        elif button.name == "gradient_input_box_input":
                            button.isBorder = True
                            button.input_box_selected = True
                        elif button.name == "add_to_custom_gradient":
                            try:
                                self.add_to_custom_gradients(color)
                                self.gradient.added_to_custom_grad = True
                            except:
                                print("Choose Color First")


                    for button in self.color_mixer.buttons:
                        if not button.clicked(pos):
                            if (button.name == "input_box1_rh_input" or button.name == "input_box1_gs_input" or button.name == "input_box1_bv_input" or button.name == "input_box2_rh_input" or button.name == "input_box2_gs_input" or button.name == "input_box2_bv_input") and button.input_box_selected:
                                button.input_box_selected = False
                                button.isBorder = False
                            continue
                        elif button.name == "toggle":
                            self.reset_mixer_inputs()
                            if self.color_mixer.mode.isRGB:
                                button.image_url = "assets/rgb_toggle.png"
                                self.color_mixer.mode.isRGB = False
                                self.color_mixer.mode.set_mode_text(
                                    self.color_mixer.buttons, "Hue", "Sat", "Value")
                            else:
                                button.image_url = "assets/hsv_toggle.png"
                                self.color_mixer.mode.isRGB = True
                                self.color_mixer.mode.set_mode_text(
                                    self.color_mixer.buttons, "Red", "Green", "Blue")

                        elif button.name == "input_box1_rh_input" or button.name == "input_box1_gs_input" or button.name == "input_box1_bv_input" or button.name == "input_box2_rh_input" or button.name == "input_box2_gs_input" or button.name == "input_box2_bv_input":
                            button.isBorder = True
                            button.input_box_selected = True
                        elif button.name == "add_to_custom_colors":
                            self.add_to_custom_color(
                                self.color_mixer.buttons, "color_mixer_preview_box")
                            self.reset_mixer_inputs()
                    for button in self.grayscale.buttons:
                        if not button.clicked(pos):
                            continue
                        if button.name  == "add_to_grayscale_colors":
                            self.grayscale.add_to_grayscale_color()

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
                                if self.color_mode.mode.isRGB:
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

                    for button in self.gradient.buttons:
                        if button.name == "gradient_input_box_input":
                            if event.key == pygame.K_BACKSPACE:
                                userInput = button.text
                                userInput = userInput[:-1]
                                button.text = userInput
                            elif (
                                event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9
                            ) and len(button.text) < 3:
                                userInput = button.text
                                userInput += event.unicode
                                if int(userInput) > 100:
                                    userInput = userInput[0:2]
                                button.text = userInput
                                opacity = button.text

                    for button in self.color_mixer.buttons:
                        if ((button.name == "input_box1_rh_input" or button.name == "input_box1_gs_input" or button.name == "input_box1_bv_input" or button.name == "input_box2_rh_input" or button.name == "input_box2_gs_input" or button.name == "input_box2_bv_input") and button.input_box_selected):
                            if event.key == pygame.K_BACKSPACE:
                                userInput = button.text
                                userInput = userInput[:-1]
                                button.text = userInput
                            elif (
                                event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9
                            ) and len(button.text) < 3:
                                userInput = button.text
                                userInput += event.unicode
                                if self.color_mixer.mode.isRGB:
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
