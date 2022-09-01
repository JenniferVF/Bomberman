#Abstract product class to generate game sounds
from pygame.locals import *
from pygame import mixer
import os.path
import pygame

from abc import ABC, abstractmethod

'''
MARDA class that allows to implement specific sounds for specific maze games
'''
class Sounds(ABC):

    def __init__(   
        self, interlude_song,
		song_in_game, 
		song_lost_game, 
		song_win_game
	):
        ''' Construct a new "Sounds" object '''
        self.interlude_song = interlude_song
        self.song_in_game = song_in_game
        self.song_lost_game = song_lost_game
        self.song_win_game = song_win_game 
    
    '''Method to start the interlude_song whenever neccessary '''
    @abstractmethod
    def start_interlude_song(self):
        mixer.init()
        mixer.music.load(os.path.join(os.path.dirname(__file__), self.interlude_song))
        mixer.music.set_volume(0.5)
        mixer.music.play(-1)

    '''Method to start the song_in_game whenever neccessary '''
    @abstractmethod
    def start_song_in_game(self):
        mixer.music.load(os.path.join(os.path.dirname(__file__), self.song_in_game))
        mixer.music.set_volume(0.5)
        mixer.music.play(-1)

    '''Method to start the win_game song whenever neccessary '''
    @abstractmethod
    def start_win_game_sound(self):
        mixer.music.load(os.path.join(os.path.dirname(__file__), self.song_win_game))
        mixer.music.set_volume(0.5)
        mixer.music.play()

    '''Method to start the lost_game song whenever neccessary '''
    @abstractmethod
    def start_lost_game_sound(self):
        mixer.music.load(os.path.join(os.path.dirname(__file__), self.song_lost_game))
        mixer.music.set_volume(0.5)
        mixer.music.play()	    

    '''Method to stop one of the songs of the game'''
    @abstractmethod
    def stop_song_in_game(self):
        mixer.music.stop()

