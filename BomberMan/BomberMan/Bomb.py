import pygame

class Bomb(pygame.sprite.Sprite):

    def __init__(self, position):
        self.sheet = pygame.image.load('img/Bomb.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 45, 45))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        clock = pygame.time.Clock()
        self.frame = 0
        self.bomb = {  0: (0, 0, 45, 45), 1: (45, 0, 45, 45), 2: (90, 0, 45, 45), 3: (135, 0, 45, 45),
                       4: (0, 0, 45, 45), 5: (45, 0, 45, 45), 6: (90, 0, 45, 45), 7: (135, 0, 45, 45),
                       8: (0, 0, 45, 45), 9: (45, 0, 45, 45), 10: (90, 0, 45, 45), 11: (135, 0, 45, 45),
                      12: (0, 0, 45, 45), 13: (45, 0, 45, 45), 14: (90, 0, 45, 45), 15: (135, 0, 45, 45),
                      16: (0, 0, 45, 45), 17: (45, 0, 45, 45), 18: (90, 0, 45, 45), 19: (135, 0, 45, 45),
                      20: (0, 0, 45, 45), 21: (45, 0, 45, 45), 22: (90, 0, 45, 45), 23: (135, 0, 45, 45),
                      24: (0, 0, 45, 45), 25: (45, 0, 45, 45), 26: (90, 0, 45, 45), 27: (135, 0, 45, 45),
                      28: (0, 0, 45, 45), 29: (45, 0, 45, 45), 30: (90, 0, 45, 45), 31: (135, 0, 45, 45),
                      32: (0, 0, 45, 45), 33: (45, 0, 45, 45), 34: (90, 0, 45, 45), 35: (135, 0, 45, 45),
                      36: (0, 0, 45, 45), 37: (45, 0, 45, 45), 38: (90, 0, 45, 45), 39: (135, 0, 45, 45),
                      40: (0, 0, 45, 45), 41: (45, 0, 45, 45), 42: (90, 0, 45, 45), 43: (135, 0, 45, 45),
                      44: (0, 0, 45, 45), 45: (45, 0, 45, 45), 46: (90, 0, 45, 45), 47: (135, 0, 45, 45),
                      48: (0, 0, 45, 45), 49: (45, 0, 45, 45), 50: (90, 0, 45, 45), 51: (135, 0, 45, 45),
                      52: (0, 0, 45, 45), 53: (45, 0, 45, 45), 54: (90, 0, 45, 45), 55: (135, 0, 45, 45),
                      #56: (0, 0, 45, 45), 57: (45, 0, 45, 45), 58: (90, 0, 45, 45), 59: (135, 0, 45, 45),
                      56: (0, 90, 45, 45), 57: (45, 90, 45, 45), 58: (90, 90, 45, 45), 59: (135, 90, 45, 45) }

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self):        
        self.clip(self.bomb)       
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def position(self, pos):
        self.rect.topleft = pos

    def setFrame(self):
        self.frame = 0
