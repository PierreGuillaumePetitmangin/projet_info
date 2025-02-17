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
from .exceptions import Exceptions
from .tile import Tile
from .direction import Direction

class Game:
    def __init__(self, settings) -> None:
        self.grid = Grid(settings.grid_size, settings.grid_size)
        self.ant = Ant(settings.grid_size // 2, settings.grid_size // 2, self.grid)
        self.steps = settings.steps
        self.gui = settings.gui
        self.direction = self.ant.direction

        
        if self.gui:
            print('gui')
            pygame.init()
            self.screen = pygame.display.set_mode((settings.screen_size, settings.screen_size))
            pygame.display.set_caption("Langton's Ant")
            self.clock = pygame.time.Clock()
            self.tile_size = settings.tile_size

    def process(self) -> None:
        x, y = self.ant.x, self.ant.y
        self.ant.turn()
        self.grid.change(x, y)
        self.ant.move()

    def run(self) -> None:
        for step in range(self.steps):
            if self.gui :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            self.process()
            if not self.gui:
                self.grid.print_grid(step, self.ant.x, self.ant.y, self.ant.direction)
            else:
                self.render()
                self.clock.tick(10)
        if self.gui:
            pygame.quit()

    def draw_arrow(self,x, y, direction):
        if direction == Direction.UP:  # Haut
            points = [(x, y), (x - 5, y + 10), (x + 5, y + 10)]
        elif direction == Direction.RIGHT:  # Droite
            points = [(x, y), (x - 10, y - 5), (x - 10, y + 5)]
        elif direction == Direction.DOWN:  # Bas
            points = [(x, y), (x - 5, y - 10), (x + 5, y - 10)]
        elif direction == Direction.LEFT:  # Gauche
            points = [(x, y), (x + 10, y - 5), (x + 10, y + 5)]
        
        
        pygame.draw.polygon(self.screen , (255,255,0), points)

    def render(self) -> None:
        self.screen.fill((255, 255, 255))
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                color = (0, 0, 0) if self.grid.grid[y][x] == 1 else (255, 255, 255)
                Tile(x, y, color, self.tile_size).draw(self.screen)
        Tile(self.ant.x, self.ant.y, (255, 0, 0), self.tile_size).draw(self.screen)
        Game.draw_arrow(self,self.ant.x * self.tile_size + self.tile_size // 2, self.ant.y * self.tile_size + self.tile_size // 2, self.direction)
        pygame.display.flip()
            
            
            





