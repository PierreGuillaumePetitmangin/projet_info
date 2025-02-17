from .direction import Direction

class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.grid_size = 100
        self.grid_width = self.screen_width // self.grid_size
        self.grid_height = self.screen_height // self.grid_size
        self.ant_color = (255, 0, 0)
        self.grid_color = (255, 255, 255)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.ant_speed = 1
        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.ant_position = [self.grid_size // 2, self.grid_size // 2]
    

    
    