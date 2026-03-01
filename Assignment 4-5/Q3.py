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

def dls(node, goal, depth_limit, visited, path):
    visited.append(node)
    path.append(node)

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

def ids(start, goal):
    for depth in range(len(graph) + 1):
        print("\n--- Trying Depth =", depth, "---")
        visited = []
        path = []
        found = dls(start, goal, depth, visited, path)
        print("Nodes Visited:", visited)
        if found:
            print("Goal found! Path:", path)
            return
    print("Goal not reachable!")

ids(start, goal)
