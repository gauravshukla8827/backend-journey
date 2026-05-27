# Tip calculator

print("Welcome to the tip calculator")
bill = float(input("What was the total bill?"))
percentage = int(input("How much tip would you like to give?10, 12, or 15?"))
# 10, 12 or 15%
tip = (percentage*bill)/100
split = int(input("How much people to split the bill?"))
each_person_pay = (bill+tip)/split
print(f"Each person should pay: {each_person_pay}")