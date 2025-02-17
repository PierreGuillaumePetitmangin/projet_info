from .game import Game
from .settings import Settings

class Main:
    def __init__(self) -> None:
        settings = Settings()
        self.game = Game(settings)
    
    def run(self) -> None:
        self.game.run()

def ant_main() -> None:
    start = Main()
    start.run()

    


