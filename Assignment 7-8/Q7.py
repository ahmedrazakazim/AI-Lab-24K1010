from ortools.sat.python import cp_model

model = cp_model.CpModel()
n = 4
queens = [model.new_int_var(0, n-1, f"q{i}") for i in range(n)]

model.add_all_different(queens)
model.add_all_different([queens[i] + i for i in range(n)])
model.add_all_different([queens[i] - i for i in range(n)])

solver = cp_model.CpSolver()
solver.solve(model)

for row in range(n):
    print(" ".join("Q" if solver.value(queens[col]) == row else "_" for col in range(n)))
