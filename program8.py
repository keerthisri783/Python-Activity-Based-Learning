expenses = [100, 200, 300]
rate = 1.0
fee = 10
budget = 600

total = sum(expenses) * rate + fee

print("Total:", total)
print("Largest Expense:", max(expenses))

if total <= budget:
    print("Within Budget")
else:
    print("Over Budget")