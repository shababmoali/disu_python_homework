# Graph 0: Basic weighted graph; four vertices and weighted edges
#    A --3-- B
#    | \     |
#    1  4    2
#    |     \ |
#    C --1-- D
#
g_w_0 = {
    'A': [('B', 3), ('C', 1), ('D', 4)],
    'B': [('A', 3), ('D', 2)],
    'C': [('A', 1), ('D', 1)],
    'D': [('B', 2), ('C', 1), ('A', 4)]
}

# Graph 1: Basic tree; slightly more complex network with five vertices
#    A --2-- B
#    |       |\
#    4       3 1
#    |       |  \
#    C --5-- D-2-E
g_w_1 = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 3), ('E', 1)],
    'C': [('A', 4), ('D', 5)],
    'D': [('B', 3), ('C', 5), ('E', 2)],
    'E': [('B', 1), ('D', 2)]
}

# Graph 2: six vertices, including longer paths and varying weights
#    A --1-- B --2-- C
#    |       |       |
#    4       3       2
#    |       |       |
#    F --5-- E --1-- D
g_w_2 = {
    'A': [('B', 1), ('F', 4)],
    'B': [('A', 1), ('C', 2), ('E', 3)],
    'C': [('B', 2), ('D', 2)],
    'D': [('C', 2), ('E', 1)],
    'E': [('B', 3), ('D', 1), ('F', 5)],
    'F': [('A', 4), ('E', 5)]
}

# Graph 3: densely connected weighted graph
#    A --2-- B
#    |\     /|\
#    3 1   3 4 4
#    |  \ /  |  \
#    D-2-C-1-E-3-F
g_w_3 = {
    'A': [('B', 2), ('C', 1), ('D', 3)],
    'B': [('A', 2), ('C', 3), ('E', 4), ('F', 4)],
    'C': [('A', 1), ('B', 3), ('D', 2), ('E', 2)],
    'D': [('A', 3), ('C', 2)],
    'E': [('B', 4), ('C', 2), ('F', 1)],
    'F': [('E', 3)]
}
