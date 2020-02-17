import sys

def print_amt_tested(n):
    print("Boards tested: {}".format(n))

def print_board(board):
    n = len(board)

    #build the string representation of the best board found
    string = ""

    for i in range(n):
        string= "{}[ ".format(string)

        for j in range(n):
            string = "{}{} ".format(string, board[i][j])

        string = "{}]\n".format(string)

    print(string)

def print_stats(board, amt_tested):
    print_amt_tested(amt_tested)
    print_board(board)
    
    sys.stdout.write("\033[F" * (len(board) + 2))

