import heapq
import queue

# weighted graph ie vertex: [edge(vertex, weight)]
#        (0)
#       /   \
#      2     3
#     /       \
#    (1)--4---(2)
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


def prim_lazy(graph):
    """
    "Lazy implementation of Prim’s algorithm" --
    Prim(graph G)
        PQ = empty priority queue of edges
        color all vertices grey
        Visit(0)
        while(|A| < n - 1)
            (u,v) = PQ.DeleteMin()
            if u or v is grey
                A = A u (u, v)
            if u is grey
                Visit(u)
            else // v is grey
                Visit(v)
    Visit(vertex u)
        color u black
        for all edges (u,v)
            if v is grey
                PQ.insert((u,v))
    """
    n = len(graph)
    A = []  # minimum spanning tree (list of edges)
    pq_edges = queue.PriorityQueue()  # priority queue of edges
    colors = ['grey'] * n

    def visit(u):
        colors[u] = 'black'
        for v, weight in graph[u]:
            if colors[v] == 'grey':
                pq_edges.put((u, v, weight))

    visit(0)

    while len(A) < n - 1:
        u, v, weight = pq_edges.get()
        if colors[u] == 'grey' or colors[v] == 'grey':
            A.append((u, v, weight))
        if colors[u] == 'grey':
            visit(u)
        else:
            visit(v)

    return A


# Graph 0: Basic weighted graph; four vertices and weighted edges
#    A --3-- B
#    | \     |
#    1  4    2
#    |     \ |
#    C --1-- D
#
# g_w_0 = {
#     'A': [('B', 3), ('C', 1), ('D', 4)],
#     'B': [('A', 3), ('D', 2)],
#     'C': [('A', 1), ('D', 1)],
#     'D': [('B', 2), ('C', 1), ('A', 4)]
# }
mst_p_lazy = prim_lazy(graph)
print(mst_p_lazy)


def prim(graph, start_v):
    """
    MST-PRIM(G, w)
        1 for each u in G.V
        2     u.key = inf
        3     u.parent = NIL
        4 r.key = 0
        5 Q = G.V
        6 while Q != 0  // not empty
        7     u = EXTRACT-MIN(Q)
        8     for each v in G.Adj[u]
        9         if v in Q and w(u, v) < v.key
        10            v.parent = u
        11            v.key = w(u, v)
        Note: From CLRS
    """
    pass
    # ill come back to playing w/ MSTs and this implementation, if i have time


# Graph 1: Basic tree; slightly more complex network with five vertices
#    A --2-- B
#    |       |\
#    4       3 1
#    |       |  \
#    C --5-- D-2-E


# Graph 2: six vertices, including longer paths and varying weights
#    A --1-- B --2-- C
#    |       |       |
#    4       3       2
#    |       |       |
#    F --5-- E --1-- D


# Graph 3: densely connected weighted graph
#    A --2-- B
#    |\     /|\
#    3 1   3 4 4
#    |  \ /  |  \
#    D-2-C-1-E-3-F

