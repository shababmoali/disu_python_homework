from graphs.directed_weighted_graphs import g_dw_0, g_dw_3, g_dw_5_with_negative_cycle


def bellman_ford(graph, start):
    """
    BELLMAN-FORD(G, w, s)
        1 INITIALIZE-SINGLE-SOURCE(G, s)
        2 for i = 1 to |G.V| - 1
        3     for each edge (u, v) in G.E
        4         RELAX(u, v, w)
        5 for each edge (u, v) in G.E
        6     if v.d > u.d + w(u, v)
        7         return FALSE
        8 return TRUE
    """
    vertex_distance_map = {v: float('infinity') for v in graph}
    vertex_predecessor_map = {v: None for v in graph}  # map to reconstruct the single shortest path

    vertex_distance_map[start] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                # relax
                ssp_cost = vertex_distance_map[vertex] + weight
                if ssp_cost < vertex_distance_map[neighbor]:
                    vertex_distance_map[neighbor] = ssp_cost
                    vertex_predecessor_map[neighbor] = vertex

    # check for negative weight cycles
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if vertex_distance_map[vertex] + weight < vertex_distance_map[neighbor]:
                return vertex_predecessor_map, vertex_distance_map, False  # negative cycle detected

    return vertex_predecessor_map, vertex_distance_map, True  # no negative cycle detected


# Graph 0:
#    A --3--> B
#    | \      |
#    1  4     2
#    |    \   |
#    V      V V
#    C <--1-- D
bm_sp_0a_path_map, bm_sp_0a_distances_map, no_neg_weight_cycle_0a = bellman_ford(g_dw_0, 'A')
assert 'A' == bm_sp_0a_path_map['D']
assert 4 == bm_sp_0a_distances_map['D']
assert no_neg_weight_cycle_0a is True

bm_sp_0b_path_map, bm_sp_0b_distances_map, no_neg_weight_cycle_0b = bellman_ford(g_dw_0, 'B')
assert float('inf') == bm_sp_0b_distances_map['A']
assert bm_sp_0b_path_map['A'] is None
assert 'D' == bm_sp_0b_path_map['C']
assert no_neg_weight_cycle_0b is True


# Graph 3:
#    A --2--> B
#    |\      / \
#    3 1    3   4
#    |  \  /     \
#    V    V       V
#    D<-2-C--2---> E---3--> F
bm_sp_3a_path_map, bm_sp_3a_distances_map, no_neg_weight_cycle_3a = bellman_ford(g_dw_3, 'A')
assert 'A' == bm_sp_3a_path_map['C']
assert 'A' == bm_sp_3a_path_map['D']

assert 3 == bm_sp_3a_distances_map['D']
assert 3 == bm_sp_3a_distances_map['E']


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
bm_sp_5a_path_map, bm_sp_5a_distances_map, no_neg_weight_cycle_5a = bellman_ford(g_dw_5_with_negative_cycle, 'A')
assert 'B' == bm_sp_5a_path_map['C']
assert 'C' == bm_sp_5a_path_map['D']

assert no_neg_weight_cycle_5a is False
