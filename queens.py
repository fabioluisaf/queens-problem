from search import expand_board, queens_amt, fscore
from ui import print_stats

# 0 = has nothing on it
# 1 = has a queen on it
# 2 = is being atacked by at least one queen

#each board is nxn
n = 9
boards_tested = 0

#creating an empty board to start everything
empty_board = [[0 for j in range(n)] for i in range(n)]

#stores the open set of boards, those that will be evaluated
open_set = [empty_board]

#stores the board with highest amount of queens
highest = (empty_board, queens_amt(empty_board))

#performs a bfs/a* to find the best board
while len(open_set) > 0 and highest[1] < n:
    #if you want to perform the bfs instead of the a*, delete the next line
    open_set.sort(key=fscore)

    #pick the next on the queue and count how many queens it has
    board = open_set.pop(0) 
    n_queens = queens_amt(board)

    #check if it is the highest
    if(n_queens > highest[1]):
        highest = board, n_queens

    #create all possible boards by adding one queen to the current board
    children = expand_board(board) 

    #add all those possible boards to the open_set
    open_set = open_set + children

    #print the current stats
    boards_tested += 1
    print_stats(highest[0], boards_tested)

#the 'print_stats' function will always move the cursor up, so
#this print compenstates that by replacing the cursor after
#the text
print("\n" * (n + 1))
