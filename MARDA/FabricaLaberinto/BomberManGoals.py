#Class specific product for Bomberman objectives

from Goals import *
from GameView import *

'''
Class that implements the functionalities and characteristics of the specific objects of the BomberMan game
such as diamonds, the key, etc.
'''
class BomberManGoals(Goals):

    def __init__(self):
        ''' Construct a new "BomberManGoals" object '''
        super().__init__()
        self.totalDiamonds = 8
        self.totalDoor = 1
        self.totalKey = 1


    def placeObject(self, maze):
        ''' Place the game objects in the maze of game 
            :param maze: game's maze '''
        super().placeObject(maze, 5, self.totalDiamonds)
        super().placeObject(maze, 6, self.totalDoor)
        super().placeObject(maze, 4, self.totalKey)

    
    def placeObjectInPosition(self, maze, objectValue, positionObject):
        ''' Place the game objects a specific position in the maze of game 
            :param maze: Maze of game
            :param objectValue: Value of the object in the maze of game
            :param positionObject: Position of the maze where you want to place the object '''
        super().placeObjectInPosition(maze, objectValue, positionObject)

    
    def openDoor(self, x_position, y_position, door, key):
        ''' Method for open the door and win the game 
            :param x_position: X coordinate of where the BomberManAvatar is located
            :param y_position: Y coordinate of where the BomberManAvatar is located
            :param door: Door position information
            :param key: true if the key needed to open the door and win has already been found, false otherwise 
            :return: True if you have open the door, false otherwise'''
        self.win = False
        if (door.first_range_x <= x_position <= door.first_range_x  
        and door.first_range_y <= y_position <= door.first_range_y):
            if door.ocuppied == 6:
                if key:
                    self.win = True
        return self.win

    
    def takeDiamond(self, direction, diamond_list, maze, player):
        ''' Method that controls the taking of diamonds according to the position of the player 
            :param direction: player address
            :param diamond_list: list of information of the squares in which a diamond is found
            :param maze: maze of the game
            :player: player of game '''
        self.list_aux = []
        for i in diamond_list:
            if i.ocuppied == 5: #diamond in the maze
                if direction == 'r':
                    if (
                        ((i.first_range_x <= (player.x + 44) <= i.second_range_x) and (i.first_range_y <= player.y < i.second_range_y)) 
                        or ((i.first_range_x <= (player.x + 44) <= i.second_range_x) and (i.first_range_y <= (player.y + 44) < i.second_range_y)) # we add to x pixel 44 to include every pixel of the bomb
                        ): # check to the rigth, len img = 44
                        maze[i.index_in_maze] = 0
                        self.list_aux.append(i.index_in_maze)
                        player.diamonds_taken = player.diamonds_taken + 1
                        
                if direction == 'l':
                    if (
                        ((i.first_range_x <= (player.x) < i.second_range_x) and (i.first_range_y < (player.y) < i.second_range_y)) 
                        or ((i.first_range_x <= (player.x) < i.second_range_x) and (i.first_range_y < (player.y + 44) < i.second_range_y))
                        ): # check to left
                        maze[i.index_in_maze] = 0
                        self.list_aux.append(i.index_in_maze)
                        player.diamonds_taken = player.diamonds_taken + 1
                        
                if direction == 'u':
                    if (
                        ((i.first_range_y <= (player.y) < i.second_range_y) and (i.first_range_x <= player.x < i.second_range_x)) 
                        #or ((i.first_range_y <= (y_position) < i.second_range_y) and (i.first_range_x <= (x_position + 44) < i.second_range_x))
                        ): # check upward
                        maze[i.index_in_maze] = 0
                        self.list_aux.append(i.index_in_maze)
                        player.diamonds_taken = player.diamonds_taken + 1
                        
                if direction == 'd':
                    if (
                        ((i.first_range_y <= (player.y + 44) <= i.second_range_y) and(i.first_range_x <= player.x < i.second_range_x)) 
                        or ((i.first_range_y <= (player.y + 44) <= i.second_range_y) and (i.first_range_x <= (player.x + 44) < i.second_range_x))
                        ): # check downward
                        maze[i.index_in_maze] = 0
                        self.list_aux.append(i.index_in_maze)
                        player.diamonds_taken = player.diamonds_taken + 1
                        
        self.updateDiamonds(self.list_aux, diamond_list)
        return diamond_list
        
    
    def updateDiamonds(self, list_aux, diamond_list):
        ''' Method to update the positions where the diamonds are
            :param list_aux: list that we will use as auxiliary
            :param diamond_list: list of information of the squares in which a diamond is found '''
        for n in range(len(list_aux)):
            counter = 0
            for i in diamond_list:
                if list_aux[n] == i.index_in_maze:
                    del diamond_list[counter]
                counter = counter + 1