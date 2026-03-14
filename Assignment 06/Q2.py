def h(n):
    return abs(20 - n)

beam = [{"val": 1, "path": [1]}]
goal = 20
k    = 2
lvl  = 0

while beam:
    states_info = [f"{s['val']}(h={h(s['val'])})" for s in beam]
    print(f"Level {lvl}: {states_info}")

    goal_state = None
    for s in beam:
        if s["val"] == goal:
            goal_state = s
            break

    if goal_state:
        print(f"\nReached {goal}")
        print(f"Path: {goal_state['path']}")
        break

    nxt  = []
    seen = set()

    for s in beam:
        for nv in [s["val"]+2, s["val"]+3, s["val"]*2]:
            if nv <= goal and nv not in seen:
                seen.add(nv)
                nxt.append({"val": nv, "path": s["path"] + [nv]})

    nxt.sort(key=lambda s: h(s["val"]))
    beam = nxt[:k]
    lvl += 1
