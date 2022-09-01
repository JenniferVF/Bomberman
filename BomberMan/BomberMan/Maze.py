import random
from random import seed

from InfoPixel import *
from random import randrange


class Maze:
	def __init__(self):
		seed(None)
		self.M = 15
		self.N = 15
		# we use this variable to verify when will have an explotion
		# False we don't need to check and explotion
		# True we need to check the explotion
		self.win = False
		self.check_explosion = False 
		self.key_reveal = False
		self.total_diamonds = 0
		self.diamonds_taken = 0
		self.player_diamonds = 0
		self.enemy_diamonds = 0

		self.disable_block_list= []
		self.list_of_positions = []
		self.diamond_list= []
		self.door = None

		self.findNumber = False

		#1- indestructible block in the maze
		#2- destructible block in the maze
		#3- enemys in the maze (maybe we would change this)
		#4- destuctible block in the maze, this element has a key inside
		#5- diamonds in the maze
		#6- door

		self.maze = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, #1-15
					1,0,0,0,1,1,1,0,1,0,1,0,0,0,1, #16-30
					1,0,0,2,0,0,2,0,2,0,2,0,2,0,1, #31-45
					1,2,0,0,1,2,1,2,0,0,0,0,0,0,1, #46-60
					1,5,0,0,0,0,2,0,0,0,2,0,1,0,1, #61-75
					1,5,2,0,1,1,1,2,0,1,2,0,0,0,1, #76-90
					1,5,0,0,0,0,1,0,1,0,0,0,0,2,1, #91-105
					1,0,0,1,0,0,0,4,0,0,2,1,0,0,1, #106-120
					1,0,0,0,0,1,0,0,0,0,0,0,0,1,1, #121-135
					1,0,1,0,1,0,0,2,1,0,2,0,2,0,1, #136-150
					1,0,0,0,2,0,0,0,0,0,0,2,0,1,1, #151-165
					1,0,0,2,2,0,1,0,1,0,0,2,0,0,1, #166-180
					1,0,2,0,0,2,0,5,5,5,0,0,2,0,1, #181-195
					1,0,1,0,2,0,1,5,0,5,0,0,0,0,1, #196-210
					1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] #211-225
		
		self.randomizeSections()
		self.placeDoor()

	''' Method to randomize some parts of the maze, that was the easiest way to handle 
this problem'''
	def randomizeSections(self):
		self.copy = self.maze[19:28]
		random.shuffle(self.copy)
		self.maze[19:28] = self.copy

		self.copy = self.maze[32:42] #42 to avoid close the way of the enemy
		random.shuffle(self.copy)
		self.maze[32:42] = self.copy
		
		self.copy = self.maze[47:59]
		random.shuffle(self.copy)
		self.maze[47:59] = self.copy

		self.copy = self.maze[47:59]
		random.shuffle(self.copy)
		self.maze[47:59] = self.copy

		self.copy = self.maze[61:74]
		random.shuffle(self.copy)
		self.maze[61:74] = self.copy

		self.copy = self.maze[76:89]
		random.shuffle(self.copy)
		self.maze[76:89] = self.copy

		self.copy = self.maze[91:104]
		random.shuffle(self.copy)
		self.maze[91:104] = self.copy

		self.copy = self.maze[106:119]
		random.shuffle(self.copy)
		self.maze[106:119] = self.copy

		self.copy = self.maze[121:134]
		random.shuffle(self.copy)
		self.maze[121:134] = self.copy
		#136-150
		self.copy = self.maze[136:149]
		random.shuffle(self.copy)
		self.maze[136:149] = self.copy
		#151-165
		self.copy = self.maze[151:164]
		random.shuffle(self.copy)
		self.maze[151:164] = self.copy
		#166-180
		self.copy = self.maze[166:179]
		random.shuffle(self.copy)
		self.maze[151:164] = self.copy
		#181-195
		self.copy = self.maze[182:193] #193 to avoid close the way of the enemy
		random.shuffle(self.copy)
		self.maze[182:193] = self.copy
		#196-210
		self.copy = self.maze[197:208]
		random.shuffle(self.copy)
		self.maze[197:208] = self.copy
		#211-225
			
	'''We save the pixels occupied by the block elements in a list of InfoPixel. 
The main idea to work in this way is to check if the movement is valid or invalid.
After that, a good idea maybe is handling the matrix maze with one kind of update 
(for example in case of changes: convert the elements with 2 by 0 and call de draw function) 
of the state of the block'''
	def saveInvalidPositionsToMove(self):
		first_range_x = 0
		second_range_x = 50
		first_range_y = 0
		second_range_y = 50
		aux_index = 1
		self.total_diamonds = 0
		self.diamonds_taken = 0
		self.enemy_diamonds = 0
		self.player_diamonds = 0
		self.door = None
		self.findNumber = False
		
		self.diamond_list= []
		for i in range(0,self.M*self.N):
			if self.maze[i] == 1 or self.maze[i] == 2 or self.maze[i] == 4: # to check if the element is a block
				self.disable_block_list.append(
					InfoPixel(
						first_range_x,
						second_range_x,
						first_range_y,
						second_range_y,
						self.maze[i], 
						i
					)
				) #these pixels are occupied by an element

			if self.maze[i] == 5: # to check if the element is a diamond
				self.total_diamonds = self.total_diamonds + 1
				self.diamonds_taken = self.total_diamonds
				self.diamond_list.append(
					InfoPixel(
						first_range_x,
						second_range_x,
						first_range_y,
						second_range_y,
						self.maze[i], 
						i
					)
				) #these pixels are occupied by an element

			if self.maze[i] == 6: # to check if the element is the door
				self.door =	InfoPixel(
					first_range_x,
					second_range_x,
					first_range_y,
					second_range_y,
					self.maze[i], 
					i
				) #these pixels are occupied by an element		

			first_range_x = second_range_x
			second_range_x = first_range_x + 50

			if aux_index % 15 == 0: # 15 to change the "row" in the maze
				# update the position in axis x
				first_range_x = 0 
				second_range_x = 50
				# update the position in axis y
				first_range_y = second_range_y
				second_range_y =  first_range_y + 50
			aux_index = aux_index + 1 # count increment
		''' The next for is to probe the correct saving of the coordinates
		for i in(self.disable_block_list):
			print(
				'1-x ',i.first_range_x, 
				'2-x ',i.second_range_x,
				'1-Y ',i.first_range_y,
				'2-Y ',i.second_range_y,
				'Element ', i.ocuppied
			)
		'''
		return self.disable_block_list

	''' This method draws on the screen in accordance with the values of the maze list.
 If the element in the list is 1 we put in the screen an indestructible block.
 If the element in the list is 2 we put in the screen a destructible block.
 And finally, if the element in the list is 0 we don't put anything on the screen.
 '''
	def draw(self,display_surf,image_surf,block_to_destroy,diamond_maze,door):
		bx = 0
		by = 0
		for i in range(0,self.M*self.N):
			if self.maze[ bx + (by*self.M)] == 1:
				display_surf.blit(image_surf,(bx * 50, by * 50))# 50 is the number of pixels 'printed' in every iteration
			if self.maze[ bx + (by*self.M)] == 2 or self.maze[ bx + (by*self.M)] == 4:
				display_surf.blit(block_to_destroy,(bx * 50, by * 50))
			if self.maze[ bx + (by*self.M)] == 5:
				display_surf.blit(diamond_maze,(bx * 50, by * 50))
			if self.maze[ bx + (by*self.M)] == 6:	#draw the door
				display_surf.blit(door,(bx * 50, by * 50))
			bx = bx + 1
			if bx > self.M-1:
				bx = 0
				by = by + 1	

	''' Method to update the positions where the avatar can move '''
	def updateInvalidPositions(self, list_aux):
		for n in range(len(list_aux)):
			counter = 0
			for i in self.disable_block_list:
				if list_aux[n] == i.index_in_maze:
					del self.disable_block_list[counter]
				counter = counter + 1

	'''Method to check where the bomb gonna explode and what blocks will be destroyed. '''
	def checkBombExplosion(self, x_position , y_position):
		#print("Bomba ", x_position, y_position)
		self.list_aux = []
		for i in self.disable_block_list:
			if i.ocuppied == 2 or i.ocuppied == 4: #destructible block
				if (
					((i.first_range_x < (x_position + 94) <= i.second_range_x) and (i.first_range_y <= y_position < i.second_range_y)) 
					or # we need the next condition to consider the bottom edge of the bomb as a part of the explosion
					((i.first_range_x < (x_position + 94) <= i.second_range_x) and (i.first_range_y <= (y_position + 44) < i.second_range_y)) # we add to x pixel 44 to include every pixel of the bomb
				): # check to the rigth, 44 + 50, we must consider the first pxl, after that sum the next 44 and finally, we have to sum the 50 pxl (the range of explosion)
					self.maze[i.index_in_maze] = 0
					self.list_aux.append(i.index_in_maze)

					if (i.ocuppied == 4):
						self.key_reveal = True

					#print('Entra a rigth')
				elif (
					((i.first_range_x <= (x_position - 50) < i.second_range_x) and (i.first_range_y < (y_position) < i.second_range_y)) 
					or # we need the next condition to consider the bottom edge of the bomb as a part of the explosion
					((i.first_range_x <= (x_position - 50) < i.second_range_x) and (i.first_range_y < (y_position + 44) < i.second_range_y))
				): # check to left
					self.maze[i.index_in_maze] = 0
					self.list_aux.append(i.index_in_maze)

					if (i.ocuppied == 4):
						self.key_reveal = True

					#print('Entra a left')
				elif (
					((i.first_range_y <= (y_position - 50) < i.second_range_y) and (i.first_range_x <= x_position < i.second_range_x)) 
					or # we need the next condition to consider the front edge of the bomb as a part of the explosion
					((i.first_range_y <= (y_position - 50) < i.second_range_y) and (i.first_range_x <= (x_position + 44) < i.second_range_x))
				
				): # check upward
					self.maze[i.index_in_maze] = 0
					self.list_aux.append(i.index_in_maze)

					if (i.ocuppied == 4):
						self.key_reveal = True

					#print('Entra a arriba')
				elif (
					((i.first_range_y < (y_position + 94) <= i.second_range_y) and(i.first_range_x < x_position < i.second_range_x)) 
					or # we need the next condition to consider the front edge of the bomb as a part of the explosion
					((i.first_range_y < (y_position + 94) <= i.second_range_y) and (i.first_range_x < (x_position + 44) < i.second_range_x))
				
				): # check downward
					self.maze[i.index_in_maze] = 0
					self.list_aux.append(i.index_in_maze)

					if (i.ocuppied == 4):
						self.key_reveal = True

					#print('Entra a abajo')

		self.updateInvalidPositions(self.list_aux)
		return self.disable_block_list
	
	def explosionAgainstAvatar(self, x_bomb,y_bomb, x_enemy, y_enemy):
		#print("Bomba X ", x_bomb, " Y ", y_bomb, " avatar X ",x_enemy," Y ", y_enemy)
		if (#check the rigth direction, we sum 44 + 50 as range of the explosion
		#and we check y_bomb between the borders of the y coordinates of the enemy to eliminate
		#if the enemy pixels collides with the bomb
			(x_bomb <= x_enemy <= x_bomb + 94 ) and
			((y_enemy <= y_bomb <= y_enemy + 44 ) or (y_enemy <= y_bomb + 44 <= y_enemy + 44))
		):
			#print('Se elimina enemigo derecha')
			return False
		if (#check the left direction
			((x_bomb - 50 <= x_enemy + 44 <= x_bomb) or (x_bomb - 50 <= x_enemy <= x_bomb)) and
			((y_enemy <= y_bomb <= y_enemy + 44) or (y_enemy <= y_bomb + 44 <= y_enemy + 44))
		):
			#print('Se elimina enemigo izquier')
			return False
		if (# check downward
			(y_bomb + 44 <= y_enemy <= y_bomb + 94) and
			((x_enemy <= x_bomb <= x_enemy + 44) or (x_enemy <= x_bomb + 44 <= x_enemy + 44))
		):
			#print('Se elimina enemigo abajo')
			return False
		if (#check upward
			(y_bomb - 50  <= y_enemy + 44 <= y_bomb) and
			((x_enemy <= x_bomb <= x_enemy + 44) or (x_enemy <= x_bomb + 44 <= x_enemy + 44))
		):
			#print('Se elimina enemigo arriba')
			return False
		return True # is enable to keeping using

	''' Method that controls the taking of diamonds according to the position of the avatar '''
	def takeDiamond(self, x_position , y_position, direction, avatar):
		self.list_aux = []
		for i in self.diamond_list:
			if i.ocuppied == 5: #diamond in the maze
				if direction == 'r':
					if (
						((i.first_range_x <= (x_position + 44) <= i.second_range_x) and (i.first_range_y <= y_position < i.second_range_y)) 
						or ((i.first_range_x <= (x_position + 44) <= i.second_range_x) and (i.first_range_y <= (y_position + 44) < i.second_range_y)) # we add to x pixel 44 to include every pixel of the bomb
					): # check to the rigth, len img = 44
						self.maze[i.index_in_maze] = 0
						self.list_aux.append(i.index_in_maze)
						if avatar == 'p':
							self.player_diamonds = self.player_diamonds + 1
							self.diamonds_taken = self.diamonds_taken - 1
						elif avatar == 'e':
							self.enemy_diamonds = self.enemy_diamonds + 1
							self.diamonds_taken = self.diamonds_taken - 1
				
				if direction == 'l':
					if (
						((i.first_range_x <= (x_position) < i.second_range_x) and (i.first_range_y < (y_position) < i.second_range_y)) 
						or ((i.first_range_x <= (x_position) < i.second_range_x) and (i.first_range_y < (y_position + 44) < i.second_range_y))
					): # check to left
						self.maze[i.index_in_maze] = 0
						self.list_aux.append(i.index_in_maze)
						if avatar == 'p':
							self.player_diamonds = self.player_diamonds + 1
							self.diamonds_taken = self.diamonds_taken - 1
						elif avatar == 'e':
							self.enemy_diamonds = self.enemy_diamonds + 1
							self.diamonds_taken = self.diamonds_taken - 1
					
				if direction == 'u':
					if (
						((i.first_range_y <= (y_position) < i.second_range_y) and (i.first_range_x <= x_position < i.second_range_x)) 
						#or ((i.first_range_y <= (y_position) < i.second_range_y) and (i.first_range_x <= (x_position + 44) < i.second_range_x))
				
					): # check upward
						self.maze[i.index_in_maze] = 0
						self.list_aux.append(i.index_in_maze)
						if avatar == 'p':
							self.player_diamonds = self.player_diamonds + 1
							self.diamonds_taken = self.diamonds_taken - 1
						elif avatar == 'e':
							self.enemy_diamonds = self.enemy_diamonds + 1
							self.diamonds_taken = self.diamonds_taken - 1

				if direction == 'd':
					if (
						((i.first_range_y <= (y_position + 44) <= i.second_range_y) and(i.first_range_x <= x_position < i.second_range_x)) 
						or ((i.first_range_y <= (y_position + 44) <= i.second_range_y) and (i.first_range_x <= (x_position + 44) < i.second_range_x))
				
					): # check downward
						self.maze[i.index_in_maze] = 0
						self.list_aux.append(i.index_in_maze)
						if avatar == 'p':
							self.player_diamonds = self.player_diamonds + 1
							self.diamonds_taken = self.diamonds_taken - 1
						elif avatar == 'e':
							self.enemy_diamonds = self.enemy_diamonds + 1
							self.diamonds_taken = self.diamonds_taken - 1

		self.updateDiamonds(self.list_aux)
		return self.diamond_list



	''' Method to update the positions where the diamonds are '''
	def updateDiamonds(self, list_aux):
		for n in range(len(list_aux)):
			counter = 0
			for i in self.diamond_list:
				if list_aux[n] == i.index_in_maze:
					del self.diamond_list[counter]
				counter = counter + 1

	
	''' Method that resets the maze to its initial state '''
	def restart(self):
		self.__init__()
		self.disable_block_list = self.saveInvalidPositionsToMove()


	''' Method for open the door and win '''
	def openDoor(self, x_position , y_position):
		i = self.door
		if (i.first_range_x < x_position < (i.first_range_x + 30)
		and i.first_range_y < y_position < (i.first_range_y + 15)):
			if i.ocuppied == 6: #diamond in the maze
				if self.key_reveal:
					self.win = True

	def placeDoor(self):
		self.tam = len(self.maze)
		self.i = 0
		while (not self.findNumber):
			self.i = randrange(self.tam-1)
			if (self.maze[self.i] == 0):
				self.maze[self.i] = 6
				self.findNumber = True

