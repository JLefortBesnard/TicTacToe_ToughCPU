"""
Generate tictactoe game output (which will be used for creating smart cpu)
and save it as an excel document (will create a folder named "memory" and store the Excel file inside.
Mind your current directory when running the script.
Check TicTacToe.py for more in depth documentation of the code
2019
Author:
        Jeremy Lefort-Besnard   jlefortbesnard (at) tuta (dot) io
"""


import random
import os
import numpy as np
import pandas as pd



class board:
    """
    This class create the board structure, print it, update it at each move,
    look at the position of X and O to check for game status (victory/even)
    """
    def __init__(self):
        self.board = [' '] * 10

    def move(self, move, symbole):
        self.board[move] = symbole

    def check_pos(self, move):
        if self.board[move] != ' ':
            return 1
        elif move not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Forbidden move")
            return 1

    def victory(self):
        victory = False
        victory_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [7,5,3], [1,4,7], [2,5,8], [3,6,9]]
        for combination in victory_combinations:
            pos1, pos2, pos3 = combination[0], combination[1], combination[2]
            if self.board[pos1] == self.board[pos2] == self.board[pos3] != " ":
                victory = self.board[pos1]
        return victory

# The idea is to make smartcpu_choice smart afterward
def randomcpu():
    memory_moves = []
    game = board()
    nb_moves = 0
    # run until victory of no more available move
    while game.victory() == False and nb_moves < 9:
        # dumb cpu
        randcpu_choice = random.randint(1, 9)
        while game.check_pos(randcpu_choice) == 1:
            randcpu_choice = random.randint(1, 9)
        # the cpu starting the game got the symbole "O"
        game.move(randcpu_choice, 'O')
        memory_moves.append(randcpu_choice)
        nb_moves += 1

        if game.victory() == False and nb_moves < 9:
            smartcpu_choice = random.randint(1, 9)
            while game.check_pos(smartcpu_choice) == 1:
                smartcpu_choice = random.randint(1, 9)
            # the cpu playing second got the symbole "X"
            game.move(smartcpu_choice, 'X')
            memory_moves.append(smartcpu_choice)
            nb_moves += 1

    if game.victory() == False and nb_moves == 9:
        print("Even")
        # save the output as a list of [move and output game (win 1, lose -1 or even 0)]
        output = np.array([memory_moves, 0])
    elif game.victory() != False:
        if game.victory() == 'O':
            print("victory for starter")
            # save the output as a list of [move and output game (win 1, lose -1 or even 0)]
            output = np.array([memory_moves, 1])
        else:
            print("Defeat for starter")
            # save the output as a list of [move and output game (win 1, lose -1 or even 0)]
            output = np.array([memory_moves, -1])
    return output



def game():
    # simulating 50 games takes about 3 seconds
    again = int(input("how many games to simulate? > "))
    turn = 0
    path = "memory\\memory.xls"
    if not os.path.exists(path): 	
        os.mkdir("memory")
        df = pd.DataFrame(columns = ["moves", "output"])
    else:
        df = pd.read_excel(path)

    while turn < again:
        memory = randomcpu()
        # save the list output in a pandas dataframe
        row_number = len(df)
        df.loc[row_number] = memory
        turn += 1

    print("saving and quit...")
    # save the pandas dataframe output in an exel document
    # 1 when starter won, -1 when starter lost, 0 for even
    df.to_excel(path, index=False)

game()
