
''' Class to handle the information about the range of pxls occupied'''
class InfoPixel:
    def __init__(self,first_range_x,second_range_x,first_range_y,second_range_y, ocuppied, index_in_maze):
        self.first_range_x = first_range_x
        self.second_range_x = second_range_x
        self.first_range_y = first_range_y
        self.second_range_y = second_range_y
        self.ocuppied = ocuppied # 1-undestructible, 2-destructible
        self.index_in_maze = index_in_maze # to save the index of the list where the element is located
