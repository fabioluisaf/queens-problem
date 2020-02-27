from copy import deepcopy

# creates a set of boards from the parameter that have the exact queens that the parameter has
# plus a new queen on the first empty column, if there is any space not being attacked by the others
def expand_board(board):
    new_boards = []

    # since the board is square, only counting one dimension is enough
    n = len(board)

    # looks for an empty column
    column = next((col for col in range(n) if board[col] == -1), -1)

    # if any empty column was found
    if column != -1:
        for i in range(n):
            # if the current row of that column is not being attacked, add a queen to it and put the
            # new board on the set
            if not is_being_attacked(board, column, i):
                new_board = deepcopy(board)
                new_board[column] = i
                new_boards.append(new_board)
    
    # return the set of new boards
    return new_boards

# checks if a row from a column is being attacked
def is_being_attacked(board, column, row):
    n = len(board)

    # if the row to be tested is not within the board, it's not being attacked
    if row < 0 or row >= n:
        return False
    
    # for every other column of the board
    for i in range(n):
        current_row = board[i]
        distance = abs(column - i)

        # if the i-th column has a queen and is different from the parameter column
        if current_row != -1 and i != column:
            if current_row == row:
                # if the parameter row is being attacked by other queens in the same row
                return True
            elif row == (current_row - distance) or row == (current_row + distance): 
                # if the parameter row is being attacked diagonally by other queens
                return True
    
    return False

    
# counts all the queens in the board
def queens_amt(board):
    n = len(board)
    amt = 0

    for i in range(n):
        if board[i] != -1:
            amt += 1
    
    return amt

# calculates the f-score of a certain state
def fscore(board):
    n = len(board)
    h_score = 0
    g_score = 0

    for i in range(n):
        if board[i] == -1:
            for j in range(n):
                if not is_being_attacked(board, i, j):
                    h_score += 1

        else:
            g_score += 1

    return h_score + g_score
    

    
    