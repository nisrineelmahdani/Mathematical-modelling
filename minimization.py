import pulp

print(pulp.listSolvers(onlyAvailable=True))

model = pulp.LpProblem("Toy_Advertising", pulp.LpMinimize)

C = model.add_variable(
    "Cartoon_Ads",
    lowBound=0,
    cat="Integer"
)

M = model.add_variable(
    "Movie_Ads",
    lowBound=0,
    cat="Integer"
)

model += 5000 * C + 12000 * M

model += 2 * C + 4 * M >= 30
model += C + 6 * M >= 40

solver = pulp.HiGHS(msg=True)

result = model.solve(solver)
print("Solver result:", result)
print("Cartoon ads:", C.value())
print("Movie ads:", M.value())
print("Minimum cost:", pulp.value(model.objective))