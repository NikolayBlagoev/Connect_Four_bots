


from human_agent import Human_Agent
from smart_agent import Smart_Agent
from game import Game
import copy
from deep_learning_agent import Deep_Learning_Agent
from time import sleep




new_Game = Game()
players = [Smart_Agent(1), Deep_Learning_Agent(-1)]
turn = 0
while not new_Game.is_over:
    print(new_Game.turn)
    new_Game.print_board()
    
    inp = players[turn].make_move(copy.deepcopy(new_Game))
    ret = new_Game.make_move(inp, players[turn].player)
    if ret == -1:
        continue
    turn = (turn+1)%2
    sleep(2)
new_Game.print_board()
print("OUTCOME:",new_Game.winner)