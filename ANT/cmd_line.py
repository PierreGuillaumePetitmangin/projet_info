'''The program must accept at least the following arguments on the command line:

The number of steps to run, with a default value of 10.
The path to the output file in which to write the state of the final step.
A verbose option that enable the display of log messages.
A flag option that enables GUI mode. By default the program does not open any GUI window.
If the GUI mode is enabled the following command line arguments are taken into account:
The size of a square tile, in pixels.
The color of the ant.
The display frequency (number of frames per second).'''
from exceptions import Exceptions
class Command_line :
    def __init__(self) -> None:
        self.steps = 10
        self.output_file = None
        self.verbose = False
        self.gui = False
        self.tile_size = 10
        self.ant_color = (255, 0, 0)
        self.display_frequency = 1

    def parse_command_line(self, args) -> tuple:
        '''Parse the command line arguments and return the values of the options,
          testing the validity of the arguments'''
        i = 1
        while i < len(args):
            if args[i] == '-steps':
                self.steps = int(args[i + 1])
                i += 2
            elif args[i] == '-output_file':
                self.output_file = args[i + 1]
                i += 2
            elif args[i] == '-verbose':
                self.verbose = True
                i += 1
            elif args[i] == '-gui':
                self.gui = True
                i += 1
            elif args[i] == '-tile_size':
                self.tile_size = int(args[i + 1])
                i += 2
            elif args[i] == '-ant_color':
                self.ant_color = tuple(map(int, args[i + 1].split(',')))
                i += 2
            elif args[i] == '-display_frequency':
                self.display_frequency = int(args[i + 1])
                i += 2
            else:
                raise Exceptions.ValueError('Unknown option: ' + args[i])
        return (self.steps, self.output_file, self.verbose, self.gui, self.tile_size, self.ant_color, self.display_frequency)


