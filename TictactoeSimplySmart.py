"""
Tictactoe game 
human vs hand-crafted AI (no training involved) 
2019
Author:
        Jeremy Lefort-Besnard   jlefortbesnard (at) tuta (dot) io
"""

#Library we need
from sys import platform as sp
import numpy as np
from os import system
from copy import deepcopy

class board:
    """
    This class create the board structure, print it, update it,
    check for winning position, highlight winning position, check if board full or still move available
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
        # Write move on board
        self.board[move] = symbole

    def check_pos(self, move):
         # Check that move is alowed or at least not already taken
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
        victory_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [7,5,3], [1,4,7], [2,5,8], [3,6,9]]
        # Check if winner
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
        # Highlight winning line
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

# AI
def smart_CPU(current_game, brd):
    # diplay possible moves
    available_moves = np.setdiff1d(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), current_game)
    best_move = 0
    for move in available_moves:
        vitual_check_win = deepcopy(brd)
        vitual_check_win.write_move(move, 'O')
        vitual_check_loose = deepcopy(brd)
        vitual_check_loose.write_move(move, 'X')
        # Check if a move can be a winning move, return it if so
        if vitual_check_win.check_for_victory() == 'O':
            return move
        # Check if a move from the opponent can make the AI loose, return it if so, to block the opponent
        if vitual_check_loose.check_for_victory() == 'X':
            # Not a return because winning is a priority over blocking (if no winning move, then block)
            best_move = move
    if best_move != 0:
        return best_move # return the move that block the opponent only if no winning move

    if 5 in available_moves:
            return 5 # best move to play if no winning or blocking move
    corners = [1, 3, 7, 9]
    for corner in corners:
        if corner in available_moves:
                return corner # best move to play if 5 not available and no winning or blocking move
    edges = [2, 4, 6, 8]
    for edge in edges:
        if edge in available_moves:
                return edge # best move to play if 5 not available and no winning or blocking move and no more empty corner


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
    # Return the output of the game, win, lost or even
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
    first = intro() # print beautiful intro
    brd = board() # initialize a board
    current_game = [] # needed for the AI to find the best next move
    if first == "1": # human first
        while brd.keep_playing() == True: # No winner and still available move
            # HUMAN TURN
            move = int(input("What's your move?"))
            # Forbid human player to play a forbiden move or an already taken one
            while brd.check_pos(move) == 1:
                move = int(input("Sorry, what move?"))
            current_game.append(move)
            brd.write_move(move, "X")
            clear_screen()
            if brd.keep_playing() == True: # No winner and still available move
                # AI TURN
                computer_move = smart_CPU(current_game, brd)
                brd.write_move(computer_move, "O")
                current_game.append(int(computer_move))
                print("Computer played: {}".format(computer_move))
                print(" ")
                brd.print_board()
                print(" ")
    else: # computer cpu first
        while brd.keep_playing() == True: # No winner and still available move
            # AI TURN
            computer_move = smart_CPU(current_game, brd)
            brd.write_move(computer_move, "O")
            current_game.append(int(computer_move))
            print("Computer played: {}".format(computer_move))
            print(" ")
            brd.print_board()
            print(" ")
            if brd.keep_playing() == True: # No winner and still available move
                # HUMAN TURN
                move = int(input("What's your move?"))
                # Forbid human player to play a forbiden move or an already taken one
                while brd.check_pos(move) == 1:
                    move = int(input("Sorry, what move?"))
                current_game.append(int(move))
                brd.write_move(move, "X")
                clear_screen()
    clear_screen()
    game_status = brd.check_for_victory() 
    brd.highlighter() # display the game (if winner, highlight the winning line)
    return winner(game_status) # display output of the game

clear_screen()
print("Press control +  C to stop playing")
again = 1
while again == 1: # infinite loop until ctrl + c
    play_a_game()
    print("Play again?")
    play_again = input("Press Enter to continue, ctrl + C to quit")
