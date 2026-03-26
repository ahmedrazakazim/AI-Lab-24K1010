import math

def minimax(tree, node, depth, is_max):
    if not tree[node]:
        return node
    children = tree[node]
    values = [minimax(tree, c, depth-1, not is_max) for c in children]
    return max(values) if is_max else min(values)

tree = {
    'Root': ['N1', 'N2'],
    'N1': ['N3', 'N4'], 'N2': ['N5', 'N6'],
    'N3': [4, 7], 'N4': [2, 5],
    'N5': [1, 8], 'N6': [3, 6],
    4:[], 7:[], 2:[], 5:[], 1:[], 8:[], 3:[], 6:[]
}

print("Root value:", minimax(tree, 'Root', 3, True))
