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

# This Code was taken from Mavens YouTube video, provided in README
def create_ships(board):
    """
    A random integer between 0 and 4 for ship_row and ship_column is created.
    It checks if "@" is already on the board, if so runs randomint until.
    there is an available space. When there is an available space update with "@".
    """
    for ship in range(3):
        ship_row, ship_column = randint(0, 4), randint(0, 4)
        while board[ship_row][ship_column] == "@":
            ship_row, ship_column = randint(0, 4), randint(0, 4)
        board[ship_row][ship_column] = "@"

def computer_guess(board):
    """
    A random integer between 0 and 4 for computer_row and computer_column
    is created. It checks if "-" or "X" is already on the board. If so, it 
    runs randomint until there is an available space. If computer_row and 
    computer_column is "@", it prints a message to the user to say their 
    ship has been hit and updates board with "X". Else the computer_row 
    and computer_column finds a blank space, and prints a message to the 
    user to say the computer has missed and updates the board with "-"
    """
    global computer_score
    computer_row, computer_column = randint(0, 4), randint(0, 4)
    if (USER_BOARD[computer_row][computer_column] == "-" or
            USER_BOARD[computer_row][computer_column] == "X"):
        computer_row = randint(0, 4)
        computer_column = randint(0, 4)
    elif USER_BOARD[computer_row][computer_column] == "@":
        prYellow(f"{username}, your battleship has been hit!")
        prYellow(
            f"The computer guessed row {computer_row +1}"
            f" and column {numbers_to_letters[computer_column]}")
        USER_BOARD[computer_row][computer_column] = "X"
        computer_score += 1
    else:
        prYellow(f"Phew {username}, the computer missed!")
        prYellow(
            f"The computer guessed row {computer_row +1}"
            f" and column {numbers_to_letters[computer_column]}")
        USER_BOARD[computer_row][computer_column] = "-"