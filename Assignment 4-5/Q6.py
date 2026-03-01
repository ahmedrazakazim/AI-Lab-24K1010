import random

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

heuristic = {'A': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0}

start = 'A'
goal = 'G'

def a_star(graph, start, goal):
    frontier = [(start, 0 + heuristic[start])]
    visited = []
    g_costs = {start: 0}
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, current_f = frontier.pop(0)

        if current_node in visited:
            continue

        visited.append(current_node)

        if current_node == goal:
            path = []
            current = goal
            while current is not None:
                path.append(current)
                current = came_from.get(current)
            path.reverse()
            return path, g_costs[goal]

        for neighbor, cost in graph.get(current_node, {}).items():
            new_g = g_costs[current_node] + cost
            f_val = new_g + heuristic[neighbor]
            if neighbor not in g_costs or new_g < g_costs[neighbor]:
                g_costs[neighbor] = new_g
                came_from[neighbor] = current_node
                frontier.append((neighbor, f_val))

    return None, float('inf')

path, cost = a_star(graph, start, goal)
print("Initial A* Run")
print("Path:", path)
print("Total Cost:", cost)

edges = []
for u in graph:
    for v in graph[u]:
        edges.append((u, v))

for i in range(1, 4):
    u, v = random.choice(edges)
    old_cost = graph[u][v]
    delta = random.choice([-3, -2, 2, 3, 4])
    new_cost = max(1, old_cost + delta)
    graph[u][v] = new_cost

    print("\n--- Change", i, ": Edge", u, "->", v, "cost", old_cost, "->", new_cost, "---")

    path, cost = a_star(graph, start, goal)
    print("Updated Path:", path)
    print("Updated Cost:", cost)
