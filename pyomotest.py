from pyomo.environ import * # For Pyomo 4.0 & later
# from coopr.pyomo import * # For earlier versions

model = ConcreteModel()
SolverFactory('cbc').solve(model).write()

expr = sum(i for i in range(31,36))

print(expr)