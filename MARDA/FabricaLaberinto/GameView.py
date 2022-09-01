
import pygame
import os.path

from abc import ABC, abstractmethod

'''
MARDA class showing game menu screen
'''
class GameView(ABC):
    
    pygame.init()

    def __init__(self,  windowWidth, windowHeight):
        ''' Construct a new GameView object 
            :param windowWidth: width of screen game
            :param windowHeight: Height of screen game '''
        self.background = None
        self.font = None
        self.image = None
        self._display_surf = pygame.display.set_mode( (windowWidth, windowHeight) , pygame.HWSURFACE )

    @abstractmethod
    def setBackgroundImage(self, imagePath ):
        ''' Set the background image of the game
            :param imagePath: path of directory where the image is located '''
        self.background = pygame.image.load(imagePath).convert()
        self._display_surf.blit(self.background,(0,0) )

    @abstractmethod
    def showConsole(self, posX1, posY1, posX2, posY2, consoleColor, frameColor):
        ''' Displays the game tool information console
            :param posX1: x coordinate 1 where the console will be placed
            :param posXY1: y coordinate 1 where the console will be placed
            :param posX2: x coordinate 2 where the console will be placed
            :param posY2: y coordinate 2 where the console will be placed
            :param consoleColor: console's color
            :param frameColor: frame's color '''
        pygame.draw.rect(self._display_surf, frameColor, (posX1,posY1,posX2,posY2))
        pygame.draw.rect(self._display_surf, consoleColor, (posX1+5,posY1+5,posX2-10,posY2-10))

    
    @abstractmethod
    def drawElementInScreen(self,imagePath, x_coordinate,y_coordinate):
        '''Method to get the path of the image and print it in the screen
           :param imagePath: path of directory where the image is located
           :param x_coordinate: X coordinate where the element will be placed
           :param y_coordinate: Y coordinate where the element will be placed '''
        self.imageOfElement = pygame.image.load(imagePath).convert_alpha()
        self._display_surf.blit(self.imageOfElement,(x_coordinate,y_coordinate))
    
    @abstractmethod
    def drawTextInScreen(self, text, x_coordinate,y_coordinate):
        '''Method to print text in the screen
           :param text: text to print
           :param x_coordinate: X coordinate where thetext will be placed
           :param y_coordinate: Y coordinate where the text will be placed '''
        self._display_surf.blit(text,(x_coordinate,y_coordinate))

    @abstractmethod
    def clean_up(self):
        ''' Refresh the screen '''
        pygame.display.update()

    @abstractmethod
    def drawPlayer(self, player):
        ''' Draw the player on the game screen 
            :param player: game's player'''
        if player.enable is True:
            self._display_surf.blit(player.image , player.rect)

    @abstractmethod
    def get_frame(self, frame_set, player):
        ''' Get the frame '''
        player.frame += 1
        if player.frame > (len(frame_set) - 1):
            player.frame = 0
        return frame_set[player.frame]

    @abstractmethod
    def clip(self, clipped_rect, player):
        if type(clipped_rect) is dict:
            player.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect, player)))
        else:
            player.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    @abstractmethod
    def update(self, direction, player):
        ''' Update the player's position on the game screen 
            :param direction: player's direction
            :param player: game's player'''
        if player.enable is True:
            if direction == 'left':
                self.clip(player.left_states, player)            
                player.rect.x = player.x
            if direction == 'right':
                self.clip(player.right_states, player)
                player.rect.x = player.x
            if direction == 'up':
                self.clip(player.up_states, player)
                player.rect.y = player.y
            if direction == 'down':
                self.clip(player.down_states, player)
                player.rect.y = player.y

            if direction == 'stand_left':
                self.clip(player.left_states[0], player)
            if direction == 'stand_right':
                self.clip(player.right_states[0], player)
            if direction == 'stand_up':
                self.clip(player.up_states[0], player)
            if direction == 'stand_down':
                self.clip(player.down_states[0], player)

            player.image = player.sheet.subsurface(player.sheet.get_clip())
        else: 
            pass

    @abstractmethod
    def handle_event(self, event, player ):
        ''' Make the player move by clicking a key 
            :param event: event occurred
            :param player: game's player '''
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.update('left', player)
            if event.key == pygame.K_RIGHT:
                self.update('right', player)
            if event.key == pygame.K_UP:
                self.update('up', player)
            if event.key == pygame.K_DOWN:
                self.update('down', player)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left', player)
            if event.key == pygame.K_RIGHT:
                self.update('stand_right', player)
            if event.key == pygame.K_UP:
                self.update('stand_up', player)
            if event.key == pygame.K_DOWN:
                self.update('stand_down', player)

    '''Update the position by collision with enemy'''
    @abstractmethod
    def simple_update(self, x, y):
        ''' simple update of coordinates 
            :param x: x coordinate
            :param y: y coordinate '''
        self.rect.x = x
        self.rect.y = y

    
    @abstractmethod
    def updateObject(self, object):    
        '''methods used to animate sprites that do not move in X and Y directions
            :param player: player to animate '''    
        self.clip(object.object, object)       
        object.image = object.sheet.subsurface(object.sheet.get_clip())

    @abstractmethod
    def positionObject(self, pos, object):
        ''' method that positions an object on the screen 
            :param pos: object's position
            :param object: object to place '''
        object.rect.topleft = pos

    @abstractmethod
    def setFrameObject(self, object):
        ''' Set of frame of object
            :param object: object '''
        object.frame = 0

    @abstractmethod        
    def gameWin(self):
        ''' Displays the victory screen upon winning the game '''
        pass

    @abstractmethod        
    def gameOver(self):
        ''' Displays the Game Over screen the game '''
        pass