#this class is equivalent to the client class of the Abstract Factory pattern
from Controller import *
from GameViewBomberMan import *
from GameMenuViewBomberMan import *

''' Controller class specific to the BomberMan game '''
class BomberManController(Controller, pygame.sprite.Sprite):

    def __init__(self):
        ''' Construct a new "BomberManController" object '''
        super().__init__()
        self.gameMenuViewBomberMan = GameMenuViewBomberMan(1000, 800)
        self.gameViewBomberMan = GameViewBomberMan(1000, 800) 

    def startGame(self):
        ''' Displays the initial game screen '''
        self.gameMenuViewBomberMan.gameStart(50, os.path.join(os.path.dirname(__file__), "img/startGame.PNG"), sounds )
        pygame.display.update()

        while(self.start):

            for eventos in pygame.event.get():

                keys = pygame.key.get_pressed()

                if (keys[K_F10]):
                    self.start = False
                    self.gaming = True
                    objects.placeObject(mazeBomberMan.maze)
                    mazeBomberMan.saveInvalidPositionsToMove()
                    #self.sounds.start_song_in_game()

                if (keys[K_F11]):
                    self.gameMenuViewBomberMan.rules(30, "berlin sans FB", os.path.join(os.path.dirname(__file__), "img/startRules.PNG"))
                    pygame.display.update()

                if (keys[K_ESCAPE]):
                    self.start = False
                    self.gameMenuViewBomberMan.gameStart(50, os.path.join(os.path.dirname(__file__), "img/startGame.PNG"), sounds)
                    pygame.display.update()

        sounds.stop_song_in_game()
        sounds.start_song_in_game()

    def play(self):
        ''' Show the maze screen and manage the game operation '''
        #elements are drawn on the screen
        self.gameViewBomberMan.setBackgroundImage(os.path.join(os.path.dirname(__file__), "img/background.PNG"), sounds)
        self.gameViewBomberMan.drawElementInScreen(mazeBomberMan.N, mazeBomberMan.maze)
        self.gameViewBomberMan.drawPlayer(avatarBomberMan)
        self.gameViewBomberMan.drawPlayer(enemyBomberMan)
        self.gameViewBomberMan.drawPlayer(enemyBomberMan2)
        self.gameViewBomberMan.drawPlayer(enemyBomberMan3)
        self.gameViewBomberMan.showConsole(745, 0, 255, 175, (0,0,0), (210,150,75), mazeBomberMan, avatarBomberMan, enemyBomberMan, enemyBomberMan2, enemyBomberMan3, mazeBomberMan.key_time)
        #the keys pressed to move the bomberman are reviewed
        keys = pygame.key.get_pressed()
        if (keys[K_ESCAPE]):
            self.gaming = False  

        if (keys[K_F11]):
            self.gameMenuViewBomberMan.rules(30, "berlin sans FB", os.path.join(os.path.dirname(__file__), "img/startRules.PNG"))
            pygame.display.update()
                    
        if keys[K_RIGHT]:
            for event in pygame.event.get():
                avatarBomberMan.moveRight()
                sounds.play_step_sound()
            objects.takeDiamond('r', mazeBomberMan.diamond_list, mazeBomberMan.maze, avatarBomberMan)
            #print("Key ->",",",self.avatarBomberMan.x,self.avatarBomberMan.y)

        if (keys[K_LEFT]):
            for event in pygame.event.get():
                avatarBomberMan.moveLeft()
                sounds.play_step_sound()
            objects.takeDiamond('l', mazeBomberMan.diamond_list, mazeBomberMan.maze, avatarBomberMan)
            #print("Key <-",",",self.avatarBomberMan.x,self.avatarBomberMan.y)

        if (keys[K_DOWN]):
            for event in pygame.event.get():
                avatarBomberMan.moveDown()
                sounds.play_step_sound()
            objects.takeDiamond('d', mazeBomberMan.diamond_list, mazeBomberMan.maze, avatarBomberMan)
            #print("Key v",",",self.avatarBomberMan.x,self.avatarBomberMan.y)

        if (keys[K_UP]):	
            for event in pygame.event.get():
                avatarBomberMan.moveUp()
                sounds.play_step_sound()
            objects.takeDiamond('u', mazeBomberMan.diamond_list, mazeBomberMan.maze, avatarBomberMan)
            #print("Key ^",",",self.avatarBomberMan.x,self.avatarBomberMan.y)

        if ((keys[K_SPACE]) and bomb.bomb_in_screen is False):
            #self.bomb.placeWeapons(self.avatarBomberMan.x, self.avatarBomberMan.y)
            bomb.saveBombCoordinates(avatarBomberMan.x, avatarBomberMan.y)
            bomb.bomb_in_screen = True
            self.gameViewBomberMan.setFrameObject(bomb)
            #controller.pressSpace = False

        if (bomb.bomb_in_screen):
            bomb.checkBombStatus(mazeBomberMan, list_of_enemies, avatarBomberMan, sounds)
            self.gameViewBomberMan.positionObject( (bomb.x, bomb.y), bomb )
            self.gameViewBomberMan.updateObject(bomb)
            self.gameViewBomberMan.drawPlayer(bomb)
                    
        #bomberman sprite animation
        for event in pygame.event.get():
            self.gameViewBomberMan.handle_event(event, avatarBomberMan )

        answer = self.winner(avatarBomberMan.x, avatarBomberMan.y, mazeBomberMan.door, mazeBomberMan.key_reveal)
        if(answer == 1):    #quiere jugar de nuevo
            self.restart()
        if(answer == 2):    #quiere salir del juego
            self.gaming = False

        answer = self.gameOver() 
        if(answer == 1):    #quiere jugar de nuevo
            self.restart()
        if(answer == 2):    #quiere salir del juego
            self.gaming = False
           
        #movement of the enemies and check the diamond taken
        enemyBomberMan.handle_direction()
        objects.takeDiamond(enemyBomberMan.direction[0], mazeBomberMan.diamond_list, mazeBomberMan.maze, enemyBomberMan)
        enemyBomberMan2.handle_direction()
        objects.takeDiamond(enemyBomberMan2.direction[0], mazeBomberMan.diamond_list, mazeBomberMan.maze, enemyBomberMan2)
        enemyBomberMan3.handle_direction()
        objects.takeDiamond(enemyBomberMan3.direction[0], mazeBomberMan.diamond_list, mazeBomberMan.maze, enemyBomberMan3)
        
        #verify crash
        avatarBomberMan.verify_crash(list_of_enemies)

        #enemy sprites
        self.gameViewBomberMan.update(enemyBomberMan.direction, enemyBomberMan )
        self.gameViewBomberMan.update(enemyBomberMan2.direction, enemyBomberMan2 )
        self.gameViewBomberMan.update(enemyBomberMan3.direction, enemyBomberMan3 )

        pygame.display.flip()
        pygame.display.update()
        
    def winner(self, x_position, y_position, door, key):
        ''' Check and establish when the game has been won 
            :param x_position: X coordinate of where the BomberManAvatar is located
            :param y_position: Y coordinate of where the BomberManAvatar is located
            :param door: Door position information
            :param key: true if the key needed to win has already been found, false otherwise 
            :return: True if you have won, false otherwise '''
        if(objects.openDoor(x_position, y_position, door, key)):
            answer = self.gameViewBomberMan.gameWin(sounds)
            return answer

    def gameOver(self):
        ''' Check and establish if the game has been lost
            :return: True if you have lost, false otherwise '''
        halfDiamonds = objects.totalDiamonds / 2
        diamondsAvailable = len(mazeBomberMan.diamond_list)

        if( (avatarBomberMan.diamonds_taken + diamondsAvailable) < halfDiamonds ):
            self.change_state_avatars(1)
            return self.gameViewBomberMan.gameOver('d', sounds)

        if (avatarBomberMan.lives == 0):
            self.change_state_avatars(1)
            return self.gameViewBomberMan.gameOver('l', sounds)
        
        
    def change_state_avatars(self, flag):
        '''Method to change to state of the avatars to enable or to unable
            :param flag: Indicates whether to enable or disable the characters '''
        if flag == 1:# if the flag is 1 we must turn off the enemies
            enemyBomberMan.enable =  False
            enemyBomberMan2.enable = False
            enemyBomberMan3.enable = False
            avatarBomberMan.enable = False
        else:# otherwise we must  turn on the enemies
            enemyBomberMan.enable =  True
            enemyBomberMan2.enable = True
            enemyBomberMan3.enable = True
            avatarBomberMan.enable = True

    def restart(self):
        ''' Restart the game '''
        self.gaming = True
        self.change_state_avatars(2)
        avatarBomberMan.restart((51,50), 51, 50)
        enemyBomberMan.restart((655,655), 655, 655)
        enemyBomberMan2.restart((50,655), 50, 655)
        enemyBomberMan3.restart((655,50), 655, 50)
        mazeBomberMan.key_reveal = False
        avatarBomberMan.key = False
        mazeBomberMan.restart()
        objects.placeObject(mazeBomberMan.maze)
        avatarBomberMan.disable_block_list = mazeBomberMan.saveInvalidPositionsToMove()
        enemyBomberMan.disable_block_list = avatarBomberMan.disable_block_list
        enemyBomberMan2.disable_block_list = avatarBomberMan.disable_block_list
        enemyBomberMan3.disable_block_list = avatarBomberMan.disable_block_list
        sounds.start_song_in_game()
       
