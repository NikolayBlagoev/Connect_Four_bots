from game import Game
class Agent(object):
    def __init__(self, player) -> None:
        self.player = player
        
    def make_move(self, board: Game):
        return 3