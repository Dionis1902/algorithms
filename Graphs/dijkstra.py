def dijkstra(graph, source):
    if 0 > source > len(graph):
        return

    def __min_distance(dist, spt_set):
        min_distance = float('inf')
        min_index = 0
        for vertex in range(vertex_count):
            if dist[vertex] < min_distance and spt_set[vertex] is False:
                min_distance = dist[vertex]
                min_index = vertex

        return min_index

    vertex_count = len(graph)
    dist = [float('inf')] * vertex_count
    dist[source] = 0
    spt_set = [False] * vertex_count

    for _ in range(vertex_count):
        min_index = __min_distance(dist, spt_set)

        spt_set[min_index] = True
        for vertex in range(vertex_count):
            if graph[min_index][vertex] > 0 and spt_set[vertex] is False \
                    and dist[vertex] > dist[min_index] + graph[min_index][vertex]:
                dist[vertex] = dist[min_index] + graph[min_index][vertex]
    return dist


if __name__ == '__main__':
    #              A   B   C   D   E
    test_graph = [[0,  14, 2,  4,  0],  # A
                  [14, 0,  0,  0,  1],  # B
                  [2,  0,  0,  1,  0],  # C
                  [4,  0,  1,  0,  0],  # D
                  [0,  1,  0,  0,  0]]  # E

    print(dijkstra(test_graph, 0))