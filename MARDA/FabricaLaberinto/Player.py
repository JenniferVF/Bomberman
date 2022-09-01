#Abstract product class to generate avatar

from abc import ABC, abstractmethod
import pygame
import os 

'''
MARDA class that allows to implement the functionalities and specific characteristics of specific maze games
'''
class Player(ABC):
    
	def __init__(self, position, init_x, init_y, init_speed, livesPlayer, imagePath, pos_x_image, pos_y_image, image_length, image_width):
		''' Construct a new Player object
			:param position: Position del Player in the view of game in pixels
			:param init_x: X coordinate Player in the view of game
			:param init_y: Y coordinate Player in the view of game
			:param init_speed: Initial movement speed of Player
			:param livesPlayer: Initial lives of Player
			:param imagePath: Avatar image
		'''
		self.x = init_x # 50
		self.y = init_y #50
		self.aux = 0
		self.lives = livesPlayer
		self.speed = init_speed
		self.left_move_activate = True # first check is with left move
		self.right_move_activate = False
		self.up_move_activate = False
		self.down_move_activate = False
		self.enable = True
		self.frame = 0
		self.sheet = pygame.image.load(os.path.join(os.path.dirname(__file__), imagePath))
		self.sheet.set_clip(pygame.Rect(pos_x_image, pos_y_image, image_length, image_width))
		self.image = self.sheet.subsurface(self.sheet.get_clip())
		self.rect = self.image.get_rect()
		self.rect.topleft = position

	''' To handle the movement at the right of the player. If the player reaches the limit of the screen 
	the program denied the movement'''
	@abstractmethod
	def moveRight(self):
		self.aux = self.x
		self.touch_border = False
		self.x = self.x + self.speed
		#print("Rigth X", self.x, " Y ", self.y)
		if self.x > 655:# watch out with this pixel, It needs testing 
			self.x = self.aux
			self.touch_border = True
			self.right_move_activate = False
			return self.right_move_activate
			#return False
		if self.touch_border == False:
			self.right_move_activate = self.checkPlayerMovement(1)
			return self.right_move_activate
			#return self.checkPlayerMovement(1)
		self.right_move_activate = True
		return self.right_move_activate
		#return True # if touch_border is true, we need to go back,
		#in this case to the left

	@abstractmethod
	def moveLeft(self):
		''' Move the BomberManAvatar character to the left '''
		self.aux = self.x
		self.touch_border = False
		self.x = self.x - self.speed
		#print("Left X", self.x, " Y ", self.y)
		if self.x < 50:
			self.x =self.aux
			self.touch_border = True
			self.left_move_activate = False
			return self.left_move_activate
			#return False # It can't keep in the same direction
		if self.touch_border == False:
			#two possibles results, but the main idea is the same
			# give in the comments of the returns
			self.left_move_activate = self.checkPlayerMovement(2)
			return self.left_move_activate
		self.left_move_activate = True
		return self.left_move_activate # It can keep in the same direction

		''' To handle the movement at the top of the player. If the player reaches the limit of the screen 
	the program denied the movement'''
	@abstractmethod
	def moveUp(self):
		self.aux = self.y
		self.touch_border = False
		self.y = self.y - self.speed
		#print("UP Y", self.y," X ", self.x)
		if self.y < 50:
			self.y = self.aux
			self.touch_border = True
			self.up_move_activate = False
			return self.up_move_activate
		if self.touch_border == False:
			self.up_move_activate = self.checkPlayerMovement(3)
			return self.up_move_activate
		self.up_move_activate = True
		return self.up_move_activate 


	''' To handle the movement at the bottom of the player. If the player reaches the limit of the screen 
	the program denied the movement'''
	@abstractmethod
	def moveDown(self):
		self.aux =self.y
		self.touch_border = False
		self.y = self.y + self.speed
		#print("Down Y ", self.y," X ", self.x)
		if self.y > 655:
			self.y = self.aux
			self.touch_border = True
			self.down_move_activate = False
			return self.down_move_activate
		if self.touch_border == False:
			self.down_move_activate = self.checkPlayerMovement(4)
			return self.down_move_activate
		self.down_move_activate = True
		return self.down_move_activate

	'''Method to handle the movement of the avatar or enemy. This method verifies if the next movement of the avatar
	collides with any blocking space occupied by any other element of the screen'''
	@abstractmethod
	def checkPlayerMovement(self, flag):
		pass

	@abstractmethod
	def restart(self, position, init_x, init_y):
		''' Reset the game settings for the BomberManAvatar 
			:param position: position of the BomberManAvatar character in the game view 
			:param init_x: X coordinate "BomberManAvatar" in the view of game
			:param init_y: Y coordinate "BomberManAvatar" in the view of game '''
		self.x = init_x # 50
		self.y = init_y #50
		self.rect.topleft = position
		self.lives = 3
