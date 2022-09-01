#Abstract product class to generate weapons

from abc import ABC, abstractmethod
import pygame
import os

'''
MARDA class that allows to implement the specific weapons that the specific maze game possesses
'''
class Weapons(ABC):
    
    def __init__(self, position, imagePath, pos_x_image, pos_y_image, image_length, image_width): 
        ''' Construct a new "BomberManWeaponds" object '''  
        self.x = 0
        self.y = 0
        self.enable = True
        self.sheet = pygame.image.load(os.path.join(os.path.dirname(__file__), imagePath))
        self.sheet.set_clip(pygame.Rect(pos_x_image, pos_y_image, image_length, image_width))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0

    @abstractmethod
    def placeWeapons(self, x_position, y_position):
        ''' Place the bomb in the game's maze 
			:param init_x: X coordinate where place the bomb in the game's maze
			:param init_y: Y coordinate where place the bomb in the game's maze '''
        self.x = x_position
        self.y = y_position
        self.rect.x = x_position
        self.rect.y = y_position





