from .direction import Direction
class Ant :
    def __init__(self, grid):
        self.grid = grid
        self.x = self.grid.cols // 2
        self.y = self.grid.rows // 2
        self.direction = 0

    def move(self):
        if self.grid.grid[self.y][self.x] == 0:
            self.direction = (self.direction + 1) % 4
            self.grid.grid[self.y][self.x] = 1
        else:
            self.direction = (self.direction - 1) % 4
            self.grid.grid[self.y][self.x] = 0

        if self.direction == Direction.UP:
            self.y -= 1
        elif self.direction == Direction.DOWN:
            self.y += 1
        elif self.direction == Direction.LEFT:
            self.x -= 1
        elif self.direction == Direction.RIGHT:
            self.x += 1
        