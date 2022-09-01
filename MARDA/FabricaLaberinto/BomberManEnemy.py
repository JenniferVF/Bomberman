#specific product class to create bomberman enemy

from Player import *
from random import seed
from random import randint
import pygame
import os.path

''' 
Class that implements the specific operation and characteristics of the character "BomberManEnemy" in the BomberMan game
'''
class BomberManEnemy(Player):
    
    def __init__(self, position, init_x, init_y, init_speed, livesPlayer, imagePath):
        ''' Construct a new "BomberManEnemy" object
			:param position: Position del "BomberManEnemy" in the view of game in pixels
			:param init_x: X coordinate "BomberManEnemy" in the view of game
			:param init_y: Y coordinate "BomberManEnemy" in the view of game
			:param init_speed: Initial movement speed of "BomberManEnemy"
			:param livesPlayer: Initial lives of "BomberManEnemy"
			:param imagePath: Avatar image
		'''
        super().__init__(position, init_x, init_y, init_speed, livesPlayer, imagePath, 90, 90, 45, 45 )
        self.left_states = { 0: (0, 90, 45, 45), 1: (45, 90, 45, 45), 2: (90, 90, 45, 45), 3: (135, 90, 45, 45) }
        self.right_states = { 0: (0, 45, 45, 45), 1: (45, 45, 45, 45), 2: (90, 45, 45, 45), 3: (135, 45, 45, 45) }
        self.up_states = { 0: (0, 135, 45, 45), 1: (45, 135, 45, 45), 2: (90, 135, 45, 45), 3: (135, 135, 45, 45) }
        self.down_states = { 0: (0, 0, 45, 45), 1: (45, 0, 45, 45), 2: (90, 0, 45, 45), 3: (135, 0, 45, 45) }
        self.direction = None
        self.diamonds_taken = 0

    def moveRight(self):
        ''' Move the BomberManEnemy character to the right '''
        return super().moveRight()

    def moveLeft(self):
        ''' Move the BomberManEnemy character to the left '''
        return super().moveLeft()

    def moveUp(self):
        ''' Move the BomberManEnemy character to the up '''
        return super().moveUp()

    def moveDown(self):
        ''' Move the BomberManEnemy character to the down '''
        return super().moveDown()

    def checkPlayerMovement(self, flag):
        ''' Check if the movement of the character "BomberManEnemy" is valid 
			:param flag: Indicates the direction in which the BomberManEnemy character will move '''
        self.state_of_return = True #1-It can keep moving in the same direction
        for element in (self.disable_block_list):
            if flag == 1: # movement to the rigth
                # We have to check the first pixel located in the avatar, that's the reason to sum 25 to 'y' 
                # (if the element is in the space of first range of a blocking element ) 
                # and the reason to sum 45 to x (if the sum is >= the avatar is in the space of a blocking element)
                if (
                    (self.y + 44 > element.first_range_y) 
                    and (self.y < element.second_range_y) 
                    and (self.x + 44 > element.first_range_x) 
                    and (self.x < element.second_range_x)
                ):
                    self.state_of_return = False # It knocks against an element
                    self.x = self.aux
            elif flag == 2: # movement to the left
                # be careful with the sum of 45, we need to add to considerer the edge of the block. 25 is the size of the avatar in pxls
                # that's why We must to check if the bottom of the avatar collides with the first range in 'y'
                if (
                    (self.y + 44 > element.first_range_y) 
                    and (self.y < element.second_range_y) 
                    and (self.x > element.first_range_x) 
                    and (self.x < element.second_range_x)
                ):
                    self.x = self.aux	
                    self.state_of_return = False # It knocks against an element
            elif flag == 3: # upward movement
                # be careful with the sum of 45, we need to add to considerer the edge of the block. 25 is the size of the avatar in pxls
                # that's why We must to check if the rigth side of the avatar collides with the first range in 'x'
                if (
                    (self.y > element.first_range_y) 
                    and (self.y < element.second_range_y) 
                    and (self.x + 44 > element.first_range_x) 
                    #and (self.x > element.first_range_x) 
                    and (self.x  < element.second_range_x)
                ):
                    self.y = self.aux	
                    self.state_of_return = False #It knocks against an element
            else: # downward movement 
                # Check the previous comment in the if statment with flag 1 
                if (
                    (self.y + 44 > element.first_range_y) 
                    and (self.y < element.second_range_y) 
                    and (self.x + 44 > element.first_range_x) 
                    and (self.x  < element.second_range_x)
                ):
                    self.state_of_return = False #It knocks against an element
                    self.y = self.aux
        return self.state_of_return

    def handle_direction(self):
        '''Randomly decide the direction the enemy character will take '''
        if(self.enable is True):
            self.direction_chosen_by_enemy()

    
    def direction_chosen_by_enemy(self):
        '''Method to verify the movements of the enemyes, this method use the
        movements moveLeft, moveRight, moveUp and moveDown also use recognizeTheMovement
        to check what kind of movement is available'''
        if (self.left_move_activate is True and self.right_move_activate is False and self.up_move_activate is False and self.down_move_activate is False):
            self.moveLeft()
            self.recognizeTheMovement(0)
            self.direction = "left"

        if (self.right_move_activate is True and self.left_move_activate is False and self.up_move_activate is False and self.down_move_activate is False):
            self.moveRight()
            self.recognizeTheMovement(1)# we activate the left movement
            self.direction = "right"

        if (self.up_move_activate is True and self.left_move_activate is False and self.right_move_activate is False and self.down_move_activate is False):
            self.moveUp()
            self.recognizeTheMovement(2)
            self.direction = "up"

        if (self.down_move_activate is True and self.left_move_activate is False and self.up_move_activate is False and self.right_move_activate is False):
            self.moveDown()
            self.recognizeTheMovement(3)
            self.direction = "down"

    
    def recognizeTheMovement(self, flag):
        '''This method works with flags each one check if is possible continue with
        the actual movement, if not is possible the programa select randomly what will be
        the next movement, after that when we have the new movement the next step is
        update de others boolean variables to avoid conflicts.
            :param flag: Indicates the direction in which the BomberManEnemy character will move '''
        if flag == 0:# left 
            if self.left_move_activate is True:
                self.right_move_activate = False
                self.up_move_activate = False
                self.down_move_activate = False
            else:#try to move at the rigth
                #self.right_move_activate = True
                randomDirection = self.generateRandomValue() 
                if randomDirection == 0:# take right direction	
                    #in case of activate only left movement
                    self.up_move_activate = False
                    self.down_move_activate = False
                    self.right_move_activate = True
                elif randomDirection == 1:# take upward direction
                    self.up_move_activate = True
                    self.down_move_activate = False
                    self.right_move_activate = False
                else:
                    self.up_move_activate = False
                    self.down_move_activate = True
                    self.right_move_activate = False
        elif flag == 1:	#to the right
            if self.right_move_activate is True:
                self.left_move_activate = False
                self.up_move_activate = False
                self.down_move_activate = False
            else:
            # self.left_move_activate = True
                randomDirection = self.generateRandomValue() 
                if randomDirection == 0:# take left direction	
                    #in case of activate only left movement
                    self.up_move_activate = False
                    self.down_move_activate = False
                    self.left_move_activate = True
                elif randomDirection == 1:# take upward direction
                    self.up_move_activate = True
                    self.down_move_activate = False
                    self.left_move_activate = False
                else:
                    self.up_move_activate = False
                    self.down_move_activate = True
                    self.left_move_activate = False

        elif flag == 2:# upward
            if self.up_move_activate is True:
                self.left_move_activate = False
                self.right_move_activate = False
                self.down_move_activate = False
            else:
                #self.down_move_activate = True
                randomDirection = self.generateRandomValue() 
                if randomDirection == 0:# take downward direction	
                    #in case of activate only left movement
                    self.left_move_activate = False
                    self.right_move_activate = False
                    self.down_move_activate = True	
                elif randomDirection == 1:# take left direction
                    self.left_move_activate = True
                    self.right_move_activate = False
                    self.down_move_activate = False
                else:
                    self.left_move_activate = False
                    self.right_move_activate = True
                    self.down_move_activate = False
        elif flag == 3: #downward
            if self.down_move_activate is True:
                    self.left_move_activate = False
                    self.right_move_activate = False
                    self.up_move_activate = False
            else:
                #self.up_move_activate = True
                randomDirection = self.generateRandomValue() 
                if randomDirection == 0:# take upward direction	
                    #in case of activate only left movement
                    self.right_move_activate = False
                    self.left_move_activate = False	
                    self.up_move_activate = True
                elif randomDirection == 1:# take left direction
                    self.right_move_activate = False
                    self.left_move_activate = True	
                    self.up_move_activate = False
                else: #take rigth direction
                    self.right_move_activate = True
                    self.left_move_activate = False	
                    self.up_move_activate = False

    
    def generateRandomValue(self):
        ''' Method to generate random numbers, we use them in the recognizeTheMovement method '''
        seed(None)
        return randint(0,2)

    def restart(self, position, init_x, init_y):
        ''' Reset the game settings for the BomberManEnemy
			:param position: position of the BomberManEnemy character in the game view 
			:param init_x: X coordinate "BomberManEnemy" in the view of game
			:param init_y: Y coordinate "BomberManEnemy" in the view of game '''
        self.diamonds_taken = 0
        super().restart(position, init_x, init_y)
