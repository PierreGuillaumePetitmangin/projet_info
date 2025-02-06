from .game import Game

class Main:
    def __init__(self) -> None:
        self.game = Game()
    
    def run(self) -> None:
        self.game.run_game()


