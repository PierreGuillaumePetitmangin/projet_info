'''Command line arguments
The program must accept at least the following arguments on the command line:

The number of steps to run, with a default value of 10.
The path to the output file in which to write the state of the final step.
A verbose option that enable the display of log messages.
A flag option that enables GUI mode. By default the program does not open any GUI window.
If the GUI mode is enabled the following command line arguments are taken into account:
The size of a square tile, in pixels.
The color of the ant.
The display frequency (number of frames per second).'''
import argparse

class Cmd_lines :
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Ant simulation')
        self.parser.add_argument('steps', type=int, default=10, help='Number of steps to run')
        self.parser.add_argument('output', type=str, default = 'ANT/result.txt' help='Path to the output file')
        self.parser.add_argument('--verbose', action='store_true', help='Enable log messages')
        self.parser.add_argument('--gui', action='store_true', help='Enable GUI mode')
        self.parser.add_argument('--tile_size', type=int, default = help='Size of a square tile, in pixels')
        self.parser.add_argument('--ant_color', type=str, help='Color of the ant')
        self.parser.add_argument('--display_frequency', type=int, help='Number of frames per second')

    def parse_args(self):
        return self.parser.parse_args()