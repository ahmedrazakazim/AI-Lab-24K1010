graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10},
    'B': {'E': 3},
    'C': {'G': 4},
    'D': {'G': 1},
    'E': {'D': 4},
    'G': {}
}

start = 'S'
goal = 'G'

frontier = [(0, start)]
visited = []
cost_so_far = {start: 0}
came_from = {start: None}

while len(frontier) > 0:
    frontier.sort(key=lambda x: x[0])
    cost, node = frontier.pop(0)

    if node in visited:
        continue

    visited.append(node)
    print("Expanding:", node, "| cost:", cost)

    if node == goal:
        break

    for neighbor in graph[node]:
        new_cost = cost + graph[node][neighbor]
        if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
            cost_so_far[neighbor] = new_cost
            came_from[neighbor] = node
            frontier.append((new_cost, neighbor))

if goal in came_from:
    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = came_from[curr]
    path.reverse()
    print("\nLeast Cost Path:", path)
    print("Total Cost:", cost_so_far[goal])
else:
    print("Goal not reachable")
