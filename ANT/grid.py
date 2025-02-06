import pygame
class Grid :
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.tile_width = self.settings.screen_width // self.settings.grid_width
        self.tile_height = self.settings.screen_height // self.settings.grid_height
        self.grid = [[0 for _ in range(self.settings.grid_width)] for _ in range(self.settings.grid_height)]

    def draw_grid(self) -> None:
        for i in range(self.settings.grid_height):
            for j in range(self.settings.grid_width):
                if self.grid[i][j] == 0:
                    color = self.settings.white
                else:
                    color = self.settings.black
                pygame.draw.rect(self.screen, color, (j * self.tile_width, i * self.tile_height, self.tile_width, self.tile_height))
                pygame.draw.rect(self.screen, self.settings.grid_color, (j * self.tile_width, i * self.tile_height, self.tile_width, self.tile_height), 1)