if __name__=="__main__":
    ''' Main method with the logic and operation of the BomberMan Game '''
    controller = BomberManController()
    bmFactory     = BomberManFactory() 
    mazeBomberMan = bmFactory.createMaze()

    avatarBomberMan  = bmFactory.createAvatar( (51,50), 51, 50, 10, 3, "img/bomberMan.png")
    enemyBomberMan  = bmFactory.createEnemy( (655,655), 655, 655, 10, 1, "img/enemy.png" )
    enemyBomberMan2  = bmFactory.createEnemy( (50,655), 50, 655, 5, 1, "img/enemy.png" )
    enemyBomberMan3  = bmFactory.createEnemy( (655,50), 655, 50, 2.5, 1, "img/enemy.png")
    bomb = bmFactory.createWeapons((0,0), "img/Bomb.png")
    objects = bmFactory.createGoals()
    sounds = bmFactory.createSounds()
    avatarBomberMan.disable_block_list = mazeBomberMan.saveInvalidPositionsToMove()
    enemyBomberMan.disable_block_list = avatarBomberMan.disable_block_list
    enemyBomberMan2.disable_block_list = avatarBomberMan.disable_block_list
    enemyBomberMan3.disable_block_list = avatarBomberMan.disable_block_list
    list_of_enemies = []
    list_of_enemies.append(enemyBomberMan)
    list_of_enemies.append(enemyBomberMan2)
    list_of_enemies.append(enemyBomberMan3)

    controller.execute()




        





