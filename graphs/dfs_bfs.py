from collections import deque
from typing import Optional, Deque, Any

from connected_graphs import g_al_2, g_al_3


def depth_first_search_recur(
        graph: dict[Any, list[Any]], vertex: Any,
        visited: Optional[set[Any]] = None,
        traversal: Optional[list[Any]] = None
) -> list[Any]:
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
    
    In DFS, the time complexity is determined by |V| the number of vertices, and |E| edges in the graph.
    For each vertex (v), DFS visits all its adjacent vertices recursively.
    In the worst case, DFS may visit all vertices and edges in the graph.
    Therefore, the time complexity of DFS is O(V + E), 
    where V represents the number of vertices and E represents the number of edges in the graph.
    """

    if visited is None: visited = set()
    if traversal is None: traversal = []

    traversal.append(vertex)
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            depth_first_search_recur(graph, neighbor, visited, traversal)

    return traversal


def depth_first_search(graph: dict[Any, list[Any]], vertex: Any) -> None:

    visited = set()
    traversal  = []

    stack = [vertex]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)

            for neighbor in reversed(graph[vertex]):  # reverse to maintain vertex order, lifo popped off stack
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal


def breadth_first_search(graph: dict[Any, list[Any]], vertex: Any) -> list[Any]:
    """
    Breadth First Search:
        create a queue Q
        mark vertex u as visited and put u into Q
        while Q is non-empty
            remove the head u of Q
            mark and enqueue all (unvisited) neighbours vertices v of u
            
    In BFS, time complexity is determined by |V| the number of vertices and |E| edges in the graph.
    BFS visits all the vertices at each level of the graph before moving to the next level.
    In the worst case (as we always talk about upper bound in Big O notation), 
    BFS may visit all vertices and edges in the graph.
    Therefore, the time complexity of BFS is O(V + E), 
    where V represents the number of vertices and E represents the number of edges in the graph.
    """

    traversal = list()

    visited: set = set()
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

assert ['A', 'B', 'D', 'C'] == depth_first_search_recur(g_al_2, 'A')

dfs_a = depth_first_search_recur(g_al_3, 'A')
assert ['A', 'B', 'D', 'E', 'F', 'C'] == dfs_a

dfs_b = depth_first_search_recur(g_al_3, 'B')
assert ['B', 'A', 'C', 'F', 'E', 'D'] == dfs_b

dfs_a = depth_first_search(g_al_3, 'A')
assert ['A', 'B', 'D', 'E', 'F', 'C'] == dfs_a

dfs_b = depth_first_search(g_al_3, 'B')
assert ['B', 'A', 'C', 'F', 'E', 'D'] == dfs_b

assert ['A', 'B', 'C', 'D'] == breadth_first_search(g_al_2, 'A')

bfs_a = breadth_first_search(g_al_3, 'A')
assert ['A', 'B', 'C', 'D', 'E', 'F'] == bfs_a

bfs_b = breadth_first_search(g_al_3, 'B')
assert ['B', 'A', 'D', 'E', 'C', 'F'] == bfs_b
