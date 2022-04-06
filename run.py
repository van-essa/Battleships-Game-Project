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

# This Code was taken from Mavens YouTube video, provided in README
def get_ship_location():
    """
    It asks the user to input the guesses for ship row and ship column locations
    and checks the input data for row is in range "12345" and for column is in range 
    "ABCDE". Then, returns int for row - 1 to match index number, converts letters 
    to numbers for column index number.
    """
    row = input("Please enter a ship row 1-5\n")
    while row not in "12345" or len(row) > 1 or row == "":
        validate_row(row)
        print("Please enter a valid row number")
        row = input("Please enter a ship row 1-5\n")
    column = input("Please enter a ship column A-E\n").upper()
    while column not in "ABCDE" or len(column) > 1 or column == "":
        validate_column(column)
        print("Please enter a valid column")
        column = input("Please enter a ship column A-E\n").upper()
    return int(row) - 1, letters_to_numbers[column]

def validate_row(values):
    """
    If values entered not an interger between 1-5, an error message will be printed.
    """
    try:
        [int(value) for value in values]
        if int(values) < 1 or int(values) > 5:
            print(
                f"Number between 1-5 required, you provided '{values}'."
            )
    except:
        print(f"Sorry number between 1-5 required, please try again.\n")
        return False

    return True


def validate_column(values):
    """
    If values entered not in letters_to_numbers, an error message will be printed.
    """
    try:
        if values not in letters_to_numbers:
            print(
                f"Letter between A-E required, you provided '{values}'."
                )
    except:
        print(f"Sorry letter between A-E required, please try again.\n")
        return False

    return True