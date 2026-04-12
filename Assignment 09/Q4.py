import numpy as np
 
states = ['Sunny', 'Cloudy', 'Rainy']
 
T = np.array([
    [0.60, 0.30, 0.10],
    [0.30, 0.40, 0.30],
    [0.20, 0.30, 0.50],
])
 
print("\nTransition Matrix:")
print(f"{'':10} {'Sunny':>8} {'Cloudy':>8} {'Rainy':>8}")
for i, row in enumerate(T):
    print(f"{states[i]:10} {row[0]:8.2f} {row[1]:8.2f} {row[2]:8.2f}")
 
np.random.seed(42)
cur = 0
seq = [cur]
 
print("\nSimulated 10-day weather (starting Sunny):")
print(f"  Day  1: {states[cur]}")
 
for day in range(2, 11):
    cur = np.random.choice(3, p=T[cur])
    seq.append(cur)
    print(f"  Day {day:2d}: {states[cur]}")
 
print(f"\nTotal Rainy days in simulation: {seq.count(2)}")
 
n_sim = 100000
count = 0
 
for _ in range(n_sim):
    s = 0
    rain = 0
    for _ in range(10):
        s = np.random.choice(3, p=T[s])
        if s == 2:
            rain += 1
    if rain >= 3:
        count += 1
 
p_rain3 = count / n_sim
print(f"\nP(at least 3 rainy days in 10 days) via Monte Carlo ({n_sim:,} simulations):")
print(f"  {p_rain3:.4f} ({p_rain3 * 100:.2f}%)")
