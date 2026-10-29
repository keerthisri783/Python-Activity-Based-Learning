consultation = 200
diagnostic = 300
treatment = 500

total = consultation + diagnostic + treatment

if total >= 500:
    concession = 100
else:
    concession = 0

final_bill = total - concession

if final_bill >= 0:
    print("Total Bill:", total)
    print("Concession:", concession)
    print("Final Bill:", final_bill)
    print("Patient: Cash Payment")
else:
    print("Invalid Bill")