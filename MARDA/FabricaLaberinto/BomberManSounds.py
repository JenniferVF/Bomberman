#Class specific sounds product for BomberMan

from Sounds import *

'''
Class that implements the functionalities and characteristics of the specific sounds of the BomberMan game
'''
class BomberManSounds(Sounds):

    def __init__(self):
       super().__init__(
           "music/BGM #10.mp3",
           "music/BGM #11.mp3",
           "music/youLost#03.mp3",
           "music/youWin#02.mp3")
       self.explosion_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'music/8BitExplosion.ogg'))
       self.step_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'music/step3.wav'))
   
    def start_song_in_game(self):
        ''' Play the sound of the initial game screen '''
        super().start_song_in_game()

    def start_interlude_song(self):
        ''' Play the sound of the interlude of game'''
        super().start_interlude_song()

    def start_win_game_sound(self):
        ''' Play the sound of the You_Win game screen '''
        #super().start_interlude_song()
        super().stop_song_in_game()
        super().start_win_game_sound()

    def start_lost_game_sound(self):
        ''' Play the sound of the Game_Over game screen '''
        #super().start_interlude_song()
        super().stop_song_in_game()
        super().start_lost_game_sound()

    def stop_song_in_game(self):
        '''Method to stop one of the songs of the game'''
        super().stop_song_in_game()

    def play_explosion_sound(self):
        ''' Method to play the explosion sound, handle sounds is different to use mixer music '''
        self.explosion_sound.set_volume(0.3)
        self.explosion_sound.play()

    def play_step_sound(self):
        ''' Method to play the step sounds, handle sounds is different to use mixer music '''
        self.step_sound.set_volume(0.1)
        self.step_sound.play()
