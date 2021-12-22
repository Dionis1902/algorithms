def dijkstra(graph, edges_count, source):
    if edges_count < source < 0:
        return

    def __min_distance(_dist, _spt_set):
        min_distance = float('inf')
        _min_index = 0
        for vertex in range(edges_count):
            if _dist[vertex] < min_distance and _spt_set[vertex] is False:
                min_distance = _dist[vertex]
                _min_index = vertex

        return _min_index

    dist = [float("Inf")] * edges_count
    dist[source] = 0
    spt_set = [False] * edges_count

    for _ in range(edges_count):
        min_index = __min_distance(dist, spt_set)
        spt_set[min_index] = True
        for edge, connected_edge, weight in graph:
            if dist[edge] != float("Inf") and spt_set[connected_edge] is False \
                    and dist[edge] + weight < dist[connected_edge]:
                dist[connected_edge] = dist[edge] + weight

    return dist


if __name__ == '__main__':
    test_graph = [
        (0, 1, 14),
        (0, 2, 2),
        (0, 3, 4),
        (1, 4, 1),
        (2, 3, 1),
        (3, 2, 1),
        (4, 1, 1)]

    print(dijkstra(test_graph, 5, 0))
