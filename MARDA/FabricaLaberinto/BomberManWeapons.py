#Specific product class to create BomberMan weapons

from Weapons import *
import pygame
import os.path
import time

'''
Class that implements the functionalities and characteristics of the specific weaponds of the BomberMan game
such as the bomb
'''
class BomberManWeapons(Weapons):

	def __init__(self, position, imagePath):
		''' Construct a new "BomberManWeaponds" object 
			:param position: position where to place the weapon (bomb) 
			:param imagePath: directory where the image of the bomb is located'''
		super().__init__(position, imagePath, 0, 0, 45, 45)
		self.bomb_in_screen = False
		self.now = 0
		self.wait = 0
		self.object = {  0: (0, 0, 45, 45), 1: (45, 0, 45, 45), 2: (90, 0, 45, 45), 3: (135, 0, 45, 45),
				4: (0, 0, 45, 45), 5: (45, 0, 45, 45), 6: (90, 0, 45, 45), 7: (135, 0, 45, 45),
				8: (0, 0, 45, 45), 9: (45, 0, 45, 45), 10: (90, 0, 45, 45), 11: (135, 0, 45, 45),
				12: (0, 0, 45, 45), 13: (45, 0, 45, 45), 14: (90, 0, 45, 45), 15: (135, 0, 45, 45),
				16: (0, 0, 45, 45), 17: (45, 0, 45, 45), 18: (90, 0, 45, 45), 19: (135, 0, 45, 45),
				20: (0, 0, 45, 45), 21: (45, 0, 45, 45), 22: (90, 0, 45, 45), 23: (135, 0, 45, 45),
				24: (0, 0, 45, 45), 25: (45, 0, 45, 45), 26: (90, 0, 45, 45), 27: (135, 0, 45, 45),
				28: (0, 0, 45, 45), 29: (45, 0, 45, 45), 30: (90, 0, 45, 45), 31: (135, 0, 45, 45),
				32: (0, 90, 45, 45), 33: (45, 90, 45, 45), 34: (90, 90, 45, 45), 35: (135, 90, 45, 45) }

	def placeWeapons(self, x_position, y_position):
		''' Place the bomb in the game's maze 
			:param init_x: X coordinate where place the bomb in the game's maze
			:param init_y: Y coordinate where place the bomb in the game's maze '''
		super().placeWeapons(x_position, y_position)

	
	def checkBombExplosion(self, maze):#object mazeBomberMan
		'''Method to check where the bomb gonna explode and what blocks will be destroyed. 
			:param maze: game's maze '''
		self.list_aux = []
		for i in maze.disable_block_list:
			if i.ocuppied == 2 or i.ocuppied == 4: #destructible block
				if (
					((i.first_range_x < (self.x + 94) <= i.second_range_x) and (i.first_range_y <= self.y < i.second_range_y)) 
					or # we need the next condition to consider the bottom edge of the bomb as a part of the explosion
					((i.first_range_x < (self.x + 94) <= i.second_range_x) and (i.first_range_y <= (self.y + 44) < i.second_range_y)) # we add to x pixel 44 to include every pixel of the bomb
					): # check to the rigth, 44 + 50, we must consider the first pxl, after that sum the next 44 and finally, we have to sum the 50 pxl (the range of explosion)
					maze.maze[i.index_in_maze] = 0
					self.list_aux.append(i.index_in_maze)
					
					if (i.ocuppied == 4):
						print("*** Llave encontrada ***")
						maze.key_reveal = True
						maze.key_time = time.time() + 2
						
				elif (
					((i.first_range_x <= (self.x - 50) < i.second_range_x) and (i.first_range_y < (self.y) < i.second_range_y)) 
					or # we need the next condition to consider the bottom edge of the bomb as a part of the explosion
					((i.first_range_x <= (self.x - 50) < i.second_range_x) and (i.first_range_y < (self.y + 44) < i.second_range_y))
					): # check to left
					maze.maze[i.index_in_maze] = 0
					self.list_aux.append(i.index_in_maze)
					
					if (i.ocuppied == 4):
						print("*** Llave encontrada ***")
						maze.key_reveal = True
						maze.key_time = time.time() + 2
						
				elif (
					((i.first_range_y <= (self.y - 50) < i.second_range_y) and (i.first_range_x <= self.x < i.second_range_x)) 
					or # we need the next condition to consider the front edge of the bomb as a part of the explosion
					((i.first_range_y <= (self.y - 50) < i.second_range_y) and (i.first_range_x <= (self.x + 44) < i.second_range_x))
					): # check upward
					maze.maze[i.index_in_maze] = 0
					self.list_aux.append(i.index_in_maze)
					
					if (i.ocuppied == 4):
						print("*** Llave encontrada ***")
						maze.key_reveal = True
						maze.key_time = time.time() + 2
						
				elif (
					((i.first_range_y < (self.y + 94) <= i.second_range_y) and(i.first_range_x < self.x < i.second_range_x)) 
					or # we need the next condition to consider the front edge of the bomb as a part of the explosion
					((i.first_range_y < (self.y + 94) <= i.second_range_y) and (i.first_range_x < (self.x + 44) < i.second_range_x))
					): # check downward
					maze.maze[i.index_in_maze] = 0
					self.list_aux.append(i.index_in_maze)
					
					if (i.ocuppied == 4):
						print("*** Llave encontrada ***")
						maze.key_reveal = True
						maze.key_time = time.time() + 2
						
		maze.updateInvalidPositions(self.list_aux)
		return maze.disable_block_list
		
	
	def explosionAgainstAvatar(self, x_enemy, y_enemy):
		''' Method to verify if an explosion touch some avatar in the screen
		We handle tthis event with the coordinates of the element bomb and the coordinates of the avatar
			:param init_x: X coordinate of enemy in the view of game
			:param init_y: Y coordinate of enemy in the view of game '''

		#check the rigth direction, we sum 44 + 50 as range of the explosion
		#and we check y_bomb between the borders of the y coordinates of the enemy to eliminate
		#if the enemy pixels collides with the bomb
		if ( (self.x <= x_enemy <= self.x + 94 ) and
		((y_enemy <= self.y <= y_enemy + 44 ) or (y_enemy <= self.y + 44 <= y_enemy + 44))
		):
			#print('Se elimina enemigo derecha')
			return False
		if (#check the left direction
		((self.x - 50 <= x_enemy + 44 <= self.x) or (self.x - 50 <= x_enemy <= self.x)) and
		((y_enemy <= self.y <= y_enemy + 44) or (y_enemy <= self.y + 44 <= y_enemy + 44))
		):
			#print('Se elimina enemigo izquier')
			return False
		if (# check downward
		(self.y + 44 <= y_enemy <= self.y + 94) and
		((x_enemy <= self.x <= x_enemy + 44) or (x_enemy <= self.x + 44 <= x_enemy + 44))
		):
			#print('Se elimina enemigo abajo')
			return False
		if (#check upward
		(self.y - 50  <= y_enemy + 44 <= self.y) and
		((x_enemy <= self.x <= x_enemy + 44) or (x_enemy <= self.x + 44 <= x_enemy + 44))
		):
			#print('Se elimina enemigo arriba')
			return False
		return True # is enable to keeping using
		


	def saveBombCoordinates(self, x_position, y_position):
		''' Stores the coordinates where the bomb is placed 
			:param init_x: X coordinate of enemy in the view of game
			:param init_y: Y coordinate of enemy in the view of game '''
		self.x = x_position
		self.y = y_position
		self.rect.x = x_position
		self.rect.y = y_position
		self.now = time.time() # take current time at the moment to put the bomb
		self.wait = self.now + 3

	def checkBombStatus(self, mazeBomberMan, list_of_enemies, avatarBomberMan, sounds): #mazeBomberMan
		''' Check the scope of the bomb explosion 
			:param mazeBomberMan: game´s maze
			:param list_of_enemies: list with information about the enemies in the game 
			:param avatarBomberMan: information about the location of the bomberman in the game
			:param sounds: sounds to use '''
		if self.wait > time.time():
			#super().placeWeapons(self.x , self.y)
			return True
		else:
			self.checkBombExplosion(mazeBomberMan) # check explosion against blocks
			for i in list_of_enemies: # check explosion against enemies
				if i.enable is True:
					i.enable = self.explosionAgainstAvatar(i.x, i.y)
			if (#to check if the explosion is near of the bomberman, false means the bomberman is unavailable, so he touched the epxlotion
				self.explosionAgainstAvatar(avatarBomberMan.x, avatarBomberMan.y) is False
			):
				avatarBomberMan.x = 50
				avatarBomberMan.y = 50
				avatarBomberMan.rect.x = 50
				avatarBomberMan.rect.y = 50
				avatarBomberMan.lives = avatarBomberMan.lives - 1 #The bomberman lost lives
			sounds.play_explosion_sound()
			self.bomb_in_screen = False
			return False