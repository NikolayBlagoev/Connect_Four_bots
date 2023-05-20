import os
import copy
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
colorama_init()
class Game(object):
    def __init__(self) -> None:
        self.is_over = False
        self.turn = 0
        self.winner = 0
        self.board = [[0 for i in range(7)] for x in range(6)]
    def print_board(self):
        os.system("cls")
        for row in self.board:
            print("|",end="")
            for col in row:

                if col == 0:
                    print(f"{Fore.WHITE}█{Style.RESET_ALL}|",end="")
                elif col == 1:
                    print(f"{Fore.RED}█{Style.RESET_ALL}|",end="")
                elif col == -1:
                    print(f"{Fore.YELLOW}█{Style.RESET_ALL}|",end="")
            print()     
        print(" 1 2 3 4 5 6 7")
    def is_won(self, y, x):
        curr =  self.board[y][x]
        count_y = 0
        i = y
        while i < 6 and self.board[i][x] == curr:
            i+=1
            count_y+=1
        if count_y >= 4:
            self.winner = curr
            self.is_over = True
            return True

        count_y = 0
        i = x
        while i < 7 and self.board[y][i] == curr:
            i+=1
            count_y+=1
        i = x-1
        while i >= 0 and self.board[y][i] == curr:
            i-=1
            count_y+=1

        if count_y >= 4:
            self.winner = curr
            self.is_over = True
            return True
        count_y = 0
        i = x
        j = y
        while i < 7 and j < 6 and self.board[j][i] == curr:
            i+=1
            j += 1
            count_y+=1
        i = x-1
        j = y - 1
        while i >= 0 and j>=0 and self.board[j][i] == curr:
            i-=1
            j-=1
            count_y+=1

        if count_y >= 4:
            self.winner = curr
            self.is_over = True
            return True
        count_y = 0
        i = x
        j = y
        while i >= 0 and j < 6 and self.board[j][i] == curr:
            i-=1
            j += 1
            count_y+=1
        i = x+1
        j = y - 1
        while i < 7 and j>=0 and self.board[j][i] == curr:
            i+=1
            j-=1
            count_y+=1

        if count_y >= 4:
            self.winner = curr
            self.is_over = True
            return True
        return False
        
    def make_move(self, inp, player):
        if inp < 0 or inp > 6:
            return -1
        if self.board[0][inp] != 0:
            return -1
        i = 0
        while i < 6 and self.board[i][inp] == 0:
            i+=1
        i-=1
        self.turn += 1
        self.board[i][inp] = player
        self.is_won(i, inp)
