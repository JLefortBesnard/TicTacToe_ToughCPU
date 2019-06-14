"""
Simple tictactoe game human vs random choice of cpu
2019
Author:
        Jeremy Lefort-Besnard   jlefortbesnard (at) tuta (dot) io
"""

#Library we need
import random
from sys import platform
import time
import os


# create the board, update it
class board:
    """
    This class create the board structure, print it, update it at each move,
    look at the position of X and O to check for game status (victory/even)
    """
    def __init__(self):
        self.board = [' '] * 10

    def print_board(self):
        position = self.board
        print(' ' + position[1] + ' | ' + position[2] + ' | ' + position[3])
        print('-----------')
        print(' ' + position[4] + ' | ' + position[5] + ' | ' + position[6])
        print('-----------')
        print(' ' + position[7] + ' | ' + position[8] + ' | ' + position[9])

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
        # winning combinations
        victory_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [7,5,3], [1,4,7], [2,5,8], [3,6,9]]
        for combination in victory_combinations:
            pos1, pos2, pos3 = combination[0], combination[1], combination[2]
            if self.board[pos1] == self.board[pos2] == self.board[pos3] != " ":
                # return the symbole (O or X) that won the game
                victory = self.board[pos1]
        return victory

# Display the coordinate system of the game, make it easier for the human player to know what to play
def position():
    print(' 1 | 2 | 3 ')
    print('-----------')
    print(' 4 | 5 | 6 ')
    print('-----------')
    print(' 7 | 8 | 9 ')

# clear the screen of your terminal in Linux/Mac or Windows
def clear_screen():
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

# Define who starts and with whaat symbole (X or O)
def define_role():
    starter = input("Who starts? cpu (c) or human (h) >> ")
    symbole = input("Symbole of the starter: X or O ? >> ")
    return starter, symbole

# the human is the first player
def human_first(symbole):
    # give symbole O to second player if starter took X, and respectively
    symbole_other = "X" if symbole == "O" else "O"
    game = board()
    nb_moves = 0
    # keep running while no victory and possible move available
    while game.victory() == False and nb_moves < 9:
        move = int(input(">> what move? >> "))
        # check that the move choice is possible
        while game.check_pos(move) == 1:
            print("move already chosen, pick an empty place (1 to 9):")
            move = int(input(">> what move? >> "))
        clear_screen()
        # Do the human move
        game.move(move, symbole)
        nb_moves += 1
        game.print_board()
        print("Turn {} ".format(nb_moves))
        time.sleep(1)
        # run if no victory and still possible move available
        if game.victory() == False and nb_moves < 9:
            # dumb cpu
            cpu_choice = random.randint(1, 9)
            # check that the move choice is possible
            while game.check_pos(cpu_choice) == 1:
                cpu_choice = random.randint(1, 9)
            # Do the cpu move
            game.move(cpu_choice, symbole_other)
            nb_moves += 1
            clear_screen()
            game.print_board()
            time.sleep(1)
    # 3 scenarios: even, win or loose
    if game.victory() == False and nb_moves == 9:
        print("...........")
        print("BORING GAME")
        print("...........")
    elif game.victory() != True:
        if game.victory() == symbole:
            print("****************")
            print("victory for human! ({})".format(game.victory()))
            print("****************")
        else:
            print("****************")
            print("victory for cpu! ({})".format(game.victory()))
            print("****************")

# the CPU is the first player
def cpu_first(symbole):
    # give symbole O to second player if starter took X, and respectively
    symbole_other = "X" if symbole == "O" else "O"
    game = board()
    nb_moves = 0
    # keep running while no victory and possible move available
    while game.victory() == False and nb_moves < 9:
        # dumb cpu
        cpu_choice = random.randint(1, 9)
        # check that the move choice is possible
        while game.check_pos(cpu_choice) == 1:
            cpu_choice = random.randint(1, 9)
        clear_screen()
        game.move(cpu_choice, symbole)
        nb_moves += 1
        game.print_board()
        print("Turn {} ".format(nb_moves))
        time.sleep(1)
        # run if no victory and still possible move available
        if game.victory() == False and nb_moves < 9:
            move = int(input(">> what move? >> "))
            # check that the move choice is possible
            while game.check_pos(move) == 1:
                print("move already chosen, pick an empty place (1 to 9):")
                move = int(input(">> what move? >> "))
            clear_screen()
            game.move(move, symbole_other)
            nb_moves += 1
            game.print_board()
            print("Turn {} ".format(nb_moves))

    # 3 scenarios: even, win or loose
    if game.victory() == False and nb_moves == 9:
        print("****************")
        print("BORING GAME")
        print("****************")
    elif game.victory() != False:
        if game.victory() == symbole:
            print("****************")
            print("victory for cpu! ({})".format(game.victory()))
            print("****************")
        else:
            print("****************")
            print("victory for human! ({})".format(game.victory()))
            print("****************")


# Processus of a complete game
def game():
    clear_screen()
    again = "y"
    while again == "y":
        print("You can choose among these positions: (remember them)")
        # display coordinate system of the game to make it easier for the player
        position()
        role = define_role()
        symbole = role[1]
        if role[0] == "h":
            # human plays first
            human_first(symbole)
        else:
            # cpu plays first
            cpu_first(symbole)
        print(" " * 10 )
        again = input("play again? (y or n) > ")
        clear_screen()

# launch the game
game()
