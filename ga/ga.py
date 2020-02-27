from random import randint, random
from copy import deepcopy

# counts the number of queens to the left of the current are attacking it
def number_attackers(board, column, row):
    n = len(board)
    attackers = 0

    # if the row is not within the board, there are no attackers
    if row < 0 or row >= n:
        return attackers
    
    # from 0 to column
    for i in range(column):
        # get the row in which the queen is on the i-th column
        current_row = board[i]
        # calculate the distance between the i-th column and column
        distance = abs(column - i)

        if current_row == row: # counting any attackers on the same row
            attackers += 1
        elif row == (current_row - distance) or row == (current_row + distance): # counting any attackers on the diagonals
            attackers += 1
    
    return attackers

# creates a random board
def generate_board(size):
    return [randint(0, size-1) for _ in range(size)]

# generate a population with amt_boards random individuals, each one of size board_size
def generate_population(amt_boards, board_size):
    population = []

    for _ in range(amt_boards):
        new_board = generate_board(board_size)
        population.append(new_board)

    return population

# calculates the fitness of a board
def fitness(board):
    n = len(board)
    fitness = 0

    # sum the amount of attackers of each queen
    for i in range(n):
        fitness += number_attackers(board, i, board[i])

    return fitness

# intelligently mutates the board
def mutate(board):
    n = len(board)
    new_board = []

    # making sure that no queens are in the same row
    for i in board:
        if i not in new_board:
            new_board.append(i)
    
    for i in range(n):
        if i not in new_board:
            new_board.append(i)
    
    # swapping a left queen and a right queen with each other
    left_index = randint(0, n//2 - 1)
    right_index = randint(n//2, n - 1)

    new_board[left_index], new_board[right_index] = new_board[right_index], new_board[left_index]

    return new_board

# given 2 parents, generates 2 children by mixing their boards
def reproduce(board1, board2):
    # ignore if the boards do not have the same size
    if(len(board1) != len(board2)):
        return []

    n = len(board1)

    # generating the children boards
    child1 = board1[0:n//2] + board2[n//2:n]
    child2 = board2[0:n//2] + board1[n//2:n]

    return [child1, child2]

# creates a new generation based on a population, and returns the best
# elements of both generations
def next_generation(population):
    new_generation = []
    n = len(population)

    # reproduce every board with it's neighbors
    for i in range(n-1):
        children = reproduce(population[i], population[i+1])

        children[0] = mutate(children[0])
        children[1] = mutate(children[1])

        new_generation = new_generation + children

    # mixing and sorting both generations
    new_generation = new_generation + population
    new_generation.sort(key=fitness)

    # killing the weakest
    return new_generation[0:len(population)]