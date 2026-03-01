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


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def best_first(start, end):
    open_list = [(manhattan(start, end), start, [start])]
    closed_list = []

    while len(open_list) > 0:
        open_list.sort(key=lambda x: x[0])
        h, curr, path = open_list.pop(0)

        if curr in closed_list:
            continue
        closed_list.append(curr)

        if curr == end:
            return path

        r, c = curr
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r+dr, c+dc
            npos = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] == 0 and npos not in closed_list:
                    open_list.append((manhattan(npos, end), npos, path + [npos]))

    return None


full_path = []
curr_start = start

for i in range(len(goals)):
    g = goals[i]
    print("Looking for goal", i+1, "at", g)
    seg = best_first(curr_start, g)
    if seg is None:
        print("Could not reach", g)
        break
    print("Segment:", seg)
    if len(full_path) == 0:
        full_path = seg
    else:
        full_path = full_path + seg[1:]
    curr_start = g

print("\nComplete path through all goals:")
print(full_path)
print("Steps taken:", len(full_path) - 1)
