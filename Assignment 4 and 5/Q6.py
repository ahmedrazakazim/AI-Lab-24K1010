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


def a_star(start, goal):
    open_list = [(heuristic[start], start)]
    closed_list = []
    g = {start: 0}
    parent = {start: None}

    while len(open_list) > 0:
        open_list.sort(key=lambda x: x[1])
        f_val, curr = open_list.pop(0)

        if curr in closed_list:
            continue
        closed_list.append(curr)

        if curr == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, g[goal]

        for nb in graph[curr]:
            new_g = g[curr] + graph[curr][nb]
            new_f = new_g + heuristic[nb]
            if nb not in g or new_g < g[nb]:
                g[nb] = new_g
                parent[nb] = curr
                open_list.append((new_f, nb))

    return None, -1


path, cost = a_star(start, goal)
print("Initial path:", path)
print("Initial cost:", cost)

all_edges = []
for u in graph:
    for v in graph[u]:
        all_edges.append((u, v))

change_num = 1
while change_num <= 3:
    u, v = random.choice(all_edges)
    old = graph[u][v]
    delta = random.choice([-2, -3, 3, 4, 2])
    updated = old + delta
    if updated < 1:
        updated = 1
    graph[u][v] = updated

    print("\nChange", change_num, "- edge", u, "->", v, ":", old, "->", updated)

    path, cost = a_star(start, goal)
    print("New path:", path)
    print("New cost:", cost)

    change_num += 1
