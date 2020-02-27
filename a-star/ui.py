import sys

def print_amt_tested(n):
  print("Boards tested: {}".format(n), end="\n")

def print_board(board):
  n = len(board)

  #build the string representation of the best board found
  string = "["

  for i in range(n):
    string= "{} {}".format(string, board[i])

  spaces = " " * n
  string = "{}]{}".format(string, spaces)

  print(string)

def print_stats(board, amt_tested):
  print_amt_tested(amt_tested)
  print_board(board)
  
  sys.stdout.write("\033[F" * 2)

