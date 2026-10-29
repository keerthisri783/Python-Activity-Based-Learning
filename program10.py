marks = [35, 32, 40]
grace = 3
passed = []

for m in marks:
    if m < 35 and m + grace >= 35:
        m = min(m + grace, 100)
    passed.append(m)

print("Marks:", passed)
print("Total:", sum(passed))
print("Result:", "Pass" if all(m >= 35 for m in passed) else "Fail")
