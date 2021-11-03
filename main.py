import string

#              A   B   C   D   E
TEST_GRAPH = [[0,  14, 2,  4,  0],  # A
              [14, 0,  0,  0,  1],  # B
              [2,  0,  0,  1,  0],  # C
              [4,  0,  1,  0,  0],  # D
              [0,  1,  0,  0,  0]]  # E


def prima(graph):
    vertex_count = len(graph)
    selected_node = [0] * vertex_count
    selected_node[0] = True
    return_data = {}
    for _ in range(vertex_count - 1):
        minimum = float('inf')
        a = 0
        b = 0
        for i in range(vertex_count):
            if selected_node[i]:
                for j in range(vertex_count):
                    if not selected_node[j] and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            a = i
                            b = j
        return_data[string.ascii_uppercase[a] + "-" + string.ascii_uppercase[b]] = graph[a][b]
        selected_node[b] = True
    return return_data


if __name__ == '__main__':
    result = prima(TEST_GRAPH)

    print(result, sum(result.values()))
