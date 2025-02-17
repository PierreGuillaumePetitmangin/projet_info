from .direction import Direction
from .grid import Grid
import numpy as np
from numpy import random as rd
class Ant :
    def __init__(self,x,y) -> None:
        self.y = x
        self.x = y
        self.direction = 0
        self._ant_color = (255, 0, 0)
        self.grid = Grid()
       

    def turn(self) -> None:

        if self.grid.grid[self.y][self.x] == 0:
            self.direction = (self.direction + 1) % 4   
        else:
            self.direction = (self.direction - 1) % 4
            


    def move(self) -> None:
        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        else:
            self.x -= 1
    
        


        

        