from collections import deque
from network import G


def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=" ")
    for neighbor in graph[vertex].keys():
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def bfs(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex].keys()) - visited)
    bfs(graph, queue, visited)


if __name__ == "__main__":
    dfs(G, "Alice")
    print()
    bfs(G, deque(["Alice"]))
