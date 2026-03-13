import random

def f(x):
    return -x**2 + 6*x

x = random.randint(0, 6)
print(f"Start: x = {x}, f(x) = {f(x)}")

step = 1
while True:
    curr = f(x)
    left  = f(x - 1) if x - 1 >= 0 else float('-inf')
    right = f(x + 1) if x + 1 <= 6 else float('-inf')

    if max(left, right) <= curr:
        break

    if left > right:
        x = x - 1
    else:
        x = x + 1

    print(f"Step {step}: x = {x}, f(x) = {f(x)}")
    step += 1

print(f"\nDone — x = {x}, f(x) = {f(x)}")
