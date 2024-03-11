from graphs.directed_weighted_graphs import g_dw_0, g_dw_3

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
                return vertex_distance_map, vertex_predecessor_map, True  # negative cycle detected

    return vertex_predecessor_map, vertex_distance_map, False  # no negative cycle detected


# Graph 0:
#    A --3--> B
#    | \      |
#    1  4     2
#    |    \   |
#    V      V V
#    C <--1-- D
bm_sp_0a_path_map, bm_sp_0a_distances_map, has_neg_weight_cycle_a  = bellman_ford(g_dw_0, 'A')
assert 'A' == bm_sp_0a_path_map['D']
assert 4 == bm_sp_0a_distances_map['D']

bm_sp_0b_path_map, bm_sp_0b_distances_map, has_neg_weight_cycle_b  = bellman_ford(g_dw_0, 'B')
print(bm_sp_0b_path_map, bm_sp_0b_distances_map)
assert float('inf') == bm_sp_0b_distances_map['A']
assert None == bm_sp_0b_path_map['A']
assert 'D' == bm_sp_0b_path_map['C']
