import pygame
from Player import *

class Enemy(Player, pygame.sprite.Sprite):
    #this constructor has position as an argument, is like a tuple. We need this for the rect objet of pygame
    #x and y to the validate the movements in Player class
    #speed: speed of the movement
    #init_used: to recognize the type of object initialized
    def __init__(self, position, x, y, speed, init_used):
        super().__init__(x, y, speed, init_used) # watch out here
        self.sheet = pygame.image.load('img/enemy.png')
        self.sheet.set_clip(pygame.Rect(90, 0, 45, 45))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 0: (0, 90, 45, 45), 1: (45, 90, 45, 45), 2: (90, 90, 45, 45), 3: (135, 90, 45, 45) }
        self.right_states = { 0: (0, 45, 45, 45), 1: (45, 45, 45, 45), 2: (90, 45, 45, 45), 3: (135, 45, 45, 45) }
        self.up_states = { 0: (0, 135, 45, 45), 1: (45, 135, 45, 45), 2: (90, 135, 45, 45), 3: (135, 135, 45, 45) }
        self.down_states = { 0: (0, 0, 45, 45), 1: (45, 0, 45, 45), 2: (90, 0, 45, 45), 3: (135, 0, 45, 45) }
        self.enable = True #if the enemy is enable in the screen
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction, x, y):
        if direction == 'left':
            self.clip(self.left_states)            
            #self.rect.x -= 5 #super().moveLeft()
            self.rect.x = x
        if direction == 'right':
            self.clip(self.right_states)
            #self.rect.x += 5 #super().moveRight()
            self.rect.x = x
        if direction == 'up':
            self.clip(self.up_states)
            #self.rect.y -= 5 #super().moveUp()
            self.rect.y = y
        if direction == 'down':
            self.clip(self.down_states)
            #self.rect.y += 5 #super().moveDown()
            self.rect.y = y

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())
