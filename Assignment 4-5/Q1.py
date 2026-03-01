building = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]

start = (0, 0)
goal = (3, 3)
rows = len(building)
cols = len(building[0])

graph = {}
for r in range(rows):
    for c in range(cols):
        if building[r][c] == 1:
            neighbors = []
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and building[nr][nc] == 1:
                    neighbors.append((nr, nc))
            graph[(r, c)] = neighbors

print("Adjacency List:")
for node in graph:
    print(node, "->", graph[node])

queue = [start]
visited = [start]
came_from = {start: None}
traversal = []

while queue:
    node = queue.pop(0)
    traversal.append(node)

    if node == goal:
        break

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            visited.append(neighbor)
            came_from[neighbor] = node
            queue.append(neighbor)

print("\nTraversal Order:", traversal)

path = []
current = goal
while current is not None:
    path.append(current)
    current = came_from.get(current)
path.reverse()

if goal in came_from:
    print("Shortest Path:", path)
else:
    print("No path found!")
