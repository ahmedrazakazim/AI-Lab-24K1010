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
        if building[r][c] == 0:
            continue
        adj = []
        if r > 0 and building[r-1][c] == 1:
            adj.append((r-1, c))
        if r < rows-1 and building[r+1][c] == 1:
            adj.append((r+1, c))
        if c > 0 and building[r][c-1] == 1:
            adj.append((r, c-1))
        if c < cols-1 and building[r][c+1] == 1:
            adj.append((r, c+1))
        graph[(r, c)] = adj

print("Graph (Adjacency List):")
for key in graph:
    print(key, ":", graph[key])

visited = [start]
queue = [start]
parent = {}
parent[start] = None
order = []

while len(queue) > 0:
    curr = queue.pop(0)
    order.append(curr)

    if curr == goal:
        break

    for nb in graph[curr]:
        if nb not in visited:
            visited.append(nb)
            parent[nb] = curr
            queue.append(nb)

print("\nBFS Traversal Order:")
print(order)

if goal in parent or goal == start:
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    print("\nShortest Path from", start, "to", goal, ":")
    print(path)
else:
    print("No path found")
