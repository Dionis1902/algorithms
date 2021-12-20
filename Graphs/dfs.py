def dfs(graph, start, end):
    queue = [start]
    visited = []
    while queue:
        current = queue.pop()
        if end in graph.get(current, list()):
            return True
        visited.append(current)
        queue += [i for i in graph.get(current, list()) if i not in visited]
    return False


if __name__ == '__main__':
    test_graph = {
        'a': ['b', 'd', 'c'],
        'b': ['d'],
        'd': ['c'],
        'c': ['f'],
        'f': ['e'],
        'e': ['g']
    }
    print(dfs(test_graph, 'a', 'g'))
