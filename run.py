from random import randint

# Legend
# "@" for placing ship
# " " for available space
# "X" for hit battleship
# "-" for missed shot

# creates a list of 8 spaces, 8 times
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
GUESS_BOARD = [[" "] * 8 for x in range(8)]
USER_BOARD = [[" "] * 8 for x in range(8)]

# converts letters to numbers and numbers to letters
letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                      "F": 5, "G": 6, "H": 7}

numbers_to_letters = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E",
                      5: "F", 6: "G", 7: "H"}

user_score = 0
computer_score = 0

continue_playing_options = ["y", "yes", "n", "no"]


# Python program to print
# The colot to text and background
# Code taken from Geeks for Geeks, see README
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
 
 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
 
 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
 
 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))

# This Code was taken from Mavens YouTube video, provided in README
"""
Creates a board with letters for the columns and numbers for the rows
"""
def print_board(board):
    print("  A B C D E F G H")
    print("  ---------------")
    row_number = 1
    for row in board:
        print(row_number, "|".join(row))
        row_number += 1

# This Code was taken from Mavens YouTube video, provided in README
"""
A random integer between 0 and 4 for ship_row and ship_column is created.
It checks if "@" is already on the board, if so runs randomint until.
there is an available space. When there is an available space update with "@".
"""
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "@":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "@"

"""
A random integer between 0 and 4 for computer_row and computer_column
is created. It checks if "-" or "X" is already on the board. If so, it
runs randomint until there is an available space. If computer_row and
computer_column is "@", it prints a message to the user to say their
ship has been hit and updates board with "X". Else the computer_row
and computer_column finds a blank space, and prints a message to the
user to say the computer has missed and updates the board with "-"
"""
def computer_guess(board):
    global computer_score
    computer_row, computer_column = randint(0, 7), randint(0, 7)
    if (USER_BOARD[computer_row][computer_column] == "-" or
            USER_BOARD[computer_row][computer_column] == "X"):
        computer_row = randint(0, 7)
        computer_column = randint(0, 7)
    elif USER_BOARD[computer_row][computer_column] == "@":
        prRed(f"Oh no, {username}, your battleship has been hit!")
        prGreen(
            f"The computer guessed row {computer_row +1}"
            f" and column {numbers_to_letters[computer_column]}")
        USER_BOARD[computer_row][computer_column] = "X"
        computer_score += 1
    else:
        prGreen(f"Yeyy {username}, the computer missed!")
        prGreen(
            f"The computer guessed row {computer_row +1}"
            f" and column {numbers_to_letters[computer_column]}")
        USER_BOARD[computer_row][computer_column] = "-"

# This Code was taken from Mavens YouTube video, provided in README
"""
It asks the user to input the guesses for ship row and ship column locations
and checks the input data for row is in range "12345" and for column is in range
"ABCDE". Then, returns int for row - 1 to match index number, converts letters
to numbers for column index number.
"""
def get_ship_location():
    row = input("Please enter a ship row 1-8\n")
    while row not in "12345678" or len(row) > 1 or row == "":
        validate_row(row)
        print("Please enter a valid row")
        row = input("Please enter a ship row 1-8\n")
    column = input("Please enter a ship column A-H\n").upper()
    while column not in "ABCDEFGH" or len(column) > 1 or column == "":
        validate_column(column)
        print("Please enter a valid column")
        column = input("Please enter a ship column A-H\n").upper()
    return int(row) - 1, letters_to_numbers[column]

"""
If values entered not an interger between 1-5, an error message will be printed.
"""
def validate_row(values):
    try:
        [int(value) for value in values]
        if int(values) < 1 or int(values) > 8:
            print(
                f"Number between 1-8 required, you provided '{values}'."
            )
    except:
        print(f"Sorry number between 1-8 required, please try again.\n")
        return False

    return True

"""
If values entered not in letters_to_numbers, an error message will be printed.
"""
def validate_column(values):
    try:
        if values not in letters_to_numbers:
            print(
                f"Letter between A-H required, you provided '{values}'."
                )
    except:
        print(f"Sorry letter between A-H required, please try again.\n")
        return False

    return True

# This Code was taken from Mavens YouTube video, provided in README
"""
Counts how many ships on the board have been hit "X"
"""
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

# print hidden board for testing, needs removing before submission
# print("Hidden Board")
# print_board(HIDDEN_BOARD)
"""
Run all start up functions
"""
def main():
    create_ships(HIDDEN_BOARD)
    create_ships(USER_BOARD)
    print("------------------------------------------------")
    print("Welcome to Ultinamte Battleships!")
    print("Board Size: 8. Number of ships: 5")
    print("You have 10 turns to find all of the battleships.")
    print("------------------------------------------------")
    global username
    username = input("Please enter your name:\n")
    while username == "" or username == " ":
        print("Sorry, please can you enter a name.")
        username = input("Please enter your name:\n")

"""
If the values entered are not in continue_playing_options, an error
message will be printed.
"""
def validate_continue_playing(values):
    try:
        if values not in continue_playing_options:
            print(
                f"Please enter y/n, you provided '{values}'."
                )
    except:
        print(f"Sorry y/n required, please try again.\n")
        return False

    return True

# This Code was taken from Mavens YouTube video, provided in README
# Additional statements added such us the if the computer wind and
# continue playing options
"""
Runs the game with 10 turns
When turns = 0 game is over
"""
def run_game():
    turns = 10
    global user_score

    while turns > 0:
        prYellow(f"{username}'s Board")
        print_board(USER_BOARD)
        prGreen("Computer's Board")
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-" or GUESS_BOARD[row][column] == "X":
            prRed("You have already guessed that")
        elif HIDDEN_BOARD[row][column] == "@":
            prYellow(f"Congratulations {username}, you hit a  battleship!")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
            computer_guess(USER_BOARD)
            user_score += 1
        else:
            prRed(f"Oh, no {username}, you missed!")
            GUESS_BOARD[row][column] = "-"
            turns -= 1
            computer_guess(USER_BOARD)
        if count_hit_ships(GUESS_BOARD) == 5:
            prYellow(
                f"Congratulations {username}, "
                "you have sunk all of the battleships!")
            print("The game is now over.")
            break
        prLightPurple("You have " + str(turns) + " turns remaining.")
        prYellow(f"{username}'s Score: {user_score}"
                 f" Computer's Score: {computer_score}")
        if turns == 0:
            prRed(
                f"You ran out of turns {username}, the game is over.")
            break
        if count_hit_ships(USER_BOARD) == 5:
            prRed(
                f"Oh, no {username}, the computer"
                " has sunk all of your battleships!")
            break
        if count_hit_ships(GUESS_BOARD) < 5:
            continue_playing = input(
                    "Do you want to continue playing? y/n\n").lower()
            while continue_playing not in continue_playing_options:
                validate_continue_playing(continue_playing)
                continue_playing = input(
                    "Do you want to continue playing? y/n\n").lower()
            if continue_playing == "y" or continue_playing == "yes":
                print(
                    "You have decided to continue playing the game.")
                continue
            elif continue_playing == "n" or continue_playing == "no":
                print(
                    "You have decided to finish the game, the game is now over.")
                break
            else:
                print("Sorry, please enter y/n")
                continue_playing = input(
                    "Do you want to continue playing? y/n \n")


main()
run_game()