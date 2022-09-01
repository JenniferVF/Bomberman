from pygame.locals import *
from pygame import mixer
import pygame

class SoundOfGame:
	pygame.init()
	def __init__(
		self,interlude_song,
		song_in_game, 
		song_lost_game, 
		song_win_game
	):
		self.interlude_song = interlude_song
		self.song_in_game = song_in_game
		self.song_lost_game = song_lost_game
		self.song_win_game = song_win_game
		self.explosion_sound = pygame.mixer.Sound('music/8BitExplosion.ogg')
		self.step_sound = pygame.mixer.Sound('music/step3.wav')
	
	'''Method to start a song each time that will be neccessary '''
	def start_song_in_game(self, song_selected):
		mixer.init()
		self.loop = True
		if song_selected == 1: #interlude song
			mixer.music.load(self.interlude_song)
		elif song_selected == 2:#main song
			mixer.music.load(self.song_in_game)
		elif song_selected == 3: #losses song
			mixer.music.load(self.song_lost_game)
			self.loop = False
		elif song_selected == 4: # win song
			mixer.music.load(self.song_win_game)
			self.loop = False
		mixer.music.set_volume(0.5)
		if self.loop is True:# to handle the loop of the song
			mixer.music.play(-1)
		else:
			mixer.music.play()		
			
	'''Method to stop one of the songs of the game'''
	def stop_song_in_game(self):
		mixer.music.stop()

	''' Method to play sounds, handle sounds is different to use mixer music '''
	def play_sound(self,effect_sound):
		if effect_sound == 1:
			self.explosion_sound.set_volume(0.3)
			self.explosion_sound.play()
		elif effect_sound == 2:
			self.step_sound.set_volume(0.1)
			self.step_sound.play()