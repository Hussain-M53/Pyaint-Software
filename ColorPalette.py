import pygame
from utils import *

class ColorPalette:
    def __init__(self):
        self.height = 350
        self.width = 300

    def run(self):
        pygame.display.set_caption("ColorPalette")
        screen2 = pygame.display.set_mode((300, 350))
        screen2.fill(BLACK)
        pygame.display.update()      
        running = True
        while running:
            # for loop through the event queue
            for event in pygame.event.get():
                # Check for QUIT event
                if event.type == pygame.QUIT:
                    running = False 