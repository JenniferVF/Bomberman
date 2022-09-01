from GameView import *
from pygame.locals import *
import pygame
import os.path
import time

'''
Class that shows and manages the Game screen specific to the BomberMan Game
'''
class GameViewBomberMan(GameView):

	pygame.init()

	def __init__(self, windowWidth, windowHeight):
		''' Construct a new GameViewBomberMan object 
            :param windowWidth: width of screen BomberMAn game
            :param windowHeight: Height of screen BomberMAn game '''
		super().__init__(windowWidth, windowHeight)
		self.display_surf = os.path.join(os.path.dirname(__file__), "img/background.PNG")
		self.image_surf = os.path.join(os.path.dirname(__file__), "img/block_indestructible.jpg")
		self.block_type1 =  os.path.join(os.path.dirname(__file__),"img/block_destructible.png")
		self.element_type1 = os.path.join(os.path.dirname(__file__), "img/diamond_maze.png")
		self.element_type2 = os.path.join(os.path.dirname(__file__),"img/door.png" )
		self.key = os.path.join(os.path.dirname(__file__),"img/key.png" )
		self.diamond = os.path.join(os.path.dirname(__file__),"img/diamond.png" )
		self.live = os.path.join(os.path.dirname(__file__),"img/live.png" )

	def setBackgroundImage(self, imagePath, sounds):
		''' Set the background image of the BomberMan Game
            :param imagePath: path of directory where the image is located 
			:param sounds; sound to use '''
		super().setBackgroundImage(imagePath)
		#sounds.start_song_in_game()
	
	
	def drawElementInScreen(self,N, maze):
		''' This method draws on the screen in accordance with the values of the maze list.
		If the element in the list is 1 we put in the screen an indestructible block.
		If the element in the list is 2 we put in the screen a destructible block.
		And finally, if the element in the list is 0 we don't put anything on the screen.
			:param maze: game's maze'''
		bx = 0
		by = 0
		for i in range(0,N*N):
			if maze[ bx + (by*N)] == 1: # print 
				super().drawElementInScreen(self.image_surf,bx * 50, by * 50)
				#self.display_surf.blit(self.image_surf,(bx * 50, by * 50))# 50 is the number of pixels 'printed' in every iteration
			if maze[ bx + (by*N)] == 2 or maze[ bx + (by*N)] == 4:# destructible block
				super().drawElementInScreen(self.block_type1,bx * 50, by * 50)
				#self.display_surf.blit(self.block_type1,(bx * 50, by * 50))
			if maze[ bx + (by*N)] == 5:#element of the maze (diamond)
				super().drawElementInScreen(self.element_type1,bx * 50, by * 50)
				#self.display_surf.blit(self.element_type1,(bx * 50, by * 50))
			if maze[ bx + (by*N)] == 6:	#element of the maze  (door)
				super().drawElementInScreen(self.element_type2,bx * 50, by * 50)
				#self.display_surf.blit(self.element_type2,(bx * 50, by * 50))
			bx = bx + 1
			if bx > N-1:
				bx = 0
				by = by + 1

	
	def keyReveal(self, maze, player, key_time):
		''' Show the key when you find it 
			:param maze: game's maze
			:param player: game's player
			:param key_time: time the key was found '''
		if maze.key_reveal == True and player.key == False:
			keyX = player.x
			keyY = player.y

			if (key_time > time.time()): # if the time to wait isn't complete, display the key in the screen
				super().drawElementInScreen(self.key, keyX, keyY-15)
			else:
				player.key = True
	

	def showConsole(self, posX1, posY1, posX2, posY2, consoleColor, frameColor, maze, player, enemy1, enemy2, enemy3, key_time):
		''' Displays the game tool information console of BomberMan Game
            :param posX1: x coordinate 1 where the console will be placed
            :param posXY1: y coordinate 1 where the console will be placed
            :param posX2: x coordinate 2 where the console will be placed
            :param posY2: y coordinate 2 where the console will be placed
            :param consoleColor: console's color
            :param frameColor: frame's color '''
		super().showConsole(posX1, posY1, posX2, posY2, consoleColor, frameColor)
		posX = 820
		enemy_diamonds = enemy1.diamonds_taken + enemy2.diamonds_taken + enemy3.diamonds_taken

		fontLive = pygame.font.Font(None, 30)
		liveText = fontLive.render("Lives: " , 0, (225,255,255))
		keyText = fontLive.render("Key: " , 0, (225,255,255) )
		diamondText = fontLive.render("Diamonds: " , 0, (225,255,255))
		diamondWon = fontLive.render("Won: " + str(player.diamonds_taken), 0, (0,255,0))
		diamondLost = fontLive.render("Lost: " + str(enemy_diamonds), 0, (255,0,0))
		diamondCount = fontLive.render(str(maze.diamonds_taken), 0, (255,255,255))
		
		self.keyReveal(maze, player, key_time)

		super().drawTextInScreen(liveText, 754, 20)
		super().drawTextInScreen(keyText, 754, 55)
		super().drawTextInScreen(diamondText, 754, 90)
		super().drawElementInScreen(self.diamond, 865, 88)
		super().drawTextInScreen(diamondCount, 900, 90)
		super().drawTextInScreen(diamondWon, 865, 120)
		super().drawTextInScreen(diamondLost, 865, 145)

		for i in range(player.lives):
			super().drawElementInScreen(self.live, posX, 20)
			posX = posX + 25

		if player.key:
			super().drawElementInScreen(self.key, 800, 55)

	def clean_up(self):
		''' Refresh the screen '''
		super().clean_up()

	def drawPlayer(self, player):
		'''methods used to animate sprites that move on the X and Y directions
			:param player: game's player '''
		super().drawPlayer(player)

	def get_frame(self, frame_set, player):
		''' Get the frame '''
		return super().get_frame(frame_set, player)

	def clip(self, clipped_rect, player):
		return super().clip(clipped_rect, player)

	def update(self, direction, player):
		''' Update the player's position on the BomberMan game screen 
            :param direction: player's direction
            :param player: game's player'''
		super().update(direction, player)

	def handle_event(self, event, player):
		''' Make the player move by clicking a key 
            :param event: event occurred
            :param player: game's player '''
		super().handle_event(event, player)

	def simple_update(self, x, y):
		''' Update the position by collision with enemy 
            :param x: x coordinate
            :param y: y coordinate '''
		super().simple_update(x, y)
		self.rect.x = x
		self.rect.y = y

	def updateObject(self, object):       
		'''methods used to animate sprites that do not move in X and Y directions (in this case, the bomb)
			:param player: player to animate''' 
		super().updateObject(object)

	def positionObject(self, pos, object):
		''' method that positions an object on the BomberMAn Game screen 
            :param pos: object's position
            :param object: object to place '''
		super().positionObject(pos, object)

	def setFrameObject(self, object):
		''' Set of frame of object
            :param object: object '''
		super().setFrameObject(object)
		
	def gameWin(self, sounds):
		''' Displays the victory screen upon winning the BomberMan game 
			:param sounds: sounds to use'''
		sounds.start_win_game_sound()
		self.win = True
		font		 = pygame.font.Font( None, 32)
		image_win    = pygame.image.load(os.path.join(os.path.dirname(__file__), "img/you_win.png"))
		playAgain	 = font.render("Play Again" , 0, (225,255,255))
		quitGame	 = font.render("Quit" , 0, (225,255,255) )
		x_quitGame	 = 555
		y_quitGame	 = 295
		x2_quitGame	 = 675
		y2_quitGame	 = 335
		#Colors
		green = (0,255,0)
		bright_green = (0,150,0)
		red = (255,0,0)
		bright_red = (150,0,0)
		
		while (self.win):

			for eventos in pygame.event.get():
				keys = pygame.key.get_pressed()
				if(keys[K_ESCAPE]):
					win = False
					
				if eventos.type == pygame.MOUSEBUTTONDOWN:
					#if the mouse is clicked on the button Quit the game is terminated 
					if x_quitGame <= mouse[0] <= x2_quitGame and y_quitGame <= mouse[1] <= y2_quitGame: 
						win = False
						return 2
						
					#if the mouse is clicked on the button PlayAgain the game is start
					if x_quitGame-300 <= mouse[0] <= x2_quitGame-300 and y_quitGame <= mouse[1] <= y2_quitGame: 
						win = False
						return 1

			self._display_surf.blit( image_win, (200,200) )
			#stores the (x,y) coordinates into the variable as a tuple 
			mouse = pygame.mouse.get_pos() 
			
			# if mouse is hovered on a button Quit it changes to lighter shade
			if x_quitGame <= mouse[0] <= x2_quitGame and y_quitGame <= mouse[1] <= y2_quitGame:
				pygame.draw.rect(self._display_surf, red, [x_quitGame, y_quitGame, 120,40])
			else:
				pygame.draw.rect(self._display_surf, bright_red, [x_quitGame, y_quitGame, 120,40])
				
			# if mouse is hovered on a button PlayAgain it changes to lighter shade
			if x_quitGame-300 <= mouse[0] <= x2_quitGame-300 and y_quitGame <= mouse[1] <= y2_quitGame:
				pygame.draw.rect(self._display_surf, green, [x_quitGame-300, y_quitGame, 120,40])
			else:
				pygame.draw.rect(self._display_surf, bright_green, [x_quitGame-300, y_quitGame, 120,40])
				
			#superimposing the texts onto our buttons
			self._display_surf.blit(quitGame , (x_quitGame+30, y_quitGame+7))
			self._display_surf.blit(playAgain , (x_quitGame-295, y_quitGame+7))
			
			#sounds.start_win_game_sound()
			pygame.display.update()
	def gameOver(self, flag, sounds):
		''' Displays the Game Over screen the BomberMan game 
			:param flag: indicates the reason why it was lost
			:param sounds: sounds to use'''
		gameOver = True
		font		 = pygame.font.Font( None, 32)

		if (flag == 'd'):
			image_GameOver    = pygame.image.load(os.path.join(os.path.dirname(__file__), "img/game_over_diamond.png"))
		else:
			image_GameOver    = pygame.image.load(os.path.join(os.path.dirname(__file__), "img/game_over_lives.png"))

		#Colors
		green = (0,255,0)
		bright_green = (0,150,0)
		red = (255,0,0)
		bright_red = (150,0,0)
		#sounds.start_lost_game_sound()
		self._display_surf.blit( image_GameOver, (200,200) )
		restart = self.button('Yes', 360, 512, 50, 25, green, bright_green, 'r')
		quit = self.button('No', 500, 512, 50, 25, red, bright_red, 'q')
			
		if (restart == 1):
			return 1
		elif (quit == 2):
			return 2
			
		pygame.display.update()


	def button(self, msg, posX, posY, posX2, posY2, color, color2, action):
		''' Displays button in the screen in BomberMan Game
			:param msg; message of button
            :param posX1: x coordinate 1 where the button will be placed
            :param posXY1: y coordinate 1 where the button will be placed
            :param posX2: x coordinate 2 where the button will be placed
            :param posY2: y coordinate 2 where the button will be placed
            :param color: button's color
			:param color2: button's color 2
            :param action: action that is carried out when the button is clicked '''
		font = pygame.font.Font( None, 32)
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		roq = 0

		# if mouse is hovered on a button it changes to lighter shade
		if posX+posX2 > mouse[0] > posX and posY+posY2 > mouse[1] > posY:
			pygame.draw.rect(self._display_surf, color,(posX,posY,posX2,posY2))

			if click[0] == 1:
				if action == 'r':
					roq = 1
				elif action == 'q':
					roq = 2
		else:
			pygame.draw.rect(self._display_surf, color2,(posX,posY,posX2,posY2))

		text = font.render(msg, 0, (255,255,255))
		textRect = text.get_rect()
		textRect.center = ( (posX+(posX2/2)), (posY+(posY2/2)) )
		self._display_surf.blit(text, textRect)

		return roq


	def drawTextInScreen(self, text, posX, posY):
		'''Method to print text in the screen
           :param text: text to print
           :param x_coordinate: X coordinate where thetext will be placed
           :param y_coordinate: Y coordinate where the text will be placed '''
		super().drawTextInScreen(text, posX, posY)