#Abstract factory class

from abc import ABC, abstractmethod

'''
MARDA class that will allow to implement a factory of a specific maze game
'''
class GameFactory(ABC):

    @abstractmethod
    def createMaze(self):
        ''' Create a new maze object specific for specific Game '''
        pass

    @abstractmethod
    def createEnemy(self):
        ''' Create a new enemy object specific for specific Game '''
        pass

    @abstractmethod
    def createAvatar(self):
        ''' Create a new main character object for specific Game '''
        pass

    @abstractmethod
    def createWeapons(self):
        ''' Create a new weapons object specific for specific Game '''
        pass

    @abstractmethod
    def createGoals(self):
        ''' Create a new specific components object  for specific Game '''
        pass

    @abstractmethod
    def createSounds(self):
        ''' Create a new sounds object specific for specific Game '''
        pass





