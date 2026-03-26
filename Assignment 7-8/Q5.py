from ortools.sat.python import cp_model

class PrintSolutions(cp_model.CpSolverSolutionCallback):
    def __init__(self, vars):
        super().__init__()
        self.vars = vars
        self.count = 0
    def on_solution_callback(self):
        self.count += 1
        print({v.name: self.value(v) for v in self.vars})

model = cp_model.CpModel()
a = model.new_int_var(0, 3, "A")
b = model.new_int_var(0, 3, "B")
c = model.new_int_var(0, 3, "C")

model.add(a != b)
model.add(b != c)
model.add(a + b <= 4)

solver = cp_model.CpSolver()
cb = PrintSolutions([a, b, c])
solver.parameters.enumerate_all_solutions = True
solver.solve(model, cb)
print(f"Total: {cb.count} solutions")
