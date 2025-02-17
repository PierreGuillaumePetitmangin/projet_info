from .grid import Grid
from .tile import Tile
import numpy as np
from numpy import random as rd
import pygame
from .direction import Direction
from .settings import Settings
class Ant:
    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        self.direction = Direction.UP
        self.settings = Settings()
        self.grid = grid
        self.size = self.settings.tile_size

    def turn(self):
        if self.grid.grid[self.y][self.x] == 0:
            self.direction = Direction((self.direction.value + 1) % 4)
        else:
            self.direction = Direction((self.direction.value - 1) % 4)

    def move(self):
        if self.direction == Direction.UP:
            self.y = (self.y - 1) % self.size
        elif self.direction == Direction.RIGHT:
            self.x = (self.x + 1) % self.size
        elif self.direction == Direction.DOWN:
            self.y = (self.y + 1) % self.size
        elif self.direction == Direction.LEFT:
            self.x = (self.x - 1) % self.size
    
        


        

        