
#Abstract product class to generate mazes
import random
from random import randrange
from InfoPixel import *
from abc import ABC, abstractmethod

'''
MARDA class that allows to implement the specific maze of the game
'''
class Maze(ABC):

	def __init__(self): 
		''' Construct a new "Maze" object '''  
		self.N = 15
		self.win = False
		self.disable_block_list= []
		self.list_of_positions = []

	@abstractmethod
	def saveInvalidPositionsToMove(self,maze):
		'''Maze by parameter. Remember first call this method and then the method inside Bomberman with the door an diamonds
			:param maze: game's maze'''
		first_range_x = 0
		second_range_x = 50
		first_range_y = 0
		second_range_y = 50
		aux_index = 1
		for i in range(0,self.N*self.N):
			if maze[i] == 1 or maze[i] == 2 or maze[i] == 4: # to check if the element is a block
				self.disable_block_list.append(
					InfoPixel(
						first_range_x,
						second_range_x,
						first_range_y,
						second_range_y,
						maze[i], 
						i
					)
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

		return self.disable_block_list

	@abstractmethod
	def updateInvalidPositions(self, list_aux):
		''' Method to update the positions where the avatar can move 
			:param list_aux: list to be used as auxiliary'''
		for n in range(len(list_aux)):
			counter = 0
			for i in self.disable_block_list:
				if list_aux[n] == i.index_in_maze:
					del self.disable_block_list[counter]
				counter = counter + 1

	@abstractmethod
	def restart(self):
		''' Method that resets the maze to its initial state '''
		self.__init__()
		self.disable_block_list = self.saveInvalidPositionsToMove()
	
