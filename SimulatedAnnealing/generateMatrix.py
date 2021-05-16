import numpy as np


def colToMatrix(file_name):
  input_filename = '../Instances/' + file_name

  # Reads file
  with open(input_filename,'r') as data:

    # Skips useless lines
    for _ in range(10):
      current_line = data.readline()
      if 'p edge' in current_line:
        break

    # Reads number of vertex
    current_line = current_line.split(' ')
    vertex_count = int(current_line[2])

    # Saves all edges
    edges = []
    for _,line in enumerate(data.readlines()):
      _,first_vertex,second_vertex = line.rstrip().split(' ')
      edges.append((first_vertex, second_vertex))
      edges.append((second_vertex, first_vertex))

    edges = list(set([i for i in edges]))

  # Initiates empty matrix
  matrix = np.zeros((vertex_count, vertex_count))

  # Fills the matrix
  for e in edges:
    i = int(e[0]) - 1
    j = int(e[1]) - 1
    matrix[i][j] = 1
    matrix[j][i] = 1

  return matrix, vertex_count