import pygame
from .settings import Settings
import numpy as np
from .tile import Tile


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
    
    def change(self, x, y):
        self.grid[y][x] = 1 - self.grid[y][x]
    
    def print_grid(self, step, x, y, direction):
        print(f"Step {step}: X={x}, Y={y}, Direction={direction}")
        for row in self.grid:
            print(" ".join(['#' if cell else '.' for cell in row]))
   

    
    
    




    