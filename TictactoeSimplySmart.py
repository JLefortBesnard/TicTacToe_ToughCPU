"""
Simple tictactoe game
2019
Author:
        Jeremy Lefort-Besnard   jlefortbesnard (at) tuta (dot) io
"""

#Library we need
from sys import platform as sp
import time
import os
import subprocess
import pandas as pd
import numpy as np
from random import choice
import platform
import time
from os import system
from copy import deepcopy

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

    def write_move(self, move, symbole):
        self.board[move] = symbole

    def check_pos(self, move):
        if self.board[move] != ' ':
            print("Position already taken...")
            return 1
        if move not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Forbidden move...")
            return 1

    def check_for_victory(self):
        victory = False
        # winning combinations
        victory_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [7,5,3], [1,4,7], [2,5,8], [3,6,9]]
        for combination in victory_combinations:
            pos1, pos2, pos3 = combination[0], combination[1], combination[2]
            if self.board[pos1] == self.board[pos2] == self.board[pos3] != " ":
                # return the symbole (O or X) that won the game
                victory = self.board[pos1]
        return victory

    def keep_playing(self):
        # Return False if game is over
        # Check if winner
        victory_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [7,5,3], [1,4,7], [2,5,8], [3,6,9]]
        for combination in victory_combinations:
            pos1, pos2, pos3 = combination[0], combination[1], combination[2]
            if self.board[pos1] == self.board[pos2] == self.board[pos3] != " ":
                return False
        # Check if a move is still available
        for pos in range(1, 10):
            if self.board[pos] == ' ':
                return True
        return False

    def highlighter(self):
        position = self.board
        # winning combinations
        victory_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [7,5,3], [1,4,7], [2,5,8], [3,6,9]]
        for combination in victory_combinations:
            pos1, pos2, pos3 = combination[0], combination[1], combination[2]
            if self.board[pos1] == self.board[pos2] == self.board[pos3] != " ":
                # return the line to highlight
                symbole = self.board[pos1]
                position[pos1] = "\x1b[10;10;31m{}\x1b[0m".format(symbole)
                position[pos2] = "\x1b[10;10;31m{}\x1b[0m".format(symbole)
                position[pos3] = "\x1b[10;10;31m{}\x1b[0m".format(symbole)
        print(' ' + position[1] + ' | ' + position[2] + ' | ' + position[3])
        print('-----------')
        print(' ' + position[4] + ' | ' + position[5] + ' | ' + position[6])
        print('-----------')
        print(' ' + position[7] + ' | ' + position[8] + ' | ' + position[9])



def highlighter(current_game):
    # define where the wining line is
    victory_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [7,5,3], [1,4,7], [2,5,8], [3,6,9]]
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    for combination in victory_combinations:
        pos1, pos2, pos3 = combination[0], combination[1], combination[2]
        if board[pos1] == board[pos2] == board[pos3] == "X":
            board[pos1] = "\x1b[10;10;31mX\x1b[0m"
            board[pos2] = "\x1b[10;10;31mX\x1b[0m"
            board[pos3] = "\x1b[10;10;31mX\x1b[0m"
        elif board[pos1] == board[pos2] == board[pos3] == "O":
            board[pos1] = "\x1b[10;10;31mO\x1b[0m"
            board[pos2] = "\x1b[10;10;31mO\x1b[0m"
            board[pos3] = "\x1b[10;10;31mO\x1b[0m"




    print(" " * 10)
    print("**" * 10)
    print(" " * 10)





# Display the coordinate system of the game, make it easier for the human player to know what to play
def position():
    print(' 1 | 2 | 3 ')
    print('-----------')
    print(' 4 | 5 | 6 ')
    print('-----------')
    print(' 7 | 8 | 9 ')

# clear the screen of your terminal in Linux/Mac or Windows
def clear_screen():
    if sp == "win32":
        os.system('cls')
    else:
        os.system('clear')


def smart_CPU(current_game, brd):
    # diplay possible moves
    available_moves = np.setdiff1d(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), current_game)
    # Check if next move can be a winning move, return it if so
    best_move = 0
    for move in available_moves:
        vitual_check_win = deepcopy(brd)
        vitual_check_win.write_move(move, 'O')
        vitual_check_loose = deepcopy(brd)
        vitual_check_loose.write_move(move, 'X')
        if vitual_check_win.check_for_victory() == 'O':
            return move
        if vitual_check_loose.check_for_victory() == 'X':
            best_move = move
    if best_move != 0:
        return best_move # return the move that block the opponent
    if 5 in available_moves:
            return 5
    corners = [1, 3, 7, 9]
    for corner in corners:
        if corner in available_moves:
                return corner
    edges = [2, 4, 6, 8]
    for edge in edges:
        if edge in available_moves:
                return edge


def intro():
    # print a beautiful intro and return who plays first (cpu or human)
    clear_screen()
    print("****")
    print("Welcome to TicTacToe")
    print("****")
    print(" ")
    print("Choose a move from these positions:")
    position()
    print(" ")
    print("****")
    print("You play first or second?")
    first = input("1 or 2 >")
    print("****")
    print("Starting game...")
    print("****")
    print(" ")
    return first


def winner(game_status):
    print(" ")
    print(" **** ")
    print(" ")
    if game_status == "O":
        print("***YOU LOST***")
    elif game_status == "X":
        print("***YOU CHAMPION!***")
    else:
        print("Such a boring game...")
    print(" ")
    print(" **** ")




def play_a_game():
    first = intro()
    brd = board()
    current_game = []
    if first == "1": # human first
        while brd.keep_playing() == True:
            move = int(input("What's your move?"))
            # Forbid player to play a forbiden move or an already taken one
            while brd.check_pos(move) == 1:
                move = int(input("Sorry, what move?"))
            current_game.append(move)
            brd.write_move(move, "X")
            clear_screen()
            if brd.keep_playing() == True:
                computer_move = smart_CPU(current_game, brd)
                brd.write_move(computer_move, "O")
                current_game.append(int(computer_move))
                print("Computer played: {}".format(computer_move))
                print(" ")
                brd.print_board()
                print(" ")
    else: # computer cpu first
        while brd.keep_playing() == True:
            computer_move = smart_CPU(current_game, brd)
            brd.write_move(computer_move, "O")
            current_game.append(int(computer_move))
            print("Computer played: {}".format(computer_move))
            print(" ")
            brd.print_board()
            print(" ")
            if brd.keep_playing() == True:
                move = int(input("What's your move?"))
                # Forbid player to play a forbiden move or an already taken one
                while brd.check_pos(move) == 1:
                    move = int(input("Sorry, what move?"))
                current_game.append(int(move))
                brd.write_move(move, "X")
                clear_screen()
    clear_screen()
    game_status = brd.check_for_victory()
    brd.highlighter()
    return winner(game_status)

clear_screen()
print("Press control +  C to stop playing")
again = 1
while again == 1:
    play_a_game()
    print("Play again?")
    play_again = input("Press Enter to continue, ctrl + C to quit")
