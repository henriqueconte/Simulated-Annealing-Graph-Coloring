import numpy as np
import time
from random import random, randint, choice

ALPHA = 0.9
MIN_TEMPERATURE = 0.001
INITIAL_TEMPERATURE = 10.0
MAX_ITERATIONS = 100

matrixEx = [
    [0, 1, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0]
]


# MAIN PROGRAM


def color_graph(vertices, matrix):
    colors_number = vertices
    cost = 0
    # Best results found
    bestSolution = []
    # Count time used to process
    start = time.time()
    # While the algorithm can reach a cost of zero
    # decreases the number of colors
    while(cost == 0):
        solution, cost = simulated_annealing(
            "file", colors_number, matrix)
        if(cost == 0):
            colors_number -= 1
            bestSolution = solution
    elapsed = (time.time() - start)
    print("FINAL-> " + "Solution: " + str(bestSolution) + " / " + " Colors: " +
          str(colors_number) + " / " + " Time Elapsed: " + str(elapsed) + "seconds")


# ANNEALING ALGORITHM
def simulated_annealing(file, colors_number, matrix):
    # matrix, vertices_number = readFile(file)
    matrix = matrix
    vertices_number = 6
    colors_number = colors_number
    colors_number -= 1
    temperature = INITIAL_TEMPERATURE
    solution = generate_first_solution(vertices_number, colors_number)
    cost, neighbour = checkCost(vertices_number, matrix, solution)
    while temperature > MIN_TEMPERATURE and cost != 0:
        i = 0
        while i <= MAX_ITERATIONS:
            new_solution = generate_new_solution(
                solution, colors_number, neighbour)
            new_cost, neighbour = checkCost(
                vertices_number, matrix, solution)
            accept = acceptance(cost, new_cost, temperature)
            if accept > random():
                solution = new_solution
                cost = new_cost
            i += 1
            print("Solution: " + str(solution) + " / " + " Colors: "
                  + str(colors_number + 1) + " / " + " Temp: " + str(temperature) + " / " + " Cost: " + str(cost))
        temperature = temperature * ALPHA
    colors_number += 1
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
# and which collision to process


def checkCost(vertices_number, matrix, solution):
    cost = 0
    collision_list = []
    neighbour_index = -1
    for i in range(vertices_number):
        for j in range(vertices_number):
            if((i != j) and (matrix[i][j] == 1) and (solution[i] == solution[j])):
                cost += 1
                collision_list.append(i)
    if(neighbour_index == -1):
        prob = randint(1, 2)
        # Chooses a random collision to treat with 50% of chance
        if(prob % 2 == 0 and len(collision_list) != 0):
            neighbour_index = choice(collision_list)
        elif(1 < i < (len(matrix) - 1)):
            ap = randint(1, 3)
            # Or chooses a random neighbour to a collision to treat
            if(ap % 3 == 0):
                neighbour_index = choice(collision_list)
                neighbour_index = neighbour_index + prob
            elif(ap % 3 == 2):
                neighbour_index = choice(collision_list)
                neighbour_index = neighbour_index - prob
            else:
                neighbour_index = choice(len(solution))
    return cost, neighbour_index

# Fill the solution array with random colors


def generate_first_solution(vertices_number, colors_number):
    solution = np.arange(vertices_number)
    for i in range(vertices_number):
        solution[i] = randint(0, colors_number)
    return solution

# Generate a new neighbour solution


def generate_new_solution(solution, colors_number, neighbour):
    oldColor = solution[neighbour]
    newColor = randint(0, colors_number)
    while (oldColor == newColor):
        newColor = randint(0, colors_number)
    solution[neighbour] = newColor
    return solution


# Execute Program
if __name__ == "__main__":
    vertices = 6
    matrix = matrixEx
    color_graph(vertices, matrix)
