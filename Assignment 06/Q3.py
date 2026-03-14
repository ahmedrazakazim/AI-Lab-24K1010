import random

def fitness(x):
    return x*x + 2*x

n    = 6
gens = 15
mr   = 0.1

def decode(b):
    return int(b, 2)

def new_chr():
    return ''.join(random.choice('01') for _ in range(5))

def pick(pop):
    p1 = random.choice(pop)
    p2 = random.choice(pop)
    if fitness(decode(p1)) >= fitness(decode(p2)):
        return p1
    return p2

def cross(p1, p2):
    pt = random.randint(1, 4)
    return p1[:pt] + p2[pt:]

def mutate(ch):
    out = ''
    for b in ch:
        if random.random() < mr:
            out += '0' if b == '1' else '1'
        else:
            out += b
    return out

pop = [new_chr() for _ in range(n)]

for g in range(1, gens + 1):
    pop.sort(key=lambda c: fitness(decode(c)), reverse=True)
    top = pop[0]
    print(f"Gen {g:02}:  {top}  x={decode(top)}  f={fitness(decode(top))}")

    nx = [top]
    while len(nx) < n:
        p1    = pick(pop)
        p2    = pick(pop)
        child = mutate(cross(p1, p2))
        nx.append(child)
    pop = nx

best = max(pop, key=lambda c: fitness(decode(c)))
print(f"\nBest chromosome : {best}")
print(f"Best x          : {decode(best)}")
print(f"Best fitness    : {fitness(decode(best))}")
