units = 250
previous_bill = 800

if units <= 100:
    bill = units * 3
elif units <= 300:
    bill = 300 + (units - 100) * 5
else:
    bill = 1300 + (units - 300) * 7
bill = bill + 50

print("Current Bill:", bill)

if bill > previous_bill * 1.2:
    print("Unusual Increase")
else:
    print("Normal Bill")