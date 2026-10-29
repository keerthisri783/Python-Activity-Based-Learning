basic = 20000
allowances = 3000
overtime = 1000
incentives = 500

gross = basic + allowances + overtime + incentives

if gross <= 20000:
    deduction = gross * 0.05
else:
    deduction = gross * 0.10

net = gross - deduction

print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)