'''The Langton’s Ant is an automata made of an ant that walks on a square grid while coloring each tile according to the following process:

If the ant is on a white tile, it turns 90° on the right, otherwise it turns 90° on the left.
The ant inverts the coloring of a tile before leaving it. A white tile becomes a black one, and a black tile becomes a white one.
The ant move forward to an adjacent tile.
This process is repeated at each step. The ant starts on a white tile and follows the sequence of instructions described above.'''

import pygame
from ant import Ant
from grid import Grid
from settings import Settings
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Langton\'s Ant')
        self.grid = Grid(self.settings, self.screen)
        self.ant = Ant(self.grid)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.ant.move()
            self.grid.draw_grid()
            pygame.display.flip()



