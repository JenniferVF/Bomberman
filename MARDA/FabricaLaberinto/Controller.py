#this class is equivalent to the client class of the Abstract Factory pattern
from abc import ABC, abstractmethod
from BomberManFactory import *
import os.path
import pygame
import time

''' 
MARDA class that will allow to implement specific controllers for different maze games
'''
class Controller(ABC):
	
	def __init__(self):
		''' Construct a new Controller object '''
		self.start = True;
		self.gaming = False;
		self.endGame = False;
		self.win = False;

	@abstractmethod
	def startGame(self):
		''' Displays the initial game screen '''
		pass

	abstractmethod
	def play(self):
		''' Show the maze screen and manage the game operation '''
		pass

	@abstractmethod
	def winner(self):
		''' Check and establish when the game has been won '''
		pass

	@abstractmethod
	def gameOver(self):
		''' Check and establish if the game has been lost '''
		pass

	@abstractmethod
	def restart(self):
		''' Restart the game '''
		pass

	
	def execute(self):
		'''Template method with the logic of game'''
		self.startGame()

		while(self.gaming):
			self.play()

		
