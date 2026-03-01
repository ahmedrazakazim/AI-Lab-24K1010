graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}

start = 'A'
goal = 'G'

def dls(node, goal, limit, visited, path):
    visited.append(node)
    path.append(node)

    if node == goal:
        return True

    if limit == 0:
        path.pop()
        return False

    for child in graph[node]:
        if child not in visited:
            if dls(child, goal, limit - 1, visited, path):
                return True

    path.pop()
    return False


def ids(start, goal):
    depth = 0
    while depth <= len(graph):
        print("Trying depth:", depth)
        v = []
        p = []
        found = dls(start, goal, depth, v, p)
        print("Nodes visited at this depth:", v)
        if found:
            print("Goal found! Path:", p)
            return
        depth += 1
    print("Goal not reachable")


ids(start, goal)
