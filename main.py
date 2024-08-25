# Tip Calculator
# welcome
# Bill
# People
# Tip
# Tip/ 100
# Tip - Bill
# Bill/People
# Display
print("Welcome to the tip calculator")
bill = int(input("Enter bill amount $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What tip would you like to give? 10, 12, or 15? "))
tip_percent = int(tip)/100
tip_amount = int(bill) * int(tip_percent)
total_bill = int(bill) + int(tip_amount)
bill_per_person = int(total_bill)/int(people)
print(f"Each person should pay: ${bill_per_person}")










