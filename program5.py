distance = 300
age = 65
fare = distance * 2

if age >= 60:
    fare = fare * 0.5

reservation_fee = 50
total = fare + reservation_fee

cancel = "no"

if cancel == "yes":
    total = total - 100

print("Ticket Fare:", fare)
print("Reservation Fee:", reservation_fee)
print("Final Fare:", total)