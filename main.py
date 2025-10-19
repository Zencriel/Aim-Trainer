import pygame
pygame.init()
import random
import math
import time

width, height = 1920,1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Aim Training')

def mainloop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break