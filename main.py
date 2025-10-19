import pygame
pygame.init()
import random
import math
import time

width, height = 1920,1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Aim Training')

targets_increment = 500 #milliseconds
target_event = pygame.USEREVENT
target_padding = 30

bg_color = (66,98,102)

def mainloop():

    targets = []
    pygame.time.set_timer(target_event, targets_increment) #make a target every 500ms

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == target_event:
                x = random.randint(target_padding, width - target_padding)
                y = random.randint(target_padding, height - target_padding)
                target = Target(x, y)
    pygame.quit()

def drawing(win, targets):
    screen.fill((bg_color))
    for each_target in targets:
        each_target.draw(win)

    pygame.display.update()


class Target:
    maximumsize = 30
    pixelgrowth = 0.2
    targetcolour = "red"
    targetrings = "white"

    def __init__(self, x,y):
        self.x = x
        self.y = y #appearance point
        self.size = 0 #start
        self.grow = True #make false when max size

    def update(self):
        if self.size + self.pixelgrowth >= self.maximumsize: #if the last growth makes it too big, don't do it
            self.grow = False
        if self.grow:
            self.size += self.pixelgrowth #grow if it will not be max size
        else:
            self.size -= self.pixelgrowth #shrink at same rate

    def draw(self, win):
        pygame.draw.circle(win, self.targetcolour, (self.x, self.y),self.size)
        pygame.draw.circle(win, self.targetrings, (self.x, self.y),self.size * 0.8)
        pygame.draw.circle(win, self.targetcolour, (self.x, self.y),self.size * 0.6)
        pygame.draw.circle(win, self.targetrings, (self.x, self.y),self.size * 0.4)