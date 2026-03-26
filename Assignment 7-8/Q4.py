from ortools.sat.python import cp_model

model = cp_model.CpModel()
a = model.new_int_var(0, 3, "A")
b = model.new_int_var(0, 3, "B")
c = model.new_int_var(0, 3, "C")

model.add(a != b)
model.add(b != c)
model.add(a + b <= 4)

solver = cp_model.CpSolver()
solver.solve(model)
print(f"A={solver.value(a)}, B={solver.value(b)}, C={solver.value(c)}")
