import pygame
from .settings import Settings
import numpy as np
class Grid(Settings) :
    def __init__(self) -> None:
        super().__init__()
        self.settings = Settings()
        self.grid = [[np.random.choice([0,1]) for k in range(self.settings.grid_width)] for j in range(self.settings.grid_height)]
        self.height = self.settings.grid_height
        self.width = self.settings.grid_width
    
        


    def change(self,x,y) -> None :
        self.grid[x][y] = 1 - self.grid[x][y]
    
    def print(self,i,x,y,direction):
        '''print the grid'''
        print('step',i)
        print('X = ',x,'Y = ',y,'direction = ',direction)
        for ligne in self.grid:
            
            print(' '.join(['#' if cell == 1 else '.' for cell in ligne]))



    