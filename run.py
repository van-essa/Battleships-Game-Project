# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

#Asking player's name 

name = input("Enter your name: ")
print("\n")
print("Hello", name + "!")

#Create a 5x5 2 dimensional list
board = []

for x in range(5):
    board.append(["[_]"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))
print("Let's play Battleship!")
print("Take a guess between 0 and 4 for row & column.\n")
print(" Battleship Field")
print("===================")

print_board(board)


#Defining the rows and columns

def random_row(board):
  return random.randint(0,len(board)-1)
def random_col(board):
  return random.randint(0,len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

for turn in range(4):
	guess_row = input("Guess Row:")
	guess_col = input("Guess Column:")





