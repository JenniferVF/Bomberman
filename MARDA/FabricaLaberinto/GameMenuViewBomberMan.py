
from GameMenuView import *
from pygame.locals import *
import pygame
import os.path

'''
Class that shows and manages the Menu screen specific to the BomberMan Game
'''
class GameMenuViewBomberMan(GameMenuView):
    
    pygame.init()

    def __init__(self, windowWidth, windowHeight):
        ''' Construct a new GameMenuViewBomberMan object 
            :param windowWidth: width of screen BomberMAn game
            :param windowHeight: Height of screen BomberMAn game '''
        super().__init__(windowWidth, windowHeight)


    def gameStart(self, size, imagePath, sounds):
        ''' Displays the initial game screen of BomberMan GAme (menu screen) 
            :param size: size of screen
            :param imagePath: path of directory where the image is located '''
        super().gameStart(size, imagePath)       
        textStart = self.font.render("Start Game (F10)" , 0, (225,131,31) )
        textRules = self.font.render("Game Rules (F11)" , 0, (225,131,31) ) 
        self.display_surf.blit( self.image, (0,0) )
        self.display_surf.blit( textStart, (400,645))
        self.display_surf.blit( textRules, (400,700))
        sounds.start_interlude_song()
       
    def rules(self,  size, SysFontType, imagePath):
        ''' Displays the BomberMan Game's rules (rules screen) 
            :param sizeFont: size of screen
            :param sysFontType: Font's type of screen
            :param imagePath: path of directory where the image is located '''
        super().rules( size, SysFontType, imagePath)  

        rules        = True
        title        = self.font.render("Game Rules" , 0, (0,0,255) )
        components 	 = self.font.render("Game Components:", 0, (0,255,255))
        bomberman    = self.font.render("BomberMan" , 0, (255,255,255) )
        enemys       = self.font.render("Enemy" , 0, (255,255,255) )
        block_no_destroy  = self.font.render("Non-destructible block" , 0, (225,255,255) )
        block_To_destroy  = self.font.render("Destructible block" , 0, (225,255,255) )
        key_needed   = self.font.render("Key" , 0, (225,255,255) )
        door_needed  = self.font.render("Door" , 0, (225,255,255) )
        bomb 		 = self.font.render("Bomb" , 0, (225,255,255) )
        diamonds 	 = self.font.render("Diamond" , 0, (225,255,255) )
        controls	 = self.font.render("Controls", 0, (0,255,255))
        movement     = self.font.render("Movement keys:" , 0, (225,255,255) )
        placeBomb    = self.font.render("Place bomb:" , 0, (225,255,255) )
        movementKey	 = pygame.image.load(os.path.join(os.path.dirname(__file__),"img/arrow_keys.png")).convert_alpha()
        spaceKey	 = pygame.image.load(os.path.join(os.path.dirname(__file__),"img/space_bar.png")).convert_alpha()
        instructions = self.font.render("Instructions", 0, (0,255,255))
        rule1        = self.font.render("1. Move around the board placing bombs." , 0, (225,255,255) )
        rule2        = self.font.render("2. Find the key and open the door and get out of the maze." , 0, (225,255,255) )
        rule3        = self.font.render("3. Collect all possible diamonds before your enemies." , 0, (225,255,255) )
        rule4        = self.font.render("4. You lose if enemies collect more than half the diamonds." , 0, (225,255,255) )
        exit         = self.font.render("Exit --> Esc" , 0, (255,0,0) )

        self.display_surf.blit( self.image, (0,0) )
        self.display_surf.blit( title, (400,20))
        self.display_surf.blit( components, (30,70))
        ##############################
        self.display_surf.blit( bomberman, (70,120))
        #self.display_surf.blit(self.bomber.image, (310,110))
        self.display_surf.blit( enemys, (630,120))
        #self.display_surf.blit(self.first_enemy.image, (800,110))
        ##############################
        self.display_surf.blit( block_no_destroy, (70,170))
        #self.display_surf.blit(self._block_surf, (400,160))
        self.display_surf.blit( key_needed, (630,170))
        #self.display_surf.blit(self._key, (800,175))
        ###############################
        self.display_surf.blit( block_To_destroy, (70,220))
        #self.display_surf.blit(self._block_to_destroy, (400,215))
        self.display_surf.blit( door_needed, (630,220))
        #self.display_surf.blit(self._door, (800,210))
        ###############################
        self.display_surf.blit( bomb, (70,270))
        #self.display_surf.blit(self.bomba.image, (180,260))
        self.display_surf.blit( diamonds, (630,270))
        #self.display_surf.blit(self._diamond, (805,275))
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