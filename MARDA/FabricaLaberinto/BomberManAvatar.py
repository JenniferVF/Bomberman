#specific product class to create bomberman avatar

from Player import *
import pygame
import os.path

''' 
Class that implements the specific operation and characteristics of the character "BomberMan" in the BomberMan game
'''
class BomberManAvatar(Player):
	
	def __init__(self, position, init_x, init_y, init_speed, livesPlayer, imagePath):
		''' Construct a new "BomberManAvatar" object
			:param position: Position del "BomberManAvatar" in the view of game in pixels
			:param init_x: X coordinate "BomberManAvatar" in the view of game
			:param init_y: Y coordinate "BomberManAvatar" in the view of game
			:param init_speed: Initial movement speed of "BomberManAvatar"
			:param livesPlayer: Initial lives of "BomberManAvatar"
			:param imagePath: Avatar image
		'''
		super().__init__(position, init_x, init_y, init_speed, livesPlayer, imagePath, 90, 90, 45, 45)
		self.left_states = { 0: (0, 45, 45, 45), 1: (45, 45, 45, 45), 2: (90, 45, 45, 45) }
		self.right_states = { 0: (0, 135, 45, 45), 1: (45, 135, 45, 45), 2: (90, 135, 45, 45) }
		self.up_states = { 0: (0, 0, 45, 45), 1: (45, 0, 45, 45), 2: (90, 0, 45, 45) }
		self.down_states = { 0: (0, 90, 45, 45), 1: (45, 90, 45, 45), 2: (90, 90, 45, 45) }
		self.diamonds_taken = 0
		self.key = False

	def moveRight(self):
		''' Move the BomberManAvatar character to the right '''
		return super().moveRight()

	def moveLeft(self):
		''' Move the BomberManAvatar character to the left '''
		return super().moveLeft()

	def moveUp(self):
		''' Move the BomberManAvatar character to the up '''
		return super().moveUp()

	def moveDown(self):
		''' Move the BomberManAvatar character to the down '''
		return super().moveDown()

	def checkPlayerMovement(self, flag):
		''' Check if the movement of the character "BomberManAvatar" is valid 
			:param flag: Indicates the direction in which the BomberManAvatar character will move '''
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

			else: # downward movement 
				# Check the previous comment in the if statment with flag 1 
				if (
					(self.y + 44 > element.first_range_y) 
					and (self.y < element.second_range_y) 
					and (self.x + 44 > element.first_range_x) 
					and (self.x  < element.second_range_x)
				):
					self.y = self.aux
		return self.state_of_return

	
	def checkPlayerAndEnemy(self,list_of_enemies):
		'''Method to check if the player has a collision with any of the enemies Of the collision happens,
		the player will return to the x 50 and y 50 coordinates. 
			:param list_of_enemies: Information list of existing enemies
			:return: True if we have a collision, false otherwise '''
		for enemy in (list_of_enemies):
			if enemy.enable is True:
				if(#rigth direction
					(enemy.x <= self.x + 44  <= enemy.x + 44) 
					and ((enemy.y <= self.y <= enemy.y + 44) or (enemy.y <= self.y + 44 <= enemy.y + 44))
				):
					#print("choca contra enemigo der", enemy.enable)
					self.x = 50
					self.y = 50
					return True
				if (#check left direction
					(enemy.x <= self.x  <= enemy.x + 44)
					and ((enemy.y <= self.y <= enemy.y + 44) or (enemy.y <= self.y + 44 <= enemy.y + 44))
				):
					#print("choca contra enemigo izq", enemy.enable)
					self.x = 50
					self.y = 50
					return True
				if (#check upward
					(enemy.y <= self.y <= enemy.y + 44)
					and ((enemy.x <= self.x <= enemy.x + 44))
				):
					#print("choca contra enemigo arriba", enemy.enable)
					self.x = 50
					self.y = 50
					return True
				if (#check downward
					(enemy.y <= self.y + 44 <= enemy.y + 44)
					and ((enemy.x <= self.x <= enemy.x + 44))
				):
					#print("choca contra enemigo abajo", enemy.enable)
					self.x = 50
					self.y = 50
					return True
		return False

	
	def verify_crash(self, list_of_enemies):
		'''Method to verify if any enemy has a collision with the player. If the collision happens then
		the bomberman has to update his position and decrement his lives 
			:param list_of_enemies: Information list of existing enemies
			:return: True if we have a collision, false otherwise '''
		if(self.checkPlayerAndEnemy(list_of_enemies) is True):
			#self.bomber.simple_update(self.bomber.x, self.bomber.y)
			self.rect.x = 50
			self.rect.y = 50
			self.lives = self.lives - 1

	def restart(self, position, init_x, init_y):
		''' Reset the game settings for the BomberManAvatar 
			:param position: position of the BomberManAvatar character in the game view 
			:param init_x: X coordinate "BomberManAvatar" in the view of game
			:param init_y: Y coordinate "BomberManAvatar" in the view of game '''
		self.diamonds_taken = 0
		super().restart(position, init_x, init_y)