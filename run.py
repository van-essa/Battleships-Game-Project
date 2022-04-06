from random import randint

# Legend
# "@" for placing ship
# " " for available space
# "X" for hit battleship
# "-" for missed shot

# creates a list of 5 spaces, 5 times
HIDDEN_BOARD = [[" "] * 5 for x in range(5)]
GUESS_BOARD = [[" "] * 5 for x in range(5)]
USER_BOARD = [[" "] * 5 for x in range(5)]

# converts letters to numbers and numbers to letters
letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}

numbers_to_letters = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F"}

# Python program to print
# The colot to text and background
# Code taken from Geeks for Geeks, see README
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))

# This Code was taken from Mavens YouTube video, provided in README
def print_board(board):
    """
    Creates a board with letters for the columns and numbers for the rows
    """
    print("  A B C D E F G H")
    print("  ---------------")
    row_number = 1
    for row in board:
      print(row_number, "|_|".join(row))
        row_number += 1