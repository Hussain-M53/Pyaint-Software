from turtle import pos
from .settings import *

class Button:
    def __init__(self, x, y, width, height, color = (0, 0, 0), text="", text_color=BLACK, shape = "rectangle", image_url = "/", name=None,pallete =False,isBorder=False,isBorderRadius=False,borderRadius =2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.shape = shape
        self.text_color = text_color
        self.image_url = image_url
        self.name = name
        self.border_color = DARKGRAY
        self.isPallete = pallete
        self.isBorder=isBorder
        self.borderRadius=borderRadius
        self.isBorderRadius=isBorderRadius
        self.input_box_selected=False

    def draw(self, win):
        # Draws button with an image
        if self.image_url != "/":
            my_image = pygame.image.load(self.image_url)
            my_image = pygame.transform.scale(my_image, (self.width, self.height))
            win.blit(my_image, (self.x,self.y))
         

        elif self.shape == "rectangle":
            if self.isBorderRadius:     
                pygame.draw.rect(win, self.color,(self.x, self.y, self.width, self.height),border_radius = self.borderRadius)
            else:
                pygame.draw.rect(win, self.color,(self.x, self.y, self.width, self.height))
            if self.isBorder:
                pygame.draw.rect(win, BLACK,(self.x, self.y, self.width, self.height), 2)
        
        elif self.shape == "ellipse":
            pygame.draw.ellipse(win, self.color, (self.x, self.y, self.width, self.height)) #fill
            if self.isBorder:
                pygame.draw.ellipse(win, BLACK, (self.x, self.y, self.width, self.height), 2) #border

        if self.text:
            button_font = get_font(int(self.width/2) - 6,self.isPallete)
            text_surface = button_font.render(self.text, 1, self.text_color)
            win.blit(text_surface, (self.x + self.width/2 - text_surface.get_width()/2, self.y + self.height/2 - text_surface.get_height()/2))

    def clicked(self, pos):
        x, y = pos
        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False

        return True

    def hover(self, pos):
        x, y = pos
        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False

        return True