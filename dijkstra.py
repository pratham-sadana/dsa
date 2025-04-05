def djik(graph, start):
    d = {node: float('inf') for node in graph}
    d[start] = 0
    visited = set()

    while len(visited) < len(graph):
        min_node = None
        for node in graph:
            if node not in visited and (min_node is None or d[node] < d[min_node]):
                min_node = node

        if d[min_node] == float('inf'):
            break

        visited.add(min_node)

        for neighbour, weight in graph[min_node].items():
            new_d = d[min_node] + weight
            if new_d < d[neighbour]:
                d[neighbour] = new_d

    return d

# Example graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start = 'A'
sp = djik(graph, start)
print(sp)
