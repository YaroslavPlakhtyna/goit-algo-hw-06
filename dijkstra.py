from network import G


def print_table(distances, node):
    print(f"Closest relation to each different person for '{node}':")
    print("-" * 20)
    print("{:<10} {:<10}".format("Node", "Distance"))
    print("-" * 20)
    for vertex in distances:
        distance = distances[vertex]
        if distance != 0:
            if distance == float("infinity"):
                distance = "∞"
            else:
                distance = str(distance)
            print("{:<10} {:<10}".format(vertex, distance))
    print()


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes)
    visited = []
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float("infinity"):
            break
        for neighbor, props in graph[current_vertex].items():
            distance = distances[current_vertex] + props["weight"]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        visited.append(current_vertex)
        unvisited.remove(current_vertex)
    print_table(distances, node)


if __name__ == "__main__":
    for node in G.nodes:
        dijkstra(G, node)
