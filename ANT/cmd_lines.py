import argparse

class Cmd_lines :
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description='Ant')
        self.parser.add_argument('steps', type=int, default=10, help='Number of steps to run')
        self.parser.add_argument('output', type=str, default = 'ANT/result.txt', help='Path to the output file')
        self.parser.add_argument('--verbose', action='store_true', help='Enable log messages')
        self.parser.add_argument('--gui', action='store_true', help='Enable GUI mode')
        self.parser.add_argument('--tile_size', type=int, default = 50,help='Size of a square tile, in pixels')
        self.parser.add_argument('--ant_color', type=tuple, default = (255,0,0),help='Color of the ant')
        self.parser.add_argument('--display_frequency', type=int, default = 10, help='Number of frames per second')
        self.parser.add_argument('--grid_size', type=int, default = 50, help='Size of the grid')
    def parse_args(self) -> argparse.Namespace:
        return self.parser.parse_args()
    