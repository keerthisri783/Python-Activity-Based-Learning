budget = 300
usage = 2

plan1 = 199
plan2 = 249
plan3 = 349

if plan1 <= budget:
    best = plan1
elif plan2 <= budget:
    best = plan2
else:
    best = plan3

print("Best Plan:", best)
print("Budget:", budget)

if best <= budget:
    print("Plan is Eligible")
else:
    print("No Plan Available")