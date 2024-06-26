# Graph 0:
#    A --3--> B
#    | \      |
#    1  4     2
#    |    \   |
#    V      V V
#    C <--1-- D

g_dw_0 = {
    'A': [('B', 3), ('C', 1), ('D', 4)],
    'B': [('D', 2)],
    'C': [],
    'D': [('C', 1)]
}

# Graph 1:
#    A --2--> B
#    |       / \
#    4      3   1
#    |     /     \
#    V    V       V
#    C    D <-2-> E
g_dw_1 = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 1)],
    'C': [],
    'D': [('E', 2)],
    'E': [('D', 2)]
}

# Graph 2:
#    A --1--> B --2--> C
#    |        |        |
#    4        3        2
#    |        |        |
#    V        V        V
#    F<---5-- E<--1--- D
g_dw_2 = {
    'A': [('B', 1), ('F', 4)],
    'B': [('C', 2), ('E', 3)],
    'C': [('D', 2)],
    'D': [('E', 1)],
    'E': [('F', 5)],
    'F': []
}

# Graph 3:
#    A --2--> B
#    |\      / \
#    3 1    3   4
#    |  \  /     \
#    V    V       V
#    D<-2-C--2---> E---3--> F
g_dw_3 = {
    'A': [('B', 2), ('C', 1), ('D', 3)],
    'B': [('C', 3), ('E', 4)],
    'C': [('D', 2), ('E', 2)],
    'D': [],
    'E': [('F', 3)],
    'F': []
}


# Graph 4:
#    A --1--> B --1--> C
#             ^       /
#             |      /
#             4    -6
#             |   /
#             D<--
g_dw_4_with_negative_cycle = {
    'A': [('B', 1)],
    'B': [('C', 1)],
    'C': [('D', -6)],
    'D': [('B', 4)]
}

# Graph 3:
#    A --4--> B <---------
#     \      / \          |
#      3    -2  2         |
#       \  /     \        |
#         V       V       |
#         C--1---> D      3
#         |               |
#        -5               |
#         |               |
#         V               |
#         E---------------
g_dw_5_with_negative_cycle = {
    'A': [('B', 4), ('C', 3)],
    'B': [('C', -2), ('D', 2)],
    'C': [('D', 1), ('E', -5)],
    'D': [],
    'E': [('B', 3)]  # This edge creates a negative weight cycle B -> C -> E -> B
}
