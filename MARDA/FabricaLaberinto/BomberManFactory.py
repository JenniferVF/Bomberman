# specific factory class Bomberman

from GameFactory import *
from BomberManMaze import *
from BomberManAvatar import *
from BomberManEnemy import *
from BomberManWeapons import *
from BomberManGoals import *
from BomberManSounds import *

'''
Factory of specific components for the BomberMan game
'''
class BomberManFactory(GameFactory):
   
    def createMaze(self):
        ''' Create a new maze object specific for BomberMan Game '''
        return BomberManMaze()

    def createAvatar(self, position,  init_x, init_y, init_speed, livesPlayer, imagePath):
        ''' Create a new BomberManAvatar object specific for BomberMan Game '''
        return BomberManAvatar(position, init_x, init_y, init_speed, livesPlayer, imagePath)

    def createEnemy(self, position,  init_x, init_y, init_speed, livesPlayer, imagePath):
        ''' Create a new enemy object specific for BomberMan Game '''
        return BomberManEnemy(position, init_x, init_y, init_speed, livesPlayer, imagePath)

    def createWeapons(self, position, imagePath):
        ''' Create a new weapons object specific for BomberMan Game '''
        return BomberManWeapons(position, imagePath)

    def createGoals(self):
        ''' Create a new goals object specific for BomberMan Game '''
        return BomberManGoals()

    def createSounds(self):
        ''' Create a new sounds object specific for BomberMan Game '''
        return BomberManSounds()
    