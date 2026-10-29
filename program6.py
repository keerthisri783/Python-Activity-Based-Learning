price = 100
quantity = 2
tax = 5

total = price * quantity
total = total + (total * tax / 100)

if total >= 200:
    discount = min(total * 0.10, 30)
else:
    discount = 0

final_bill = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)