cost = 21000
sponsorship = 15000
fee = 200

shortfall = max(0, cost - sponsorship)
participants = (shortfall + fee - 1) // fee

print("Total Cost:", cost)
print("Shortfall:", shortfall)
print("Break-even Registrations:", participants)