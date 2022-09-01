from pygame.locals import *
import pygame
from pygame import mixer
import time
import math

from Maze import *
import BomberMan 
import Enemy 
import Bomb
from SoundOfGame import *

class Controller:
	windowWidth = 1000
	windowHeight= 800

	def __init__(self):
		self.runnig = True
		self.bomb = False
		self.pressSpace = True

		self.x_bomb = 0
		self.y_bomb = 0
		self.display_surf = None
		self.image_surf = None
		self.block_surf = None
		self.block_to_destroy = None
		self.live = None
		self.diamond = None
		self.diamond_maze = None
		self.image_bomb = None
		self.key = None
		self.enemy = None
		self.background = None
		self.door = None
		self.game_over_diamond = None
		self.game_over_lives = None

		self.list_of_enemies = []

		self.bomba = Bomb.Bomb((0, 0))

		#initialize bomberman
		self.bomber = BomberMan.bomberman((51,50), 51, 50, 5, True)
		#initiliaze enemies
		self.first_enemy = Enemy.Enemy((655,655), 655, 655, 2.5, False)
		self.second_enemy =  Enemy.Enemy((50,655), 50, 655, 2.5, False)
		self.third_enemy =  Enemy.Enemy((655,50), 655, 50, 2.5, False)

		self.maze = Maze()
		self.sounds_of_game = SoundOfGame(
			"music/BGM #10.mp3",
			"music/BGM #11.mp3",
			"music/youLost#03.mp3",
			"music/youWin#02.mp3"
		)
		

		# to check in the bomber class the valid movements
		self.bomber.disable_block_list = self.maze.saveInvalidPositionsToMove() 

		#We share the invalid movements to each enemy
		self.first_enemy.disable_block_list = self.bomber.disable_block_list
		self.second_enemy.disable_block_list = self.bomber.disable_block_list
		self.third_enemy.disable_block_list = self.bomber.disable_block_list
		
		self.list_of_enemies.append(self.first_enemy)
		self.list_of_enemies.append(self.second_enemy)
		self.list_of_enemies.append(self.third_enemy)

		self.now = 0 # for time
		self.wait = 0 # time to wait

		self.key_time = 0

		#Colors
		self.green = (0,255,0)
		self.bright_green = (0,150,0)
		self.red = (255,0,0)
		self.bright_red = (150,0,0)

	''' Method to stablish the init values for the display screen '''
	def on_init(self):
		pygame.init()
		
		self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
		pygame.display.set_caption("Bomberman en Python")

		self._running = True

		self._background = pygame.image.load("img/background.png").convert()#1000x800 background image

		# blocks in the screen
		self._block_surf = pygame.image.load("img/block_indestructible.jpg").convert()#50x50 pxls
		self._block_to_destroy = pygame.image.load("img/block_destructible.png").convert()#50x50 pxls

		# icons in the screen
		self._live = pygame.image.load("img/live.png").convert_alpha() # 20 pxls
		self._diamond = pygame.image.load("img/diamond.png").convert_alpha() # 30 pxls
		self._diamond_maze = pygame.image.load("img/diamond_maze.png").convert_alpha() # 45 pxls
		self._key = pygame.image.load("img/key.png").convert_alpha() # 45 pxls
		#self._image_bomb = pygame.image.load("img/grenade.png").convert_alpha() # 45x45 pxls
		self._door = pygame.image.load("img/door.png").convert_alpha() # 50x28 pxls

		# Endgame screens
		self._game_over_diamond = pygame.image.load("img/game_over_diamond.png").convert_alpha() # 500x400 pxls
		self._game_over_lives = pygame.image.load("img/game_over_lives.png").convert_alpha() # 500x400 pxls


	'''Method to display the image of the avatars, if the enemy
is enable then will be printed in the screen otherwise the enemy won't be printed '''
	def displayAvatars(self):
		# if you want to check the enemy stop you can descoment the next 4 lines and coment ****
		#self.display_surf.blit(self.bomber.image, self.bomber.rect)
		#self.display_surf.blit(self.first_enemy.image, self.first_enemy.rect)
		#self.display_surf.blit(self.second_enemy.image, self.second_enemy.rect)
		#self.display_surf.blit(self.third_enemy.image,self.third_enemy.rect)
		#**** comment the next 7 lines
		self.display_surf.blit(self.bomber.image, self.bomber.rect)

		if self.first_enemy.enable is True:		
			self.display_surf.blit(self.first_enemy.image, self.first_enemy.rect)
		if self.second_enemy.enable is True:	
			self.display_surf.blit(self.second_enemy.image, self.second_enemy.rect)
		if self.third_enemy.enable is True:
			self.display_surf.blit(self.third_enemy.image,self.third_enemy.rect)
	
	''' Method to handle the exit of the screen '''
	def on_event(self, event):
		if event.type == QUIT:
			self._running = False

	'''Method to verify if a bomb explodes near of any enemy. If the bomb touch any
enemy the state of availability would change to False'''
	def check_availability_of_avatars(self):
		if self.first_enemy.enable is True:
			self.first_enemy.enable = self.maze.explosionAgainstAvatar(self.x_bomb,self.y_bomb,self.first_enemy.x,self.first_enemy.y)
		if self.second_enemy.enable is True:
			self.second_enemy.enable = self.maze.explosionAgainstAvatar(self.x_bomb,self.y_bomb,self.second_enemy.x,self.second_enemy.y)
		if self.third_enemy.enable is True:
			self.third_enemy.enable = self.maze.explosionAgainstAvatar(self.x_bomb,self.y_bomb,self.third_enemy.x,self.third_enemy.y)
		if (#to check if the explosion is near of the bomberman, false means the bomberman is unavailable, so he touched the epxlotion
			self.maze.explosionAgainstAvatar(self.x_bomb,self.y_bomb,self.bomber.x,self.bomber.y) is False 
		):
			self.bomber.x =51
			self.bomber.y = 51
			self.bomber.simple_update(self.bomber.x, self.bomber.y)
			self.bomber.lives = self.bomber.lives - 1
			

	'''Method to put the main elements into the screen and print them '''
	def on_render(self):
		posX = 820

		self._display_surf.fill((0,0,0))
		self.display_surf.blit(self._background,(0,0))#instruction to put a background image

		if self.bomb == True: # to establish the coordinates where the bomb will be printed

			self.x_bomb = self.bomber.x
			self.y_bomb = self.bomber.y
			self.bomba.position((self.bomber.x, self.bomber.y) )
			self.bomba.setFrame()
			#print('Bomb  X = ', self.x_bomb,' Y= ',self.y_bomb )

		if (self.wait > time.time()): # if the time to wait isn't complete, display the bomb in the screen
			
			self.bomba.update()
			self._display_surf.blit(self.bomba.image, self.bomba.rect)			
			self.maze.check_explosion = True # update check explotion, after that we must to check the explosion

		else: # completed time, it can  enable the button, time to explodes the bomb
			if self.maze.check_explosion is True:
				self.bomber.disable_block_list = self.maze.checkBombExplosion(self.x_bomb,self.y_bomb) # check the bomb explotion
				self.check_availability_of_avatars() # to check explotion against avatars
				self.maze.check_explosion = False #update de value, after that we don't need to check explotion
				self.key_time = time.time() + 2
				self.sounds_of_game.play_sound(1)
				
			self.pressSpace = True
		self.displayAvatars()
		self.maze.draw(self._display_surf,self._block_surf,self._block_to_destroy,self._diamond_maze,self._door)

		#Key reveal
		if self.maze.key_reveal == True and self.bomber.key == False:
			keyX = self.bomber.x
			keyY = self.bomber.y

			if (self.key_time > time.time()): # if the time to wait isn't complete, display the key in the screen
				self._display_surf.blit(self._key,(keyX, keyY-15))
			else:
				self.bomber.key = True
		
		pygame.draw.rect(self._display_surf, (210,150,75), (745,0,255,175))
		pygame.draw.rect(self._display_surf, (0,0,0), (750,5,245,165))
		fontLive = pygame.font.Font(None, 30)
		liveText = fontLive.render("Lives: " , 0, (225,255,255))
		keyText = fontLive.render("Key: " , 0, (225,255,255) )
		diamondText = fontLive.render("Diamonds: " , 0, (225,255,255))
		diamondWon = fontLive.render("Won: " + str(self.maze.player_diamonds), 0, (0,255,0))
		diamondLost = fontLive.render("Lost: " + str(self.maze.enemy_diamonds), 0, (255,0,0))
		diamondCount = fontLive.render(str(self.maze.diamonds_taken), 0, (255,255,255))
		

		self._display_surf.blit(liveText, (754,20))
		self._display_surf.blit(keyText, (754,55))
		self._display_surf.blit(diamondText, (754,90))
		self._display_surf.blit(self._diamond, (865,88))
		self._display_surf.blit(diamondCount, (900,90))
		self._display_surf.blit(diamondWon, (865,120))
		self._display_surf.blit(diamondLost, (865,145))
		
		

		for i in range(self.bomber.lives):
			self._display_surf.blit(self._live, (posX,20))
			posX = posX + 25

		if self.bomber.key:
			self._display_surf.blit(self._key, (800,55))
		
		pygame.display.flip()
	
	''' Method to clean up the screen '''
	def on_cleanup(self):
		pygame.display.update()
	
	def start(self):

		#pygame.init()
		self.sounds_of_game.start_song_in_game(1)# start the interlude song
		font		 = pygame.font.Font( None, 50)
		start        = True
		self.display_surf = pygame.display.set_mode((1000,800)) 
		image        = pygame.image.load("img/startGame.png") 
		textStart    = font.render("Start Game (F10)" , 0, (225,131,31) )
		textRules    = font.render("Game Rules (F11)" , 0, (225,131,31) ) 

		while(start):

			for eventos in pygame.event.get():

				keys = pygame.key.get_pressed()

				if (keys[K_F10]):
					start = False

				if (keys[K_F11]):
					self.rules()

				if (keys[K_ESCAPE]):
					start = False

			self.display_surf.blit( image, (0,0) )
			self.display_surf.blit( textStart, (400,645))
			self.display_surf.blit( textRules, (400,700))
			pygame.display.update()
		self.sounds_of_game.stop_song_in_game()

	def rules(self):
			
		rules        = True
		#font		 = pygame.font.Font( None, 50)
		font		 = pygame.font.SysFont("berlin sans FB", 30)
		image        = pygame.image.load("img/startRules.png")
		title        = font.render("Game Rules" , 0, (0,0,255) )

		#a textrect could be used instead of writing rule by rule
		components 	 = font.render("Game Components:", 0, (0,255,255))
		bomberman    = font.render("BomberMan" , 0, (255,255,255) )
		enemys       = font.render("Enemy" , 0, (255,255,255) )
		block_no_destroy  = font.render("Non-destructible block" , 0, (225,255,255) )
		block_To_destroy  = font.render("Destructible block" , 0, (225,255,255) )
		key_needed   = font.render("Key" , 0, (225,255,255) )
		door_needed  = font.render("Door" , 0, (225,255,255) )
		bomb 		 = font.render("Bomb" , 0, (225,255,255) )
		diamonds 	 = font.render("Diamond" , 0, (225,255,255) )

		controls	 = font.render("Controls", 0, (0,255,255))
		movement     = font.render("Movement keys:" , 0, (225,255,255) )
		placeBomb    = font.render("Place bomb:" , 0, (225,255,255) )
		movementKey	 = pygame.image.load("img/arrow_keys.png").convert_alpha()
		spaceKey	 = pygame.image.load("img/space_bar.png").convert_alpha()

		instructions = font.render("Instructions", 0, (0,255,255))
		rule1        = font.render("1. Move around the board placing bombs." , 0, (225,255,255) )
		rule2        = font.render("2. Find the key and open the door and get out of the maze." , 0, (225,255,255) )
		rule3        = font.render("3. Collect all possible diamonds before your enemies." , 0, (225,255,255) )
		rule4        = font.render("4. You lose if enemies collect more than half the diamonds." , 0, (225,255,255) )

		exit         = font.render("Exit --> Esc" , 0, (255,0,0) )

		while(rules):

			for eventos in pygame.event.get():

				keys = pygame.key.get_pressed()

				if(keys[K_ESCAPE]):
					rules = False

			self.display_surf.blit( image, (0,0) )
			self.display_surf.blit( title, (400,20))
			self.display_surf.blit( components, (30,70))
			##############################
			self.display_surf.blit( bomberman, (70,120))
			self.display_surf.blit(self.bomber.image, (310,110))
			self.display_surf.blit( enemys, (630,120))
			self.display_surf.blit(self.first_enemy.image, (800,110))
			##############################
			self.display_surf.blit( block_no_destroy, (70,170))
			self.display_surf.blit(self._block_surf, (400,160))
			self.display_surf.blit( key_needed, (630,170))
			self.display_surf.blit(self._key, (800,175))
			###############################
			self.display_surf.blit( block_To_destroy, (70,220))
			self.display_surf.blit(self._block_to_destroy, (400,215))
			self.display_surf.blit( door_needed, (630,220))
			self.display_surf.blit(self._door, (800,210))
			###############################
			self.display_surf.blit( bomb, (70,270))
			self.display_surf.blit(self.bomba.image, (180,260))
			self.display_surf.blit( diamonds, (630,270))
			self.display_surf.blit(self._diamond, (805,275))
			###############################
			self.display_surf.blit( controls, (30,330))
			self.display_surf.blit( movement, (70,380))
			self.display_surf.blit( movementKey, (320,350))
			self.display_surf.blit( placeBomb, (630,380))
			self.display_surf.blit( spaceKey, (805,360))
			###############################
			self.display_surf.blit( instructions, (30,450))
			self.display_surf.blit( rule1, (30,500))
			self.display_surf.blit( rule2, (30,550))
			self.display_surf.blit( rule3, (30,600))
			self.display_surf.blit( rule4, (30,650))

			self.display_surf.blit( exit,  (400,700))
			pygame.display.update()

	'''Method to verify the movements of the enemyes, this method use the
movements moveLeft, moveRight, moveUp and moveDown also use recognizeTheMovement
to check what kind of movement is available'''
	def direction_chosen_by_enemy(self, Enemy):
		if (
			Enemy.left_move_activate is True and 
			Enemy.right_move_activate is False and
			Enemy.up_move_activate is False and
			Enemy.down_move_activate is False
		):
			Enemy.moveLeft()
			Enemy.update("left",Enemy.x, Enemy.y)
			Enemy.recognizeTheMovement(0)
			self.maze.diamond_list = self.maze.takeDiamond(Enemy.x, Enemy.y, 'l', 'e')
		if (
			Enemy.right_move_activate is True and 
			Enemy.left_move_activate is False and
			Enemy.up_move_activate is False and
			Enemy.down_move_activate is False
		):
			Enemy.moveRigth()
			Enemy.update("right",Enemy.x, Enemy.y)
			Enemy.recognizeTheMovement(1)# we activate the left movement
			self.maze.diamond_list = self.maze.takeDiamond(Enemy.x, Enemy.y, 'r', 'e')
		if (
			Enemy.up_move_activate is True and 
			Enemy.left_move_activate is False and
			Enemy.right_move_activate is False and
			Enemy.down_move_activate is False
		):
			Enemy.moveUp()
			Enemy.update("up",Enemy.x, Enemy.y)
			Enemy.recognizeTheMovement(2)
			self.maze.diamond_list = self.maze.takeDiamond(Enemy.x, Enemy.y, 'u', 'e')
		if (
			Enemy.down_move_activate is True and 
			Enemy.left_move_activate is False and
			Enemy.up_move_activate is False and
			Enemy.right_move_activate is False
		):
			Enemy.moveDown()
			Enemy.update("down",Enemy.x, Enemy.y)
			Enemy.recognizeTheMovement(3)
			self.maze.diamond_list = self.maze.takeDiamond(Enemy.x, Enemy.y, 'd', 'e')

	'''This method handle the direction of any of ours enemies, if the enemy was "destroyed" 
It won't take any direction anymore, we disable the visibility and the movements with
boolean variables'''
	def handle_directions(self):
		if self.first_enemy.enable is True:
			self.direction_chosen_by_enemy(self.first_enemy)
		if self.second_enemy.enable is True:
			self.direction_chosen_by_enemy(self.second_enemy)
		if self.third_enemy.enable is True:
			self.direction_chosen_by_enemy(self.third_enemy)	
					
	'''Method to verify if any enemy has a collision with the player. If the collision happens then
the bomberman has to update his position and decrement his lives'''
	def verify_crash(self):
		if(self.bomber.checkPlayerAndEnemy(self.list_of_enemies) is True):
			self.bomber.simple_update(self.bomber.x, self.bomber.y)
			self.bomber.lives = self.bomber.lives - 1

	'''Method to change to state of the avatars to enable or to unable'''
	def change_state_avatars(self, flag):
		if flag == 1:# if the flag is 1 we must turn off the enemies
			self.first_enemy.enable =  False
			self.second_enemy.enable = False
			self.third_enemy.enable = False
			self.bomber.enable = False
		else:# otherwise we must  turn on the enemies
			self.first_enemy.enable =  True
			self.second_enemy.enable = True
			self.third_enemy.enable = True
			self.bomber.enable = True

	''' Main method to show and handle the events on the screen '''
	def on_execute(self, turn):
		if self.on_init() == False:
			self._running = False
		
		clock = pygame.time.Clock()

		if (turn == 0):
			self.start()
		#bomber = BomberMan.bomberman(windowWidth/2,windowHeight/2);
		self.sounds_of_game.start_song_in_game(2)#  start the main song of the game

		while (self._running):
			self.bomb = False
			pygame.event.pump()
			keys = pygame.key.get_pressed()

			if self.bomber.enable is True:		
				
				if (self.maze.win):
					self.you_win_screen()
					#self.change_state_avatars(1)

				if (keys[K_RIGHT]):
					#self.bomber.moveRigth() 
					for event in pygame.event.get():
						pass
					self.sounds_of_game.play_sound(2)# play the footstep sound
					self.bomber.moveRigth() 
					self.bomber.handle_event(event,self.bomber.x, self.bomber.y)
					self.maze.diamond_list = self.maze.takeDiamond(self.bomber.x, self.bomber.y, 'r', 'p')
					#self.maze.openDoor(self.bomber.x, self.bomber.y)
				
				elif (keys[K_LEFT]):
					#self.bomber.moveLeft()
					for event in pygame.event.get():
						pass
					self.sounds_of_game.play_sound(2)# play the footstep sound
					self.bomber.moveLeft()
					self.bomber.handle_event(event,self.bomber.x, self.bomber.y)
					self.maze.diamond_list = self.maze.takeDiamond(self.bomber.x, self.bomber.y, 'l', 'p')
					#self.maze.openDoor(self.bomber.x, self.bomber.y)
				
				elif (keys[K_DOWN]):
					#self.bomber.moveDown()
					for event in pygame.event.get():
						pass
					self.sounds_of_game.play_sound(2)# play the footstep sound
					self.bomber.moveDown()
					self.bomber.handle_event(event,self.bomber.x, self.bomber.y)
					self.maze.diamond_list = self.maze.takeDiamond(self.bomber.x, self.bomber.y, 'd', 'p')
					#self.maze.openDoor(self.bomber.x, self.bomber.y)
					
				elif (keys[K_UP]):
					
					for event in pygame.event.get():
						pass
					self.sounds_of_game.play_sound(2)# play the footstep sound
					self.bomber.moveUp()
					self.bomber.handle_event(event,self.bomber.x, self.bomber.y)
					self.maze.diamond_list = self.maze.takeDiamond(self.bomber.x, self.bomber.y, 'u', 'p')
					#self.maze.openDoor(self.bomber.x, self.bomber.y)

				if (keys[K_SPACE]) and self.pressSpace:
					self.bomb = True
					self.now = time.time() # get the current time when the user press the button
					self.wait = self.now + 3 # time to enable the button and time for exploding the bomb
					self.pressSpace = False

				if (keys[K_ESCAPE]):
					self._running = False

				if (keys[K_F11]):
					self.rules()

			# Game Over 
			if (math.floor((self.maze.total_diamonds/2)+1) <= self.maze.enemy_diamonds):
				self.gameOver('d')
				self.change_state_avatars(1)
			if (self.bomber.lives == 0):
				self.gameOver('l')
				self.change_state_avatars(1)

			if self.maze.key_reveal is True:
				self.maze.openDoor(self.bomber.x, self.bomber.y)
			pygame.display.flip()			
			clock.tick(20)
			
			#movement of the enemies
			self.handle_directions()

			#verify the bomb explosion
			self.verify_crash()
		
			self.on_render()

		self.on_cleanup()


	def button(self, msg, posX, posY, posX2, posY2, color, color2, action):
		font = pygame.font.Font( None, 32)
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if posX+posX2 > mouse[0] > posX and posY+posY2 > mouse[1] > posY:
			pygame.draw.rect(self.display_surf, color,(posX,posY,posX2,posY2))

			if click[0] == 1:
				if action == 'r':
					self.restart()
				elif action == 'q':
					self._running = False
		else:
			pygame.draw.rect(self.display_surf, color2,(posX,posY,posX2,posY2))

		text = font.render(msg, 0, (255,255,255))
		textRect = text.get_rect()
		textRect.center = ( (posX+(posX2/2)), (posY+(posY2/2)) )
		self.display_surf.blit(text, textRect)


	''' Method that restarts the position of the avatar '''
	def restart_avatar(self, avatar, posX, posY):
		avatar.rect.x = posX
		avatar.rect.y = posY
		avatar.x = posX
		avatar.y = posY

	'''' Method to reset the elements of the maze and the avatar to their initial position'''
	def restart(self):
		self.sounds_of_game.start_song_in_game(1) # restart the main song

		self.bomber.lives = 3
		self.change_state_avatars(2)
		self.bomber.key = False
		#self.bomber.enable = True
		#restart the init values for the avatars in the screen
		self.restart_avatar(self.bomber, 50, 50)
		self.restart_avatar(self.first_enemy, 655, 655)
		self.restart_avatar(self.second_enemy, 50, 655)
		self.restart_avatar(self.third_enemy, 655, 50)

		self.maze.restart()

		# to check in the bomber class the valid movements
		self.bomber.disable_block_list = self.maze.saveInvalidPositionsToMove() 

		#We share the invalid movements to each enemy
		self.first_enemy.disable_block_list = self.bomber.disable_block_list
		self.second_enemy.disable_block_list = self.bomber.disable_block_list
		self.third_enemy.disable_block_list = self.bomber.disable_block_list

		self.on_execute(1)

	'''Method that restarts or ends the game according to the player's decision'''
	def gameOver(self, type):
		#self.songs.stop_song_in_game()# stop the main song
		#self.songs.start_song_in_game(3)
		if(type == 'd'):
			self.display_surf.blit(self._game_over_diamond, (200,200))
		elif(type == 'l'):
			self.display_surf.blit(self._game_over_lives, (200,200))

		self.button('Yes', 360, 512, 50, 25, self.green, self.bright_green, 'r')
		self.button('No', 500, 512, 50, 25, self.red, self.bright_red, 'q')	

	'''Method that the screen displays when you win the game'''
	def you_win_screen(self):
		self.sounds_of_game.stop_song_in_game()#stop the main song
		self.sounds_of_game.start_song_in_game(4)#start winner song
		win        	 = True
		font		 = pygame.font.Font( None, 32)
		image_win    = pygame.image.load("img/you_win.png")

		#win_text    = font.render("Press space bar to play again or ESC for exit" , 0, (225,255,255) )
		playAgain	 = font.render("Play Again" , 0, (225,255,255) )
		quitGame	 = font.render("Quit" , 0, (225,255,255) )
		x_quitGame	 = 555
		y_quitGame	 = 295
		x2_quitGame	 = 675
		y2_quitGame	 = 335

		while(win):

			for eventos in pygame.event.get():
				keys = pygame.key.get_pressed()
				if(keys[K_ESCAPE]):
					win = False
					self._running = False

				if eventos.type == pygame.MOUSEBUTTONDOWN:
					#if the mouse is clicked on the button Quit the game is terminated 
					if x_quitGame <= mouse[0] <= x2_quitGame and y_quitGame <= mouse[1] <= y2_quitGame: 
						win = False
						self._running = False
					#if the mouse is clicked on the button PlayAgain the game is start
					if x_quitGame-300 <= mouse[0] <= x2_quitGame-300 and y_quitGame <= mouse[1] <= y2_quitGame: 
						win = False
						self.restart()

			self.display_surf.blit( image_win, (200,200) )

			# stores the (x,y) coordinates into the variable as a tuple 
			mouse = pygame.mouse.get_pos() 
			
			# if mouse is hovered on a button Quit it changes to lighter shade  
			if x_quitGame <= mouse[0] <= x2_quitGame and y_quitGame <= mouse[1] <= y2_quitGame: 
				pygame.draw.rect(self.display_surf, self.red, [x_quitGame, y_quitGame, 120,40]) 
				
			else: 
				pygame.draw.rect(self.display_surf, self.bright_red, [x_quitGame, y_quitGame, 120,40]) 
			
			# if mouse is hovered on a button PlayAgain it changes to lighter shade  
			if x_quitGame-300 <= mouse[0] <= x2_quitGame-300 and y_quitGame <= mouse[1] <= y2_quitGame: 
				pygame.draw.rect(self.display_surf, self.green, [x_quitGame-300, y_quitGame, 120,40]) 
				
			else: 
				pygame.draw.rect(self.display_surf, self.bright_green, [x_quitGame-300, y_quitGame, 120,40]) 
			
			# superimposing the texts onto our buttons
			self.display_surf.blit(quitGame , (x_quitGame+30, y_quitGame+7))
			self.display_surf.blit(playAgain , (x_quitGame-295, y_quitGame+7))

			pygame.display.update()


if __name__=="__main__":
	controller = Controller()
	controller.on_execute(0)