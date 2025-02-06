class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.grid_size = 50
        self.tile_size = self.screen_width // self.grid_size
        self.ant_color = (255, 0, 0)
        self.grid_color = (255, 255, 255)
        self.ant_speed = 1
        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.ant_position = [self.grid_size // 2, self.grid_size // 2]
        self.ant_direction = 'up'
        self.ant_turns = {'up': ['right', 'left'], 'right': ['down', 'up'], 'down': ['left', 'right'], 'left': ['up', 'down']}
        self.ant_moves = {'up': [-1, 0], 'right': [0, 1], 'down': [1, 0], 'left': [0, -1]}

    
    