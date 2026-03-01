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
goal = 'H'

def dls(node, goal, depth_limit, visited, path):
    visited.append(node)
    path.append(node)
    print("Visiting:", node)

    if node == goal:
        return True

    if depth_limit == 0:
        path.pop()
        return False

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dls(neighbor, goal, depth_limit - 1, visited, path):
                return True

    path.pop()
    return False

for limit in [2, 3]:
    print("\n--- Depth Limit =", limit, "---")
    visited = []
    path = []
    found = dls(start, goal, limit, visited, path)
    print("Nodes Visited:", visited)
    if found:
        print("Goal found! Path:", path)
    else:
        print("Goal NOT found within depth limit", limit)
