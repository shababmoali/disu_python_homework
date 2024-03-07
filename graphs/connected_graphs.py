from typing import Any

# Graph 0: Basic tree
#    A -- B
#    |    |
#    C    D -- E


# Adjacency List:
g_al_0: dict[Any, list[Any]] = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B', 'E'],
    'E': []
}

# Adjacency Matrix:
g_am: list[list[Any]] = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

# Graph 1: Slightly more complicated tree, + 1 lead node
#    A -- B
#    |    |
#    C    D -- E
#         |
#         F


# Adjacency List:
g_al_1: dict[Any, list[Any]] = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B', 'E', 'F'],
    'E': [],
    'F':[]
}

# Graph 2: simple cycle
#    A -- B
#    |    |
#    C -- D


# Adjacency List:
g_al_2: dict[Any, list[Any]] = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}


# Graph 3: graph with multiple cycles, and paths
#    A -- B-----
#    |    |    |
#    C    D -- E
#    |         |
#    |---------F


g_al_3: dict[Any, list[Any]] = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

