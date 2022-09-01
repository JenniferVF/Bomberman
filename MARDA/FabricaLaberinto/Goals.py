#Abstract product class to generate the target elements of the game (keys, diamonds, chests, flags, etc).

from abc import ABC, abstractmethod
from random import randrange

'''
MARDA class that implements the game's specific tools and components
'''
class Goals(ABC):

    def __init__(self):  
        ''' Construct a new "Goals" object ''' 
        self.position = 0

    #place the game objects in the maze
    @abstractmethod
    def placeObject(self, maze, objectValue, total):
        ''' Place the game objects in the maze of game 
            :param maze: game's maze
            :param objectValue: object's value in maze
            :param total: number of object to place '''
        self.count = 0
        self.tam = len(maze)
        while (self.count < total):
            self.position = randrange(self.tam-1)
            if (maze[self.position] == 0 and self.position != 16 and self.position != 28
            and self.position != 208 and self.position != 196):
                maze[self.position] = objectValue
                #print("Coloque objeto => " + str(objectValue) + " en casilla " + str(self.i))
                self.count = self.count + 1

    @abstractmethod
    def placeObjectInPosition(self, maze, objectValue, positionObject):
        ''' Place the game objects a specific position in the maze of game 
            :param maze: Maze of game
            :param objectValue: Value of the object in the maze of game
            :param positionObject: Position of the maze where you want to place the object '''
        self.position = positionObject
        maze[self.position] = objectValue