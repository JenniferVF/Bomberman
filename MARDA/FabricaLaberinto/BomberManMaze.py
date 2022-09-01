#Class specific maze product for BomberMan

from Maze import *

'''
Class that implements the specific functionalities and characteristics of the maze for the BomberMan Game
'''
class BomberManMaze(Maze):

	def __init__(self):
		''' Construct a new "BomberManMaze" object '''
		super().__init__()

		self.check_explosion = False 
		self.key_reveal = False
		self.key_time = 0  # key block explosion time
		self.total_diamonds = 0
		self.diamonds_taken = 0
		
		self.diamond_list= []
		self.door = None

		self.findNumber = False
		#the maze in the parent class goes to use maze by parameter
		self.maze = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, #1-15
			1,0,0,0,1,1,1,0,1,0,1,0,0,0,1, #16-30
			1,0,0,2,0,0,2,0,2,0,2,0,2,0,1, #31-45
			1,2,0,0,1,2,1,2,0,0,0,0,0,0,1, #46-60
			1,0,0,0,0,0,2,0,0,0,2,0,1,0,1, #61-75
			1,0,2,0,1,1,1,2,0,1,2,0,0,0,1, #76-90
			1,0,0,0,0,0,1,0,1,0,0,0,0,2,1, #91-105
			1,0,0,1,0,0,0,0,0,0,2,1,0,0,1, #106-120
			1,0,0,0,0,1,0,0,0,0,0,0,0,1,1, #121-135
			1,0,1,0,1,0,0,2,1,0,2,0,2,0,1, #136-150
			1,0,0,0,2,0,0,0,0,0,0,2,0,1,1, #151-165
			1,0,0,2,2,0,1,0,1,0,0,2,0,0,1, #166-180
			1,0,2,0,0,2,0,0,0,0,0,0,2,0,1, #181-195
			1,0,1,0,2,0,1,0,0,0,0,0,0,0,1, #196-210
			#1,0,0,0,0,0,0,0,0,0,0,0,0,0,1, #196-210
			1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] #211-225

		self.randomizeSections()

		self.init_bomberman_features()
	
	
	def saveInvalidPositionsToMove(self):
		''' Make a list with information about the boxes where there are blocks where you cannot walk '''
		self.saveDiamondsAndDoorLocations()
		return super().saveInvalidPositionsToMove(self.maze)
	
	
	def updateInvalidPositions(self, list_aux):
		'''Everytime that we need check if at least one element was detroyed 
			:param list_aux: list that we will use as auxiliary '''
		super().updateInvalidPositions(list_aux)

	def restart(self):
		''' Reset the maze settings for restart the game '''
		self.__init__()
		
	
	def randomizeSections(self):
		''' Method to randomize some parts of the maze, that was the easiest way to handle this problem'''
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

	def saveDiamondsAndDoorLocations(self):
		''' Make a list of information about the squares where there are diamonds
		and the square where the door is '''
		first_range_x = 0
		second_range_x = 50
		first_range_y = 0
		second_range_y = 50
		aux_index = 1
		for i in range(0,self.N*self.N):
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
			
	def init_bomberman_features(self):
		''' Initialize the bomberman´s features '''
		self.saveInvalidPositionsToMove()

