import sys
import numpy as np
import time
from random import random, randint, choice
from generateMatrix import colToMatrix

ALPHA = 0.9
MIN_TEMPERATURE = 0.001
INITIAL_TEMPERATURE = 10.0
MAX_ITERATIONS = 10000

matrixData = colToMatrix('2-FullIns_3.col')

# MAIN PROGRAM


def color_graph(vertices, matrix):
    cost = 0
    # Best results found
    bestSolution = []
    # Count time used to process
    start = time.time()
    # While the algorithm can reach a cost of zero
    # decreases the number of colors
    while(cost == 0):
        solution, cost = simulated_annealing(vertices, matrix)
    elapsed = (time.time() - start)
    print("FINAL-> " + "Solution: " + str(solution) + " / " + " Cost: " +
          str(cost) + " / " + " Time Elapsed: " + str(elapsed) + "seconds")


# ANNEALING ALGORITHM
def simulated_annealing(vertices_number, matrix):
    # matrix, vertices_number = readFile(file)
    matrix = matrix
    vertices_number = vertices_number
    colors_number = vertices_number - 1
    temperature = INITIAL_TEMPERATURE
    solution = generate_first_solution(vertices_number, colors_number, matrix)
    cost = get_cost(solution, vertices_number)
    vertice = get_next_vertice(vertices_number)
    while temperature > MIN_TEMPERATURE and cost != 0:
        i = 0
        while i <= MAX_ITERATIONS:
            new_solution = generate_new_solution(
                solution, colors_number, vertice, vertices_number, matrix)
            new_cost = get_cost(new_solution, vertices_number)
            vertice = get_next_vertice(vertices_number)
            accept = acceptance(cost, new_cost, temperature)
            if accept > random():
                solution = new_solution.copy()
                cost = new_cost
                colors_number = cost + 1
            i += 1
            print("Solution: " + str(solution) + " / " + " Temp: " +
                  str(temperature) + " / " + " Cost: " + str(cost))
        temperature = temperature * ALPHA
    return solution, cost

# Generate Acceptance Probability based on the function:
#  Acceptance = e*(-(new_cost - old_cost) / Temperature)


def acceptance(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return 1
    else:
        accept = np.exp(- (new_cost - old_cost) / temperature)
        return accept

# Calculates cost of the the solution based on the number of collisions
# and which collision to processs


def get_next_vertice(vertices_number):
    return randint(0, vertices_number - 1)


def get_cost(solution, vertices_number):
    cost = 0
    different_colors = []
    for i in range(0, vertices_number):
        if solution[i] not in different_colors:
            different_colors.append(solution[i])

    return len(different_colors)


def generate_first_solution(vertices_number, colors_number, matrix):
    solution = np.arange(vertices_number)
    for i in range(0, vertices_number):
        solution[i] = randint(0, colors_number)
        while(not is_valid_color(solution, i, vertices_number, matrix)):
            solution[i] = randint(0, colors_number)
    return solution


def is_valid_color(solution, vertice, vertices_number, matrix):
    for i in range(0, vertices_number):
        if((i != vertice) and (matrix[i][vertice] == 1) and (solution[i] == solution[vertice])):
            return False
    return True


def generate_new_solution(solution, colors_number, vertice, vertices_number, matrix):
    new_solution = solution.copy()
    old_color = new_solution[vertice]
    new_solution[vertice] = randint(0, colors_number)
    i = 0
    while(not is_valid_color(new_solution, vertice, vertices_number, matrix) and (i < colors_number)):
        new_solution[vertice] = randint(0, colors_number)
        i = i + 1

    if (i == colors_number):
        new_solution[vertice] = old_color
    return new_solution


# Execute Program
if __name__ == "__main__":
    matrix = matrixData[0]
    vertices = matrixData[1]
    color_graph(vertices, matrix)
