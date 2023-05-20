from agent import Agent
from game import Game
class Human_Agent(Agent):
    def make_move(self, board: Game):
        board.print_board()
        print("where do you play? (1-7): ")
        
        inp = int(input())
        inp-=1
           
            
            
        
        return inp