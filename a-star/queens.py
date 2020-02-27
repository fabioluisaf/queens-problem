from search import expand_board, queens_amt, fscore
from ui import print_stats

#each board is nxn
n = 10
boards_tested = 0

# -1 at column i symbolizes that there is no queen at column i
# j at column i symbolizes that there is a queen at row j in column i

#creating an empty board to start everything
empty_board = [-1 for i in range(n)]

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

print("\n")
