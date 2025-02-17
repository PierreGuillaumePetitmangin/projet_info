from .direction import Direction
from .cmd_lines import Cmd_lines
class Settings:
    def __init__(self):
        cmd = Cmd_lines()
        self.args = cmd.parse_args()
        self.steps = self.args.steps
        self.grid_size = self.args.grid_size
        self.gui = self.args.gui
        self.tile_size = 10
        self.screen_size = self.grid_size * self.tile_size
    

    
    