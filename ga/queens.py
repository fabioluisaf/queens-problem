from ga import next_generation, generate_population, fitness
from ui import print_stats

# the board size is nxn
n = 25
# since the process is random, it is possible to go on forever
# this number limits the amount of generations
max_generations = 100000
# the size of the population
amt_boards = 100

# creating the starting population
population = generate_population(amt_boards, n)
# counting the amount of generations
amt_generations = 1

# sorting the first population
population.sort(key=fitness)

# looping while no individual has reached the perfect score, or until the max number
# of generations has been exceeded
while fitness(population[0]) > 0 and amt_generations <= max_generations:
  amt_generations += 1
  # get the next generation
  population = next_generation(population)

  # print the stats of the current generation
  print_stats(population[0], amt_generations)


print("\n")
