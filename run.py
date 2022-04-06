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