test_graph = {
    'a': ['b', 'd', 'c'],
    'b': ['f'],
    'd': ['f'],
    'c': ['f'],
    'f': ['e'],
    'e': ['g']
}


def breadth_first_search(graph, start, end):
    queue = [start]
    while len(queue) > 0:
        current = queue.pop(0)
        if current not in graph:
            graph[current] = []
        if end in graph[current]:
            return True
        queue = [*queue, *graph[current]]
    return False


if __name__ == '__main__':
    print(breadth_first_search(test_graph, 'a', 'f'))
