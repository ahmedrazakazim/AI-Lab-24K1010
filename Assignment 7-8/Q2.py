import math

def alpha_beta(tree, node, depth, alpha, beta, is_max):
    if not tree[node]:
        return node
    if is_max:
        val = -math.inf
        for child in tree[node]:
            val = max(val, alpha_beta(tree, child, depth-1, alpha, beta, False))
            alpha = max(alpha, val)
            if beta <= alpha:
                print(f"Pruned at {child}")
                break
        return val
    else:
        val = math.inf
        for child in tree[node]:
            val = min(val, alpha_beta(tree, child, depth-1, alpha, beta, True))
            beta = min(beta, val)
            if beta <= alpha:
                print(f"Pruned at {child}")
                break
        return val

tree = {
    'Root': ['N1', 'N2'],
    'N1': ['N3', 'N4'], 'N2': ['N5', 'N6'],
    'N3': [4, 7], 'N4': [2, 5],
    'N5': [1, 8], 'N6': [3, 6],
    4:[], 7:[], 2:[], 5:[], 1:[], 8:[], 3:[], 6:[]
}

print("Root value:", alpha_beta(tree, 'Root', 3, -math.inf, math.inf, True))
