import pygame 
from .settings import Settings

class Tile :
    def __init__(self, x, y,color) -> None:
        self._x = x
        self._y = y
        self._color = color
        self._settings = Settings()
        self._width = self._settings.grid_width
        self._height = self._settings.grid_height
        self.size = self._settings.grid_size
    @property
    def x(self) -> int:
        """The x coordinate (i.e.: column index) of the tile."""
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        """Set the x coordinate."""
        self._x = value

    @property
    def y(self) -> int:
        """The y coordinate (i.e.: line index) of the tile."""
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        """Set the y coordinate."""
        self._y = value
    @property
    def color(self) -> pygame.Color:
        """The color of the tile."""
        return self._color
    
    @color.setter
    def color(self, color: pygame.Color) -> None:
        """Change the color of the tile."""
        self._color = color

    def draw(self, screen: pygame.Surface, ) -> None:
        """Draw the tile on screen."""
        rect = pygame.Rect(self._x * self.size, self._y*self.size, self._width, self._height)
        pygame.draw.rect(screen, self.color, rect)
