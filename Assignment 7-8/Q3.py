import math


tree = {
    'Root': ['N1', 'N2'],
    'N1': ['N3', 'N4'], 'N2': ['N5', 'N6'],
    'N3': [4, 9, 2], 'N4': [6, 1],   
    'N5': [5, 3],    'N6': [7, 0],
    4:[], 9:[], 2:[], 6:[], 1:[], 5:[], 3:[], 7:[], 0:[]
}

def minimax(tree, node, is_max):
    if not tree[node]: return node
    values = [minimax(tree, c, not is_max) for c in tree[node]]
    return max(values) if is_max else min(values)

def alpha_beta(tree, node, alpha, beta, is_max):
    if not tree[node]: return node
    if is_max:
        val = -math.inf
        for c in tree[node]:
            val = max(val, alpha_beta(tree, c, alpha, beta, False))
            alpha = max(alpha, val)
            if beta <= alpha: print(f"Pruned: {c}"); break
        return val
    else:
        val = math.inf
        for c in tree[node]:
            val = min(val, alpha_beta(tree, c, alpha, beta, True))
            beta = min(beta, val)
            if beta <= alpha: print(f"Pruned: {c}"); break
        return val

print("Minimax root:", minimax(tree, 'Root', True))
print("Alpha-Beta root:", alpha_beta(tree, 'Root', -math.inf, math.inf, True))
print("Root value changed due to modified leaves and extra branch on N3.")
