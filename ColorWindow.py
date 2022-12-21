import pygame
from utils import *


class ColorWindow:
    def __init__(self,theme):
        self.theme=theme
        self.bg_color = BG_COLOR_PALLETE_WINDOW
        self.text_color = DARKGRAY
        self.isRGB = True
        self.height = 500
        self.width = 550
        self.color_window_rect = pygame.Rect(
            WIDTH/2-(self.width/2), HEIGHT/2-(self.height/2)-50, self.width, self.height)
        self.color_window_heading_rect = pygame.Rect(
            WIDTH/2-80, self.color_window_rect.x+65, 80, 40)
            #left-hand tools
        self.color_grayscale_rect = pygame.Rect(
            WIDTH/2-(self.width/2)+20, self.color_window_heading_rect.y+self.color_window_heading_rect.h+5, 276, 103)
        self.color_gradient_rect = pygame.Rect(
            WIDTH/2-(self.width/2)+20, self.color_grayscale_rect.y+self.color_grayscale_rect.h+10, 255, 132)
        self.custom_gradient_rect = pygame.Rect(
            WIDTH/2-(self.width/2)+20, self.color_gradient_rect.y+self.color_gradient_rect.h+10, 230, 96)
            #right hand tools
        self.color_mode_rect = pygame.Rect(WIDTH/2-(self.width/2)+self.color_grayscale_rect.w+50,
            self.color_window_heading_rect.y+self.color_window_heading_rect.h+5, 197, 106)
        self.color_mixer_rect = pygame.Rect(
            WIDTH/2-(self.width/2)+self.color_gradient_rect.w+50, self.color_mode_rect.y+self.color_mode_rect.h+10, 224, 132)
        self.custom_color_rect = pygame.Rect(
            WIDTH/2-(self.width/2)+self.custom_gradient_rect.w+50, self.color_mixer_rect.y+self.color_mixer_rect.h+10, 256, 95)

        #rgb/hsv input box rects
        # self.r_h_input1_rect = pygame.Rect(self.color_mode_rect.x)
        self.add_button()

    def add_button(self):
        self.buttons = []
        self.buttons.append(Button(self.color_window_rect.w+self.color_window_rect.x-25, self.color_window_rect.y +
                            5, 20, 20, image_url="assets/color_window_exit.png", name="Exit_Color_Window"))
        self.buttons.append(Button(self.color_window_heading_rect.x+self.color_window_heading_rect.w/2, self.color_window_heading_rect.y,
                            self.color_window_heading_rect.w, self.color_window_heading_rect.h, text="COLOR PALLETE", text_color=self.text_color, shape="", pallete=True))

    #color mode parts
        self.buttons.append(Button(self.color_mode_rect.x+5,self.color_mode_rect.y+5,50,20,WHITE,"MODE",GRAY))
        if self.isRGB:
            self.buttons.append(Button(self.color_mode_rect.x+self.color_mode_rect.w-51,self.color_mode_rect.y+5,46,18,image_url="assets/hsv_toggle.png", name="toggle"))                    
        else:
            self.buttons.append(Button(self.color_mode_rect.x+self.color_mode_rect.w-51,self.color_mode_rect.y+5,46,18,image_url="assets/rgb_toggle.png", name="toggle"))
        #input box 1
        self.buttons.append(Button(self.color_mode_rect.x+5,self.color_mode_rect.y+5+18,60,20,GRAY,shape="rectangle",name="input_box_rh_text"))                    
        self.buttons.append(Button(self.color_mode_rect.x+5,self.color_mode_rect.y+5+18,60,20,GRAY,shape="rectangle",name="input_box_rh"))
         #input box 2
        self.buttons.append(Button(self.color_mode_rect.x+5,self.color_mode_rect.y+5+18,60,20,GRAY,shape="rectangle",name="input_box_gs_text"))                    
        self.buttons.append(Button(self.color_mode_rect.x+5,self.color_mode_rect.y+5+18,60,20,GRAY,shape="rectangle",name="input_box_gs"))
         #input box 3
        self.buttons.append(Button(self.color_mode_rect.x+5,self.color_mode_rect.y+5+18,60,20,GRAY,shape="rectangle",name="input_box_bv_text"))                    
        self.buttons.append(Button(self.color_mode_rect.x+5,self.color_mode_rect.y+5+18,60,20,GRAY,shape="rectangle",name="input_box_bv"))

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

    def run(self, win):
        pygame.draw.rect(win, self.bg_color,
                         self.color_window_rect, border_radius=5)
        pygame.draw.rect(win, GRAY, (WIDTH/2-(self.width/2), HEIGHT/2-(self.height/2)-50,
                         self.width, 30), border_top_left_radius=5, border_top_right_radius=4)
        # pygame.draw.rect(win,WHITE,self.color_window_heading_rect,border_radius=4)
        pygame.draw.rect(
            win, WHITE, self.color_grayscale_rect, border_radius=4)
        pygame.draw.rect(win, WHITE, self.color_mode_rect, border_radius=4)
        pygame.draw.rect(win, WHITE, self.color_gradient_rect, border_radius=4)
        pygame.draw.rect(win, WHITE, self.color_mixer_rect, border_radius=4)
        pygame.draw.rect(win, WHITE, self.custom_color_rect, border_radius=4)
        pygame.draw.rect(
            win, WHITE, self.custom_gradient_rect, border_radius=4)

        self.draw_buttons(win)
        running = True
        while running:
            if(self.theme.getMode() == "dark"):
                self.bg_color = DARKGRAY
                self.text_color = BG_COLOR_PALLETE_WINDOW
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
                            running= False


            
