maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goals = [(2, 1), (4, 4)]

rows = len(maze)
cols = len(maze[0])

def manhattan(pos, target):
    return abs(pos[0] - target[0]) + abs(pos[1] - target[1])

def best_first(maze, start, end):
    frontier = [(manhattan(start, end), start, [start])]
    visited = []

    while frontier:
        frontier.sort(key=lambda x: x[0])
        h, current, path = frontier.pop(0)

        if current in visited:
            continue
        visited.append(current)

        if current == end:
            return path

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = current[0] + dr, current[1] + dc
            new_pos = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and new_pos not in visited:
                frontier.append((manhattan(new_pos, end), new_pos, path + [new_pos]))

    return None

full_path = []
current_start = start

for i in range(len(goals)):
    goal = goals[i]
    print("Searching for goal", i + 1, ":", goal)
    segment = best_first(maze, current_start, goal)

    if segment is None:
        print("Could not reach goal", goal)
        break

    print("Path segment:", segment)

    if full_path:
        full_path += segment[1:]
    else:
        full_path += segment

    current_start = goal

print("\nFull path covering all goals:", full_path)
print("Total steps:", len(full_path) - 1)
