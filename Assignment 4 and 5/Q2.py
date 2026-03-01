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

def dls(node, goal, limit, visited, path):
    visited.append(node)
    path.append(node)
    print("  Visited:", node)

    if node == goal:
        return True

    if limit == 0:
        path.pop()
        return False

    for child in graph[node]:
        if child not in visited:
            result = dls(child, goal, limit - 1, visited, path)
            if result == True:
                return True

    path.pop()
    return False


print("--- Running DLS with depth limit = 2 ---")
v = []
p = []
found = dls(start, goal, 2, v, p)
print("Nodes visited:", v)
if found:
    print("Goal found! Path:", p)
else:
    print("Goal not found within depth 2")

print()
print("--- Running DLS with depth limit = 3 ---")
v = []
p = []
found = dls(start, goal, 3, v, p)
print("Nodes visited:", v)
if found:
    print("Goal found! Path:", p)
else:
    print("Goal not found within depth 3")
