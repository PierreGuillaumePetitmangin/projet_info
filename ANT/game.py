'''The Langton’s Ant is an automata made of an ant that walks on a square grid while coloring each tile according to the following process:

If the ant is on a white tile, it turns 90° on the right, otherwise it turns 90° on the left.
The ant inverts the coloring of a tile before leaving it. A white tile becomes a black one, and a black tile becomes a white one.
The ant move forward to an adjacent tile.
This process is repeated at each step. The ant starts on a white tile and follows the sequence of instructions described above.'''

import pygame
from .ant import Ant
from .grid import Grid
from .settings import Settings
import sys

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.grid = Grid()
        self.ant = Ant(5,5)
        self.grid_width = self.settings.grid_width
        self.grid_height = self.settings.grid_height


    def process(self) -> None:
        '''The ant is moving '''
        x, y = self.ant.x, self.ant.y
        if self.grid.grid[x][y] == 0:  #if the cell is white
            self.grid.change(x, y)
            self.ant.turn()  # Turn right
        else:  # if the cell is black
            self.grid.change(x, y)
            self.ant.turn()  # Turn left
        self.ant.move()
    
   

    def run_game(self) -> None:
        for i in range(10):
            self.process()
            self.grid.print(i,self.ant.x,self.ant.y,self.ant.direction)


            





