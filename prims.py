# Graph:
#    A -- B
#    |    |
#    C    D -- E

# Adjacency List:
g_al = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B', 'E'],
    'E': []
}

# Adjacency Matrix:
g_am = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

# "Lazy implementation of Prim’s algorithm"
# Prim(graph G)
#     PQ = empty priority queue of edges
#     color all vertices grey
#     Visit(0)
#     while(|A| < n - 1)
#         (u,v) = PQ.DeleteMin()
#         if u or v is grey
#             A = A u (u, v)
#         if u is grey
#             Visit(u)
#         else // v is grey
#             Visit(v)
# Visit(vertex u)
#     color u black
#     for all edges (u,v)
#         if v is grey
#             PQ.insert((u,v))

import queue

# directed asymmetric graph ie vertex: [edge(vertex, weight)]
graph = {
    0: [(1, 2), (2, 3)],
    1: [(0, 2), (2, 4)],
    2: [(0, 3), (1, 4)]
}

# Interesting Point:
# https://www.geeksforgeeks.org/why-prims-and-kruskals-mst-algorithm-fails-for-directed-graph/
# Why Prim’s Algorithm Fails for Directed Graph ?
# Prim’s algorithm assumes that all vertices are connected.
# But in a directed graph, every node is not reachable from every other node.
# So, Prim’s algorithm fails due to this reason.
# graph = {
#     0: [(1, 2), (2, 3), (3, 4)],
#     1: [(0, 2), (2, 4)],
#     2: [(0, 3), (1, 4), (4, 5)],
#     3: [(0, 4), (2, 5)],
#     4: [(1, 4), (2, 5)],
#     5: [(2, 5), (3, 5)]
# }


def prim(graph):
    n = len(graph)
    A = []  # minimum spanning tree (list of edges)
    pq_edges = queue.PriorityQueue()  # priority queue of edges
    colors = ['grey'] * n

    def visit(u):
        colors[u] = 'black'
        for v, weight in graph[u]:
            if colors[v] == 'grey':
                pq_edges.put((weight, u, v))

    visit(0)

    while len(A) < n - 1:
        weight, u, v = pq_edges.get()
        if colors[u] == 'grey' or colors[v] == 'grey':
            A.append((u, v))
        if colors[u] == 'grey':
            visit(u)
        else:
            visit(v)

    return A

minimum_spanning_tree = prim(graph)
print(minimum_spanning_tree)

