from agent import Agent
from game import Game
from time import sleep
import copy
class Smart_Agent(Agent):
    def __init__(self, player, depth = 6) -> None:
        self.player = player
        self.depth = depth
        self.verbose = False
    
    def evaluate(self, board: Game):
        score = 0
        for y in range(len(board.board)):
            for x in range(len(board.board[y])):
                
                ret= self.evaluate_specific(board, y, x)
                if abs(ret) == 40000000:
                    return ret
                score += ret
        return score
                

    def min_max(self, board: Game, pl, depth, alpha = -4000000000, beta = 40000000):
        if board.is_over:
            return (40000000*board.winner,0)
        if depth == self.depth:
            return (self.evaluate(board), 0)
        best_choice = 0
        best_score = -4000000000*pl
        for ch in range(7):
            i = (ch+3)%7
            new_board = board
            y_put = new_board.make_move(i, pl)
            if  y_put != -1:
                ret = self.min_max(new_board, pl*-1, depth+1, alpha, beta)[0]
                if self.verbose:
                    for _ in range(depth):
                        print(" ", end="")
                    
                    print(ret)
                if depth == 0:
                    print(ret)
                if pl == 1 and ret > best_score:
                    best_choice = i 
                    best_score = ret
                elif pl == -1 and ret < best_score:
                    best_choice = i 
                    best_score = ret
                
                if pl == 1:
                    alpha = max(alpha,ret)
                    if beta<alpha:
                        board.undo_move(y_put, i)
                        # print("PRUNE %d <=%d : ret %d"%(beta,alpha,best_score))
                        return (ret, i)
                else:
                    beta = min(beta,ret)
                    if beta < alpha:
                        board.undo_move(y_put, i)
                        return (ret,i)
                board.undo_move(y_put, i)
        if self.verbose:
            print("------------")
        return (best_score, best_choice)
        
                    




    def make_move(self, board: Game):
        inp = self.min_max(board, self.player, 0)
        # print(inp)
        # sleep(3)
        return inp[1]
    def min_eval(self, count, empties, curr):
        score = 0
        if count >= 4:
            return 40000000 * curr
        elif count == 3 and empties == 2:
            score += 333*curr
        elif count == 3 and empties == 1:
            score += 11 * curr
        elif count == 2 and empties == 2:
            score += 2 * curr
        return score
    def evaluate_specific(self, board: Game, y, x):
        score = 0
        curr =  board.board[y][x]

        if curr == 0:
            return 0
        
        count_y = 0
        i = y
        empties = 0
        while i < 6 and board.board[i][x] == curr:
            i+=1
            count_y+=1
        
        if count_y >= 4:
            
            return 40000000 * curr
        elif count_y == 3:
            score += 11 * curr
        
        empties = 0
        count_y = 0
        i = x
        while i < 7 and board.board[y][i] == curr:
            i+=1
            count_y+=1
        if i < 7 and board.board[y][i] == 0:
            empties += 1
        i = x-1
        while i >= 0 and board.board[y][i] == curr:
            i-=1
            count_y+=1
        if i >= 0 and board.board[y][i] == 0:
            empties += 1
        score += self.min_eval(count_y, empties, curr)
        
        empties = 0
        count_y = 0
        i = x
        j = y
        while i < 7 and j < 6 and board.board[j][i] == curr:
            i+=1
            j += 1
            count_y+=1
        if i < 7 and board.board[y][i] == 0:
            empties += 1
        i = x-1
        j = y - 1
        while i >= 0 and j>=0 and board.board[j][i] == curr:
            i-=1
            j-=1
            count_y+=1
        if i >= 0 and board.board[y][i] == 0:
            empties += 1
        score += self.min_eval(count_y, empties, curr)
        empties = 0
        count_y = 0
        i = x
        j = y
        while i >= 0 and j < 6 and board.board[j][i] == curr:
            i-=1
            j += 1
            count_y+=1
        if i >= 0 and board.board[y][i] == 0:
            empties += 1
        i = x+1
        j = y - 1
        while i < 7 and j>=0 and board.board[j][i] == curr:
            i+=1
            j-=1
            count_y+=1
        if i < 7 and board.board[y][i] == 0:
            empties += 1
        score += self.min_eval(count_y, empties, curr)
        if x == 3:
            score+=18*curr
        elif x == 2 or x==4:
            score+=9*curr
        
        
        return score