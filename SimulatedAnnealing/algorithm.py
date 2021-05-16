import sys
import numpy as np
import time
from random import random, randint, choice
import random
from generateMatrix import colToMatrix

ALPHA = 0.9
MIN_TEMPERATURE = 0.001
INITIAL_TEMPERATURE = 10.0
MAX_ITERATIONS = 500
FILE_NAME = '2-FullIns_3'
SEED = 3


def color_graph(vertices, matrix):
    cost = 0
    start = time.time()
    while(cost == 0):
        solution, cost = simulated_annealing(vertices, matrix)
    end = (time.time() - start)
    return "Solution: " + str(solution) + " \nCost: " + str(cost) + "\nTime: " + str(end) + " seconds"


def simulated_annealing(vertices_number, matrix):
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
            if accept > random.random():
                solution = new_solution.copy()
                cost = new_cost
                colors_number = cost + 1
            i += 1
        temperature = temperature * ALPHA
    return solution, cost


def acceptance(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return 1
    else:
        accept = np.exp(- (new_cost - old_cost) / temperature)
        return accept


def get_next_vertice(vertices_number):
    return random.randint(0, vertices_number - 1)


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
        solution[i] = random.randint(0, colors_number)
        while(not is_valid_color(solution, i, vertices_number, matrix)):
            solution[i] = random.randint(0, colors_number)
    return solution


def is_valid_color(solution, vertice, vertices_number, matrix):
    for i in range(0, vertices_number):
        if((i != vertice) and (matrix[i][vertice] == 1) and (solution[i] == solution[vertice])):
            return False
    return True


def generate_new_solution(solution, colors_number, vertice, vertices_number, matrix):
    new_solution = solution.copy()
    old_color = new_solution[vertice]
    new_solution[vertice] = random.randint(0, colors_number)
    i = 0
    while(not is_valid_color(new_solution, vertice, vertices_number, matrix) and (i < colors_number)):
        new_solution[vertice] = random.randint(0, colors_number)
        i = i + 1

    if (i == colors_number):
        new_solution[vertice] = old_color
    return new_solution


if __name__ == "__main__":
    FILE_NAME = sys.argv[1]
    INITIAL_TEMPERATURE = float(sys.argv[2])
    ALPHA = float(sys.argv[3])
    MAX_ITERATIONS = int(sys.argv[4])
    MIN_TEMPERATURE = float(sys.argv[5])
    SEED = int(sys.argv[6])

    random.seed(SEED)

    matrix, vertices = colToMatrix(FILE_NAME + '.col')
    print(color_graph(vertices, matrix))
