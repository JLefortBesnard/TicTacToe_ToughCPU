"""
Once you generated games and saved them in "memory\\memory.xls".
Run this script to display the generated games on your terminal
Display the winning line in red, and only the games won by the computer that started
2019
Author:
        Jeremy Lefort-Besnard   jlefortbesnard (at) tuta (dot) io
"""

import pandas as pd

def game_reader():
    print("read the winning moves computed one by one, ctrl + c to stop the process")
    path = "memory\\memory.xls"
    df = pd.read_excel(path)
    winning_moves = df["moves"][df["output"] == 1]
    game_nb = 1
    for string_of_moves in winning_moves:
        # convert the df output into readable numbers
        moves = []
        for stuff in string_of_moves:
            try:
                digit = int(float(stuff))
                moves.append(digit)
            except ValueError:
                continue
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        for nb, position in enumerate(moves):
            if nb % 2 == 0:
                #even number (first player)
                board[position] = "O"
            else:
                #odd number (second player)
                board[position] = "X"        
        # define where the wining line is
        victory_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [7,5,3], [1,4,7], [2,5,8], [3,6,9]]
        for combination in victory_combinations:
            pos1, pos2, pos3 = combination[0], combination[1], combination[2]
            # paint the winning line in red
            if board[pos1] == board[pos2] == board[pos3] == "O":
                board[pos1] = "\x1b[10;10;31mO\x1b[0m"
                board[pos2] = "\x1b[10;10;31mO\x1b[0m"
                board[pos3] = "\x1b[10;10;31mO\x1b[0m"
        print(" " * 10)
        print("game number {}".format(game_nb))
        print(" " * 10)
        
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('-----------')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('-----------')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print(" " * 10)
        print("**" * 10)
        print(" " * 10)
        game_nb += 1
        
game_reader()
