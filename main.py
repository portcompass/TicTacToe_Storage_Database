# This is not really a "program", but instead of a set of functions 
# that you might want to copy into your TicTacToe program.

# This doesn't do any drawing; it is NOT a Turtle graphics program.
# RATHER:
# This provides what you might want to call a "database" specifically
# for representing a 3-by-3 "grid" of cells.

# Each cell is either EMPTY or contains a letter like "X" or "O".

# One function "initializes" the grid of storage cells, 
# setting each of the 9 cells to be EMPTY.

# Another function is used to ask what is stored inside one of the cells.
# The last function places a value inside one of the storage cells.

# To refer to one of the cells in the grid, 
# you must specify which ROW and which COLUMN.
# The top row is row 0, bottom row is row 2.
# The left column is numbered 0, right column is numbered 2.

# TO COPY THIS CODE INTO YOUR OWN PROGRAM, JUST BRING OVER LINES 24 THROUGH 47
######################################################################################
TICTACTOE_STORAGE_GRID = None

def initialize_storage_grid():
  global TICTACTOE_STORAGE_GRID
  TICTACTOE_STORAGE_GRID = []
  for row in [0,1,2]:
    TICTACTOE_STORAGE_GRID.append(["EMPTY", "EMPTY", "EMPTY"])

def fetch_value_from_storage_grid(row_number, column_number):
  global TICTACTOE_STORAGE_GRID
  return TICTACTOE_STORAGE_GRID[row_number][column_number]
  
def store_value_in_storage_grid(row_number, column_number, value):
  global TICTACTOE_STORAGE_GRID
  TICTACTOE_STORAGE_GRID[row_number][column_number] = value

import sys
def print_out_storage_grid():
  global TICTACTOE_STORAGE_GRID
  for current_row in (0,1,2):
    for current_col in (0,1,2):
      sys.stdout.write('{:^10}'.format
         (TICTACTOE_STORAGE_GRID[current_row][current_col]))
    print('')
######################################################################################


# Below is David's code for testing the above functions.  
# You don't need to bring the below code into your own program.
# But, remember: your program must launch the initialization function before 
# it starts using the fetch/store functions.

# This is the initialization function:
initialize_storage_grid()

# Let's print out the initial empty game board just to do a "sanity check"
print("Now I am going to print out the INITIAL (empty) status of the game board:")
print_out_storage_grid()

# Now, I'm putting two "markers" on the game board
print("Let me put down two markers on the game board...")
store_value_in_storage_grid(0,2, 'X')
store_value_in_storage_grid(1,1, 'O')

print("Now I am going to print out the current status of the game board:")
print_out_storage_grid()

print("Now I am going to 'fetch' the value stored at row 0, column 2:")
print(fetch_value_from_storage_grid(0,2))  # This will print "X"

print("Now I am going to 'fetch' the value stored at row 0, column 0:")
print(fetch_value_from_storage_grid(0,0))  # This will print "EMPTY"

print("Now I am going to 'fetch' the value stored at row 1, column 1:")
print(fetch_value_from_storage_grid(1,1))  # This will print "O"

