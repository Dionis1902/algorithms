def bellman_ford(graph, edges_count, source):
    if edges_count < source < 0:
        return
    dist = [float("Inf")] * edges_count
    dist[source] = 0

    for _ in range(edges_count):
        for edge, connected_edge, weight in graph:
            if dist[edge] != float("Inf") and dist[edge] + weight < dist[connected_edge]:
                dist[connected_edge] = dist[edge] + weight

    for edge, connected_edge, weight in graph:
        if dist[edge] != float("Inf") and dist[edge] + weight < dist[connected_edge]:
            print("Graph contains negative weight cycle")
            return

    return dist


if __name__ == '__main__':
    test_graph = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)]

    print(bellman_ford(test_graph, 5, 0))
