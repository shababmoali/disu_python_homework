from graphs.weighted_graphs import g_w_0, g_w_1, g_w_2, g_w_3


def find_set(parent, vertex):
    # print(f"find_set({parent}, {vertex})")
    if parent[vertex] != vertex:
        parent[vertex] = find_set(parent, parent[vertex])
    return parent[vertex]


def union(parent, rank, root_u, root_v):
    # print(f"Union: {root_u}, {root_v}")

    # attach the smaller rank tree under the root of the higher rank tree
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_v] < rank[root_u]:
        parent[root_v] = root_u
    else:
        # if ranks are same, make one as root and increment its rank by one
        parent[root_v] = root_u
        rank[root_u] += 1


def kruskal(graph):
    """
    MST-KRUSKAL(G, w)
        1 A = 0
        2 for each vertex v in G.V
        3     MAKE-SET(v)
        4 sort the edges of G.E into nondecreasing order by weight w
        5 for each edge (u v) in G.E, taken in nondecreasing order by weight
        6     if FIND-SET(u) != FIND-SET(v)
        7         A = A U {(u, v)}
        8         UNION(u, v)
        9 return A
    Note: courtesy of CLRS

    What is UNION-FIND data structure for?

    + Initial State: Initially, each vertex is in its own set, and thus each vertex is its own root.
        This is represented by having each vertex point to itself.

    + Union Operations: As you perform union operations to merge sets, trees grow by attaching the root of one set to another set's root.
        The root of the larger set (by rank or size) typically becomes the root of the merged set to keep the tree's height minimal.

    + Find Operation: When you perform a find operation on a vertex, you traverse up the tree (following the parent pointers) until you reach the root.
        This root is the representative of the set, indicating that any two vertices with the same root are in the same set.
    """
    # Initialize parent and rank
    parent = {vertex: vertex for vertex in graph}
    rank = {vertex: 0 for vertex in graph}

    edges = [
        (u, v, weight) for u, neighbors in graph.items() for v, weight in neighbors
    ]
    edges.sort(key=lambda e: e[2])
    print(f"edges: {edges}")

    mst = []
    for u, v, weight in edges:
        root_u = find_set(parent, u)
        root_v = find_set(parent, v)

        # print(f"parent: {parent}")
        # print(f"rank: {rank}")

        if root_u != root_v:
            mst.append(
                (u, v, weight)
            )
            union(parent, rank, root_u, root_v)

    # print(f"mst: {mst}")
    return mst


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
mst_k_0 = kruskal(g_w_0)
assert [('A', 'C', 1), ('C', 'D', 1), ('B', 'D', 2)] == mst_k_0

# Graph 1: Basic tree; slightly more complex network with five vertices
#    A --2-- B
#    |       |\
#    4       3 1
#    |       |  \
#    C --5-- D-2-E
mst_k_1 = kruskal(g_w_1)
assert [('B', 'E', 1), ('A', 'B', 2), ('D', 'E', 2), ('A', 'C', 4)] == mst_k_1

# Graph 2: six vertices, including longer paths and varying weights
#    A --1-- B --2-- C
#    |       |       |
#    4       3       2
#    |       |       |
#    F --5-- E --1-- D
mst_k_2 = kruskal(g_w_2)
assert [('A', 'B', 1), ('D', 'E', 1), ('B', 'C', 2), ('C', 'D', 2), ('A', 'F', 4)] == mst_k_2

# Graph 3: densely connected weighted graph
#    A --2-- B
#    |\     /|\
#    3 1   3 4 4
#    |  \ /  |  \
#    D-2-C-1-E-3-F
mst_k_3 = kruskal(g_w_3)
assert [('A', 'C', 1), ('C', 'E', 1), ('A', 'B', 2), ('C', 'D', 2), ('E', 'F', 3)] == mst_k_3
