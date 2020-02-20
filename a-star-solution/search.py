from copy import deepcopy

def expand_board(board):
    new_boards = []

    #since the board is square, only counting one dimension is enough
    n = len(board)

    for i in range(n):
        for j in range(n):
            #if the current position is free
            if board[i][j] == 0:
                #copy the current board and add a queen
                new_board = deepcopy(board)
                new_board[i][j] = 1
                attack(new_board, i, j)
                new_boards.append(new_board)
    
    return new_boards

#this function puts a 2 on every position that's being attacked by
#by the queen at (i,j)
def attack(board, i, j):
    n = len(board)

    #attacking the rows and columns
    for k in range(n):
        #attacking all squares in the ith row
        if board[i][k] != 1:
            board[i][k] = 2
        #attacking all squares in the jth column
        if board[k][j] != 1:
            board[k][j] = 2

    # attacking the main diagonal
    row = 0 if j >= i else i - j
    column = 0 if i >= j else j - i

    while row < n and column < n:
        if board[row][column] != 1:
            board[row][column] = 2
        
        row += 1
        column += 1

    #attacking the secondary diagonal
    row = n - 1 if j >= (n - 1 - i) else i + j
    column = 0 if (n - 1 - i) >= j else j - n + 1 + i

    while row >= 0 and column < n:
        if board[row][column] != 1:
            board[row][column] = 2
        
        row -= 1
        column += 1
    
#this functions counts all the queens in the board
def queens_amt(board):
    n = len(board)
    queens = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                queens += 1
    
    return queens

#calculates the f-score of a certain state
def fscore(board):
    score = 0
    n = len(board)

    for i in range(n):
        for j in range(n):
            if board[i][j] != 2:
                score += 1
    
    return score
    