
import pygame
import os.path

from abc import ABC, abstractmethod

'''
MARDA class showing game menu screen
'''
class GameMenuView(ABC):

    pygame.init()

    def __init__(self,  windowWidth, windowHeight):
        ''' Construct a new GameMenuView object 
            :param windowWidth: width of screen game
            :param windowHeight: Height of screen game '''
        self.backgroundMenu = None
        self.font = None
        self.image = None
        self.display_surf = pygame.display.set_mode( (windowWidth, windowHeight) , pygame.HWSURFACE )

    @abstractmethod
    def gameStart(self, size, imagePath):
        ''' Displays the initial game screen (menu screen) 
            :param size: size of screen
            :param imagePath: path of directory where the image is located '''
        self.font = pygame.font.Font( None, size)
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), imagePath)) 

    @abstractmethod
    def rules(self, sizeFont, sysFontType, imagePath):
        ''' Displays the games's rules (rules screen) 
            :param sizeFont: size of screen
            :param sysFontType: Font's type of screen
            :param imagePath: path of directory where the image is located '''
        self.font	= pygame.font.SysFont(sysFontType, sizeFont)
        self.image  = pygame.image.load(os.path.join(os.path.dirname(__file__), imagePath))


