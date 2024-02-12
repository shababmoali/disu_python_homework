from collections import deque
from typing import Optional, Deque, Any

from graphs import g_al_2, g_al_3

# Graph 2:
#    A -- B
#    |    |
#    C -- D

# Graph 3:
#    A -- B-----
#    |    |    |
#    C    D -- E
#    |         |
#    |---------F


def depth_first_search(
        graph: dict[Any, list[Any]], vertex: Any,
        visited: Optional[set[Any]] = None,
        traversal: Optional[list[Any]] = None
) -> Optional[list[Any]]:
    """
    Depth First Search:
        DFS(G, u)
        u.visited = true
        for each v ∈ G.Adj[u]
        if v.visited == false
            DFS(G, v)

        init() {
            For each u ∈ G
                u.visited = false
            For each u ∈ G
                DFS(G, u)
        }
    Recursion to handle adjacency list (python built-in types)...
    """

    if visited is None:
        visited = set()

    if traversal is None:
        traversal = []

    if vertex in visited:
        return None

    traversal.append(vertex)

    visited.add(vertex)
    for neighbor in graph[vertex]:
        depth_first_search(graph, neighbor, visited, traversal)

    return traversal


assert ['A', 'B', 'D', 'C'] == depth_first_search(g_al_2, 'A')

dfs_a = depth_first_search(g_al_3, 'A')
assert ['A', 'B', 'D', 'E', 'F', 'C'] == dfs_a

dfs_b = depth_first_search(g_al_3, 'B')
assert ['B', 'A', 'C', 'F', 'E', 'D'] == dfs_b


def breadth_first_search(
        graph: dict[Any, list[Any]], vertex: Any,
        visited: Optional[set[Any]] = None,
        traversal: Optional[list[Any]] = None
) -> Optional[list[Any]]:
    """
    Breadth First Search:
        create a queue Q
        mark vertex u as visited and put u into Q
        while Q is non-empty
            remove the head u of Q
            mark and enqueue all (unvisited) neighbours vertices v of u
    """

    if visited is None:
        visited = set()

    if traversal is None:
        traversal = []

    queue: Deque = deque()
    visited.add(vertex)
    queue.append(vertex)

    while queue:

        vertex = queue.popleft()
        traversal.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal


assert ['A', 'B', 'C', 'D'] == breadth_first_search(g_al_2, 'A')

bfs_a = breadth_first_search(g_al_3, 'A')
assert ['A', 'B', 'C', 'D', 'E', 'F'] == bfs_a

bfs_b = breadth_first_search(g_al_3, 'B')
assert ['B', 'A', 'D', 'E', 'C', 'F'] == bfs_b
