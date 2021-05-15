import sys

file_list = ['2-FullIns_3.col', '2-FullIns_4.col', '4-FullIns_3.col', '5-FullIns_3.col', 'queen5_5.col', 'queen6_6.col', 'queen7_7.col', 'queen9_9.col', 'queen10_10.col', 'queen11_11.col']

def colToDat(file_name):
    input_filename = '../Instances/' + file_name
    output_filename =  '../Instances/' + file_name + '.dat'

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

    # Write .dat file
    with open(output_filename,'w') as output:
        output.write('data;\n')
        
        # Creates sets
        output.write(f"set V := {' '.join(map(str, range(1,vertex_count+1)))};\n")
        output.write(f"set E :=")
        for edge in edges:
            output.write(f'\n\t({edge[0]},{edge[1]})')
        output.write(';\n')

        # Creates params
        # output.write(f'param color :=')
        # for i in range(vertex_count):
        #     output.write(f'\n\t{i+1}')
        # output.write(';\n')
        output.write(f'param vertexCount := {vertex_count};\n')

        # Ends the .dat file
        output.write('end;\n')


for element in file_list:
    colToDat(element)