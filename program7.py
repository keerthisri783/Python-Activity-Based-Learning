material = 500
labour = 200
machine = 100
wastage = 50
selling_price = 1100
target = 200

total_cost = material + labour + machine + wastage
profit = selling_price - total_cost

print("Total Cost:", total_cost)
print("Profit:", profit)

if profit >= target:
    print("Target Achieved")
else:
    print("Target Not Achieved")