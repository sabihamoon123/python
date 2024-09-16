print("Thank you for choosing Python pizza deliveries!!!")
size = input()
add_peparoni = input()
extra_cheese = input()

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_peparoni == "Y":
    if size == "S":
     bill += 2
else:
     bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"The total bill {bill}.")
