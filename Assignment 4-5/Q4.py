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
came_from = {start: None}
g_costs = {start: 0}

while frontier:
    frontier.sort(key=lambda x: x[0])
    cost, node = frontier.pop(0)

    if node in visited:
        continue

    print("Visiting:", node, "| Cost so far:", cost)
    visited.append(node)

    if node == goal:
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = came_from.get(current)
        path.reverse()
        print("\nLeast Cost Path:", path)
        print("Total Cost:", cost)
        break

    for neighbor, edge_cost in graph.get(node, {}).items():
        new_cost = cost + edge_cost
        if neighbor not in g_costs or new_cost < g_costs[neighbor]:
            g_costs[neighbor] = new_cost
            came_from[neighbor] = node
            frontier.append((new_cost, neighbor))
else:
    print("Goal not reachable!")
