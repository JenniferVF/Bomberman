from random import seed
from random import randint

'''
Player Class. We use it to handle the movements of the player in the screen.
 '''
class Player:
		
	def __init__(self, init_x, init_y, init_speed, init_used):
		self.x = init_x # 50
		self.y = init_y #50
		self.aux = 0

		self.used_by = init_used# used to distinguis what kind of instance was created
		
		self.left_move_activate = True # first check is with left move
		self.right_move_activate = False
		self.up_move_activate = False
		self.down_move_activate = False

		self.lives = 3
		self.key = False
		self.speed = init_speed
	''' Method to generate random numbers, we use them in the
recognizeTheMovement method '''
	def generateRandomValue(self):
		seed(None)
		return randint(0,2)
	'''This method works with flags each one check if is possible continue with
the actual movement, if not is possible the programa select randomly what will be
the next movement, after that when we have the new movement the next step is
update de others boolean variables to avoid conflicts '''
	def recognizeTheMovement(self, flag):
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

	''' To handle the movement at the right of the player. If the player reaches the limit of the screen 
the program denied the movement'''
	def moveRigth(self):
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


	''' To handle the movement at the left of the player. If the player reaches the limit of the screen 
the program denied the movement'''
	def moveLeft(self):
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


	'''Method to handle the movement of the avatar. This method verifies if the next movement of the avatar
collides with any blocking space occupied by any other element of the screen'''
	def checkPlayerMovement(self, flag):
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
					if self.used_by is True:# used by player
						self.x = self.aux
					else: #used by enemy
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
					if self.used_by is True:# used by player 
						self.x = self.aux
					else: #used by enemy
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
					'''print(
						"rangos X ", element.first_range_x,"-",
						element.second_range_x, " Rangos Y ", 
						element.first_range_y, "-",element.second_range_y,
						" X ->", self.x, "y ->",self.y
					)'''
					if self.used_by is True:# used by player 
						self.y = self.aux
					else: #used by enemy
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
					if self.used_by is True:# used by player 
						self.y = self.aux
					else: #used by enemy	
						self.state_of_return = False #It knocks against an element
						self.y = self.aux
		return self.state_of_return
	'''Method to check if the player has a collision with any of the enemies Of the collision happens,
the player will return to the x 50 and y 50 coordinates, 
We would return True if we have a collision'''
	def checkPlayerAndEnemy(self,list_of_enemies):
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
		