# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

""" 
Asking player's name 
"""
name = input("Enter your name: ")
prinnt = ("Hello, name + ! Let's play Battleships!")

"""
Creating the board/grid
"""

board = []

for x in range(0,5):
    board.append(["0"] * 5])

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

"""
Defining the rows and columns
"""

def random_row(board):
  return random.randint(0,len(board)-1)

def random_col(board):
  return random.randint(0,len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

for turn in range(4):
	guess_row = input("Guess Row:")
	guess_col = input("Guess Column:")


players_board()
computers_board()
pass

def board
pass

def ships_location
pass



