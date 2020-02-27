import sys

def print_amt_generations(n):
  print("Generations: {}".format(n), end="\n")

def print_stats(board, amt_generations):
  print_amt_generations(amt_generations)
  print(board)
  
  sys.stdout.write("\033[F" * 2)

