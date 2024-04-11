import heapq

from graphs.directed_weighted_graphs import g_dw_0, g_dw_3, g_dw_5_with_negative_cycle


def _relax(delta_v, delta_u, weight_u_v):
    """
    Relax is a key feature used in single shortest path algorithms:
    It updates the shortest distance (delta) estimate of vertices.

    For each edge, (u,v) with weight w,
        if the distance (delta) to v can be shortened by taking u to v,
            then the distance (delta) to v is updated to the shorter distance (delta).

    Pseudocode:
    RELAX(u, v)
    if d[u] + w(u, v) < d[v]
    then, d[v] = d[u] + w(u, v)

    + relax is O(1)
    """
    if delta_u + weight_u_v < delta_v:
        delta_v = delta_u + weight_u_v


def dijkstra(graph, start):
    """
    Dijkstra(V, E, s):
    S {s}
    d[s] 0
    While S V
    For all v S such that there is an edge (u, v) for some u S:
        cost c[v] min{(u, v): u in S} d[u] + w(u, v)

        Of these vertices, let v be one for which c[v] is minimum
        Add v to S
        d[v] c[v]
    """
    vertex_distance_map = {v: float('inf') for v in graph}
    vertex_predecessor_map = {v: None for v in graph}  # map to reconstruct the single shortest path

    vertex_distance_map[start] = 0
    pq = [(start, vertex_distance_map[start])]

    while pq:
        vertex, distance = heapq.heappop(pq)

        for neighbor, weight in graph[vertex]:
            # relax
            ssp_cost = vertex_distance_map[vertex] + weight
            if ssp_cost < vertex_distance_map[neighbor]:
                vertex_distance_map[neighbor] = ssp_cost
                vertex_predecessor_map[neighbor] = vertex

                heapq.heappush(pq, (neighbor, ssp_cost))  # insert next to pq

    return vertex_predecessor_map, vertex_distance_map


# Graph 0:
#    A --3--> B
#    | \      |
#    1  4     2
#    |    \   |
#    V      V V
#    C <--1-- D
dijk_sp_0a_path_map, dijk_sp_0a_distances_map = dijkstra(g_dw_0, 'A')
assert 'A' == dijk_sp_0a_path_map['D']
assert 4 == dijk_sp_0a_distances_map['D']

dijk_sp_0b_path_map, dijk_sp_0b_distances_map = dijkstra(g_dw_0, 'B')
assert float('inf') == dijk_sp_0b_distances_map['A']
assert dijk_sp_0b_path_map['A'] is None
assert 'D' == dijk_sp_0b_path_map['C']


# Graph 3:
#    A --2--> B
#    |\      / \
#    3 1    3   4
#    |  \  /     \
#    V    V       V
#    D<-2-C--2---> E---3--> F
dijk_sp_3a_path_map, dijk_sp_3a_distances_map = dijkstra(g_dw_3, 'A')
assert 'A' == dijk_sp_3a_path_map['C']
assert 'A' == dijk_sp_3a_path_map['D']

assert 3 == dijk_sp_3a_distances_map['D']
assert 3 == dijk_sp_3a_distances_map['E']


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
#
# Dijkstra's is a greedy algorithm, where relaxing on the neighbour will push neighbour (v) to the priority queue (PQ)
# If a negative edge weight cycle is reachable from the source, the shortest path distances in the negative weight cycle
# are ever reducing leading to an infinite loop
# dijk_sp_0a_path_map, dijk_sp_0a_distances_map = dijkstra(g_dw_5_with_negative_cycle, 'A')
